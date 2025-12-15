# generate_dataset.py
from __future__ import annotations

import json
import gzip
import random
from dataclasses import dataclass
from typing import List, Optional, TextIO, Dict, Tuple

from rule_solver import (
    Cube,
    MOVE_LIST_12,
    check_state,
    iddfs,
    cube_to_vec48,
    do_path,
)

MOVE_TO_ID: Dict[str, int] = {m: i for i, m in enumerate(MOVE_LIST_12)}


def open_text(path: str) -> TextIO:
    """Open text file; uses gzip if path ends with .gz."""
    if path.endswith(".gz"):
        return gzip.open(path, "wt", encoding="utf-8")
    return open(path, "w", encoding="utf-8")


def random_scramble(rng: random.Random, length: int = 25) -> List[str]:
    """
    Simple scramble generator using the same 12 moves as your solver.
    Avoids repeating the same face twice in a row (e.g., R then r).
    """
    out: List[str] = []
    last_face: Optional[str] = None  # e.g., "R", "U", ...
    for _ in range(length):
        m = rng.choice(MOVE_LIST_12)
        face = m.upper()
        while face == last_face:
            m = rng.choice(MOVE_LIST_12)
            face = m.upper()
        out.append(m)
        last_face = face
    return out


@dataclass
class GenConfig:
    num_scrambles: int = 1000
    scramble_len: int = 25
    goal_max: int = 29          # 0..29 => cross + F2L + U-edge orientation in your ladder
    seed: int = 0

    # safety limits (avoid infinite loops if something goes weird)
    max_teacher_calls_per_goal: int = 50
    max_moves_per_goal: int = 200
    max_total_moves_per_scramble: int = 5000

    # optional: also write scrambles list to a separate file
    scrambles_out_path: Optional[str] = None


def generate_policy_dataset_jsonl(
    out_path: str,
    cfg: GenConfig = GenConfig(),
) -> Tuple[int, int]:
    """
    Writes JSONL rows:
      {
        "scramble_id": int,
        "goal": int,
        "lastMove": int (-1..11),
        "state": [48 ints 0..5],
        "move": int (0..11)
      }

    Returns: (num_rows_written, num_successful_scrambles)
    """
    rng = random.Random(cfg.seed)

    rows_written = 0
    successful_scrambles = 0

    scrambles_f = open_text(cfg.scrambles_out_path) if cfg.scrambles_out_path else None

    with open_text(out_path) as f:
        for sid in range(cfg.num_scrambles):
            cube = Cube.solved()
            scramble = random_scramble(rng, cfg.scramble_len)
            do_path(cube, scramble)

            if scrambles_f:
                scrambles_f.write(json.dumps({"scramble_id": sid, "scramble": "".join(scramble)}) + "\n")

            last_move_id = -1
            total_moves = 0
            ok = True

            for goal in range(cfg.goal_max + 1):
                teacher_calls = 0
                moves_this_goal = 0

                while not check_state(cube, goal):
                    teacher_calls += 1
                    if teacher_calls > cfg.max_teacher_calls_per_goal:
                        ok = False
                        break

                    if moves_this_goal > cfg.max_moves_per_goal:
                        ok = False
                        break

                    if total_moves > cfg.max_total_moves_per_scramble:
                        ok = False
                        break

                    path = iddfs(cube, goal)
                    if path is None:
                        ok = False
                        break

                    # Execute teacher path move-by-move, logging each step
                    for m in path:
                        row = {
                            "scramble_id": sid,
                            "goal": goal,
                            "lastMove": last_move_id,
                            "state": cube_to_vec48(cube),
                            "move": MOVE_TO_ID[m],
                        }
                        f.write(json.dumps(row) + "\n")
                        rows_written += 1

                        cube.apply_move(m)
                        last_move_id = MOVE_TO_ID[m]
                        total_moves += 1
                        moves_this_goal += 1

                        if check_state(cube, goal):
                            break

                if not ok:
                    break

            if ok:
                successful_scrambles += 1

            if (sid + 1) % 50 == 0:
                print(
                    f"[{sid+1}/{cfg.num_scrambles}] rows={rows_written} "
                    f"success={successful_scrambles}"
                )

    if scrambles_f:
        scrambles_f.close()

    print(f"Done. Wrote {rows_written} rows. Successful scrambles: {successful_scrambles}/{cfg.num_scrambles}")
    return rows_written, successful_scrambles


if __name__ == "__main__":
    cfg = GenConfig(
        num_scrambles=500,
        scramble_len=25,
        goal_max=29,
        seed=123,
        scrambles_out_path="scrambles.jsonl.gz",
    )
    generate_policy_dataset_jsonl("policy_dataset.jsonl.gz", cfg)
