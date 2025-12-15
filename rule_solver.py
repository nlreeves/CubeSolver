# rule_solver.py
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Tuple, Dict, Iterable


MOVE_LIST_12 = ["U", "u", "R", "r", "F", "f", "D", "d", "L", "l", "B", "b"]

INVERSE_MOVE: Dict[str, str] = {
    "U": "u", "u": "U",
    "R": "r", "r": "R",
    "F": "f", "f": "F",
    "D": "d", "d": "D",
    "L": "l", "l": "L",
    "B": "b", "b": "B",
}


def _rot_face_4(face: List[str]) -> None:
    """JS: face.unshift(face.pop()) for 4 items"""
    face.insert(0, face.pop())


@dataclass
class Cube:
    cube_edges: List[List[str]]
    cube_corners: List[List[str]]

    @staticmethod
    def solved() -> "Cube":
        # Match your makeCube()
        array_corners = [
            ["g", "g", "g", "g"],
            ["r", "r", "r", "r"],
            ["b", "b", "b", "b"],
            ["o", "o", "o", "o"],
            ["w", "w", "w", "w"],
            ["y", "y", "y", "y"],
        ]
        array_edges = [
            ["g", "g", "g", "g"],
            ["r", "r", "r", "r"],
            ["b", "b", "b", "b"],
            ["o", "o", "o", "o"],
            ["w", "w", "w", "w"],
            ["y", "y", "y", "y"],
        ]
        return Cube(array_edges, array_corners)

    def clone(self) -> "Cube":
        e = [row[:] for row in self.cube_edges]
        c = [row[:] for row in self.cube_corners]
        return Cube(e, c)

    # ---- moves (direct port) ----
    def right(self) -> None:
        _rot_face_4(self.cube_edges[1])
        _rot_face_4(self.cube_corners[1])

        temp = self.cube_edges[0][1]
        self.cube_edges[0][1] = self.cube_edges[5][1]
        self.cube_edges[5][1] = self.cube_edges[2][1]
        self.cube_edges[2][1] = self.cube_edges[4][1]
        self.cube_edges[4][1] = temp

        temp = self.cube_corners[0][1]
        temp2 = self.cube_corners[0][2]
        self.cube_corners[0][1] = self.cube_corners[5][1]
        self.cube_corners[0][2] = self.cube_corners[5][2]
        self.cube_corners[5][1] = self.cube_corners[2][1]
        self.cube_corners[5][2] = self.cube_corners[2][2]
        self.cube_corners[2][1] = self.cube_corners[4][1]
        self.cube_corners[2][2] = self.cube_corners[4][2]
        self.cube_corners[4][1] = temp
        self.cube_corners[4][2] = temp2

    def right_prime(self) -> None:
        self.right(); self.right(); self.right()

    def left(self) -> None:
        _rot_face_4(self.cube_edges[3])
        _rot_face_4(self.cube_corners[3])

        temp = self.cube_edges[0][3]
        self.cube_edges[0][3] = self.cube_edges[4][3]
        self.cube_edges[4][3] = self.cube_edges[2][3]
        self.cube_edges[2][3] = self.cube_edges[5][3]
        self.cube_edges[5][3] = temp

        temp = self.cube_corners[0][0]
        temp2 = self.cube_corners[0][3]
        self.cube_corners[0][0] = self.cube_corners[4][0]
        self.cube_corners[0][3] = self.cube_corners[4][3]
        self.cube_corners[4][0] = self.cube_corners[2][0]
        self.cube_corners[4][3] = self.cube_corners[2][3]
        self.cube_corners[2][0] = self.cube_corners[5][0]
        self.cube_corners[2][3] = self.cube_corners[5][3]
        self.cube_corners[5][0] = temp
        self.cube_corners[5][3] = temp2

    def left_prime(self) -> None:
        self.left(); self.left(); self.left()

    def up(self) -> None:
        _rot_face_4(self.cube_edges[4])
        _rot_face_4(self.cube_corners[4])

        temp = self.cube_edges[0][0]
        self.cube_edges[0][0] = self.cube_edges[1][0]
        self.cube_edges[1][0] = self.cube_edges[2][2]
        self.cube_edges[2][2] = self.cube_edges[3][0]
        self.cube_edges[3][0] = temp

        temp = self.cube_corners[0][0]
        temp2 = self.cube_corners[0][1]
        self.cube_corners[0][0] = self.cube_corners[1][0]
        self.cube_corners[0][1] = self.cube_corners[1][1]
        self.cube_corners[1][0] = self.cube_corners[2][2]
        self.cube_corners[1][1] = self.cube_corners[2][3]
        self.cube_corners[2][2] = self.cube_corners[3][0]
        self.cube_corners[2][3] = self.cube_corners[3][1]
        self.cube_corners[3][0] = temp
        self.cube_corners[3][1] = temp2

    def up_prime(self) -> None:
        self.up(); self.up(); self.up()

    def down(self) -> None:
        _rot_face_4(self.cube_edges[5])
        _rot_face_4(self.cube_corners[5])

        temp = self.cube_edges[0][2]
        self.cube_edges[0][2] = self.cube_edges[3][2]
        self.cube_edges[3][2] = self.cube_edges[2][0]
        self.cube_edges[2][0] = self.cube_edges[1][2]
        self.cube_edges[1][2] = temp

        temp = self.cube_corners[0][2]
        temp2 = self.cube_corners[0][3]
        self.cube_corners[0][2] = self.cube_corners[3][2]
        self.cube_corners[0][3] = self.cube_corners[3][3]
        self.cube_corners[3][2] = self.cube_corners[2][0]
        self.cube_corners[3][3] = self.cube_corners[2][1]
        self.cube_corners[2][0] = self.cube_corners[1][2]
        self.cube_corners[2][1] = self.cube_corners[1][3]
        self.cube_corners[1][2] = temp
        self.cube_corners[1][3] = temp2

    def down_prime(self) -> None:
        self.down(); self.down(); self.down()

    def front(self) -> None:
        _rot_face_4(self.cube_edges[0])
        _rot_face_4(self.cube_corners[0])

        temp = self.cube_edges[4][2]
        self.cube_edges[4][2] = self.cube_edges[3][1]
        self.cube_edges[3][1] = self.cube_edges[5][0]
        self.cube_edges[5][0] = self.cube_edges[1][3]
        self.cube_edges[1][3] = temp

        temp = self.cube_corners[4][3]
        temp2 = self.cube_corners[4][2]
        self.cube_corners[4][2] = self.cube_corners[3][1]
        self.cube_corners[4][3] = self.cube_corners[3][2]
        self.cube_corners[3][1] = self.cube_corners[5][0]
        self.cube_corners[3][2] = self.cube_corners[5][1]
        self.cube_corners[5][0] = self.cube_corners[1][3]
        self.cube_corners[5][1] = self.cube_corners[1][0]
        self.cube_corners[1][0] = temp
        self.cube_corners[1][3] = temp2

    def front_prime(self) -> None:
        self.front(); self.front(); self.front()

    def back(self) -> None:
        _rot_face_4(self.cube_edges[2])
        _rot_face_4(self.cube_corners[2])

        temp = self.cube_edges[4][0]
        self.cube_edges[4][0] = self.cube_edges[1][1]
        self.cube_edges[1][1] = self.cube_edges[5][2]
        self.cube_edges[5][2] = self.cube_edges[3][3]
        self.cube_edges[3][3] = temp

        temp = self.cube_corners[4][0]
        temp2 = self.cube_corners[4][1]
        self.cube_corners[4][0] = self.cube_corners[1][1]
        self.cube_corners[4][1] = self.cube_corners[1][2]
        self.cube_corners[1][1] = self.cube_corners[5][2]
        self.cube_corners[1][2] = self.cube_corners[5][3]
        self.cube_corners[5][2] = self.cube_corners[3][3]
        self.cube_corners[5][3] = self.cube_corners[3][0]
        self.cube_corners[3][3] = temp
        self.cube_corners[3][0] = temp2

    def back_prime(self) -> None:
        self.back(); self.back(); self.back()

    def apply_move(self, m: str) -> None:
        if m == "R": self.right()
        elif m == "r": self.right_prime()
        elif m == "L": self.left()
        elif m == "l": self.left_prime()
        elif m == "U": self.up()
        elif m == "u": self.up_prime()
        elif m == "D": self.down()
        elif m == "d": self.down_prime()
        elif m == "F": self.front()
        elif m == "f": self.front_prime()
        elif m == "B": self.back()
        elif m == "b": self.back_prime()
        else:
            raise ValueError(f"Unknown move: {m}")


def do_path(cube: Cube, path: Iterable[str]) -> None:
    for m in path:
        cube.apply_move(m)


def undo_path(cube: Cube, path: Iterable[str]) -> None:
    # reverse + inverse
    seq = list(path)
    for m in reversed(seq):
        cube.apply_move(INVERSE_MOVE[m])


# ---- checks (direct port) ----
def check_bottom_edges(cube: Cube, num: int) -> bool:
    count = 0
    if cube.cube_edges[0][2] == "g" and cube.cube_edges[5][0] == "y": count += 1
    if cube.cube_edges[1][2] == "r" and cube.cube_edges[5][1] == "y": count += 1
    if cube.cube_edges[3][2] == "o" and cube.cube_edges[5][3] == "y": count += 1
    if cube.cube_edges[2][0] == "b" and cube.cube_edges[5][2] == "y": count += 1
    return num <= count


def check_bottom_corners(cube: Cube, num: int) -> bool:
    count = 0
    if (cube.cube_corners[1][2] == "r" and cube.cube_corners[5][2] == "y" and cube.cube_corners[2][1] == "b"):
        count += 1
    if (cube.cube_corners[3][3] == "o" and cube.cube_corners[5][3] == "y" and cube.cube_corners[2][0] == "b"):
        count += 1
    if (cube.cube_corners[0][3] == "g" and cube.cube_corners[5][0] == "y" and cube.cube_corners[3][2] == "o"):
        count += 1
    if (cube.cube_corners[0][2] == "g" and cube.cube_corners[5][1] == "y" and cube.cube_corners[1][3] == "r"):
        count += 1
    return num <= count


def check_middle_edges(cube: Cube, num: int) -> bool:
    count = 0
    if (cube.cube_edges[2][1] == "b" and cube.cube_edges[1][1] == "r" and
        cube.cube_corners[5][2] == "y" and cube.cube_corners[1][2] == "r" and cube.cube_corners[2][1] == "b"):
        count += 1
    if (cube.cube_edges[2][3] == "b" and cube.cube_edges[3][3] == "o" and
        cube.cube_corners[5][3] == "y" and cube.cube_corners[3][3] == "o" and cube.cube_corners[2][0] == "b"):
        count += 1
    if (cube.cube_edges[0][1] == "g" and cube.cube_edges[1][3] == "r" and
        cube.cube_corners[5][1] == "y" and cube.cube_corners[1][3] == "r" and cube.cube_corners[0][2] == "g"):
        count += 1
    if (cube.cube_edges[0][3] == "g" and cube.cube_edges[3][1] == "o" and
        cube.cube_corners[5][0] == "y" and cube.cube_corners[3][2] == "o" and cube.cube_corners[0][3] == "g"):
        count += 1
    return num <= count


def corner_in_top(cube: Cube) -> bool:
    if cube.cube_corners[0][0] == "y" or cube.cube_corners[0][1] == "y": return True
    if cube.cube_corners[1][0] == "y" or cube.cube_corners[1][1] == "y": return True
    if cube.cube_corners[2][2] == "y" or cube.cube_corners[2][3] == "y": return True
    if cube.cube_corners[3][0] == "y" or cube.cube_corners[3][1] == "y": return True
    return False


def edge_in_top(cube: Cube) -> bool:
    if ((cube.cube_edges[0][0] != "w" and cube.cube_edges[4][2] != "w") or
        (cube.cube_edges[3][0] != "w" and cube.cube_edges[4][3] != "w") or
        (cube.cube_edges[1][0] != "w" and cube.cube_edges[4][1] != "w") or
        (cube.cube_edges[2][2] != "w" and cube.cube_edges[4][0] != "w")):
        return True
    return False


def corner_edge_pair(cube: Cube) -> bool:
    if (cube.cube_corners[0][0] == "y" and cube.cube_corners[4][3] == cube.cube_edges[4][3] and cube.cube_corners[3][1] == cube.cube_edges[3][0]):
        return True
    if (cube.cube_corners[0][1] == "y" and cube.cube_corners[4][2] == cube.cube_edges[4][1] and cube.cube_corners[1][0] == cube.cube_edges[1][0]):
        return True
    if (cube.cube_corners[3][1] == "y" and cube.cube_corners[4][3] == cube.cube_edges[4][2] and cube.cube_corners[0][0] == cube.cube_edges[0][0]):
        return True
    if (cube.cube_corners[3][0] == "y" and cube.cube_corners[4][0] == cube.cube_edges[4][0] and cube.cube_corners[2][3] == cube.cube_edges[2][2]):
        return True
    if (cube.cube_corners[2][3] == "y" and cube.cube_corners[4][0] == cube.cube_edges[4][3] and cube.cube_corners[3][0] == cube.cube_edges[3][0]):
        return True
    if (cube.cube_corners[2][2] == "y" and cube.cube_corners[4][1] == cube.cube_edges[4][1] and cube.cube_corners[1][1] == cube.cube_edges[1][0]):
        return True
    if (cube.cube_corners[1][1] == "y" and cube.cube_corners[4][1] == cube.cube_edges[4][0] and cube.cube_corners[2][2] == cube.cube_edges[2][2]):
        return True
    if (cube.cube_corners[1][0] == "y" and cube.cube_corners[4][2] == cube.cube_edges[4][2] and cube.cube_corners[0][1] == cube.cube_edges[0][0]):
        return True
    return False


def check_top_edges(cube: Cube, num: int) -> bool:
    count = 0
    if cube.cube_edges[4][0] == "w": count += 1
    if cube.cube_edges[4][1] == "w": count += 1
    if cube.cube_edges[4][2] == "w": count += 1
    if cube.cube_edges[4][3] == "w": count += 1
    if num == 2 and cube.cube_edges[4][0] != "w":
        return False
    return count >= num


def check_top_corners(cube: Cube) -> bool:
    count = 0
    if cube.cube_corners[4][0] == "w": count += 1
    if cube.cube_corners[4][1] == "w": count += 1
    if cube.cube_corners[4][2] == "w": count += 1
    if cube.cube_corners[4][3] == "w": count += 1
    return count == 4


def check_pll(cube: Cube) -> bool:
    count = 0
    if cube.cube_corners[0][0] == cube.cube_corners[0][1] and cube.cube_edges[0][0] == cube.cube_corners[0][1]: count += 1
    if cube.cube_corners[1][0] == cube.cube_corners[1][1] and cube.cube_edges[1][0] == cube.cube_corners[1][1]: count += 1
    if cube.cube_corners[3][0] == cube.cube_corners[3][1] and cube.cube_edges[3][0] == cube.cube_corners[3][1]: count += 1
    if cube.cube_corners[2][2] == cube.cube_corners[2][3] and cube.cube_edges[2][2] == cube.cube_corners[2][3]: count += 1
    return count == 4


def check_auf(cube: Cube) -> bool:
    return cube.cube_edges[0][0] == "g"


def check_state(cube: Cube, state: int) -> bool:
    # Direct port of your switch(state)
    if state == 0:  return check_bottom_edges(cube, 1)
    if state == 1:  return check_bottom_edges(cube, 2)
    if state == 2:  return check_bottom_edges(cube, 3)
    if state == 3:  return check_bottom_edges(cube, 4)

    if state == 4:  return check_bottom_edges(cube, 4) and corner_in_top(cube)
    if state == 5:  return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 1)
    if state == 6:  return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 1) and corner_in_top(cube)
    if state == 7:  return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 2)
    if state == 8:  return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 2) and corner_in_top(cube)
    if state == 9:  return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3)
    if state == 10: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and corner_in_top(cube)
    if state == 11: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4)

    if state == 12: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and edge_in_top(cube)
    if state == 13: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and edge_in_top(cube)
    if state == 14: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and corner_edge_pair(cube)
    if state == 15: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 1)
    if state == 16: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and edge_in_top(cube) and check_middle_edges(cube, 1)
    if state == 17: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and edge_in_top(cube) and check_middle_edges(cube, 1)
    if state == 18: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and corner_edge_pair(cube) and check_middle_edges(cube, 1)

    if state == 19: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 2)
    if state == 20: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and edge_in_top(cube) and check_middle_edges(cube, 2)
    if state == 21: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and edge_in_top(cube) and check_middle_edges(cube, 2)
    if state == 22: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and corner_edge_pair(cube) and check_middle_edges(cube, 2)

    if state == 23: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 3)
    if state == 24: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and edge_in_top(cube) and check_middle_edges(cube, 3)
    if state == 25: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and edge_in_top(cube) and check_middle_edges(cube, 3)
    if state == 26: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 3) and corner_edge_pair(cube) and check_middle_edges(cube, 3)

    if state == 27: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 4)
    if state == 28: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 4) and check_top_edges(cube, 2)
    if state == 29: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 4) and check_top_edges(cube, 4)
    if state == 30: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 4) and check_top_edges(cube, 4) and check_top_corners(cube)
    if state == 31: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 4) and check_top_edges(cube, 4) and check_top_corners(cube) and check_pll(cube)
    if state == 32: return check_bottom_edges(cube, 4) and check_bottom_corners(cube, 4) and check_middle_edges(cube, 4) and check_top_edges(cube, 4) and check_top_corners(cube) and check_pll(cube) and check_auf(cube)
    return False


# ---- IDDFS / DLS (direct port structure) ----
OLL_ALGS_7 = [
    "RUruRUUr",
    "RUUruRur",
    "RUURRuRRuRRUUR",
    "RUrURurURUUr",
    "RRDrUURdrUUr",
    "rFRbrfRB",
    "RURDruRdRR",
]

PLL_ALGS_21 = [
    "rFrBBRfrBBRR",
    "LfLBBlFLBBLL",
    "rufRUrurFRRuruRUrUR",
    "RRUrUruRuRRuDrURd",
    "ruRUdRRUrURuRuRRD",
    "RRuRuRUrURRUdRurD",
    "RUruDRRuRurUrURRd",
    "RUrfRUrurFRRur",
    "luLFluLULfLLUL",
    "RuruRURDruRdrUUr",
    "RRFRURurfRUUrUUR",
    "RUrurFRRuruRUrf",
    "FRRDruRdrUUrurfRURur",
    "RUrURUrfRUrurFRRurUURur",
    "rURurfuFRUrFrfRuR",
    "RuRUrDRdRuDRRURRdRR",
    "FRuruRUrfRUrurFRf",
    "RRUURUURRUURRUURUURR",
    "RuRURURuruRR",
    "RRURUrururUr",
    "ruRuRURurURURRur",
]


def _dls(cube: Cube, path: List[str], depth: int, state: int) -> Tuple[List[str], bool]:
    if depth == 0:
        # Special: OLL and PLL states try suffix algorithms after current path
        if state == 30:
            prefix = "".join(path)
            for alg in OLL_ALGS_7:
                do_path(cube, prefix + alg)
                if check_state(cube, state):
                    return list(prefix + alg), True
                undo_path(cube, prefix + alg)
            return path, False

        if state == 31:
            prefix = "".join(path)
            for alg in PLL_ALGS_21:
                do_path(cube, prefix + alg)
                if check_state(cube, state):
                    return list(prefix + alg), True
                undo_path(cube, prefix + alg)
            return path, False

        # Normal: test this exact path
        do_path(cube, path)
        if check_state(cube, state):
            return path, True
        undo_path(cube, path)
        return path, False

    # Choose candidate moves based on state (same branching limits as JS)
    size = 12
    if state > 27: size = 6
    if state > 29: size = 2

    choices = ["U", "u", "R", "r", "F", "f", "D", "d", "L", "l", "B", "b"][:size]

    for mv in choices:
        path[depth - 1] = mv
        cand, ok = _dls(cube, path, depth - 1, state)
        if ok:
            return cand, True
    return path, False


def iddfs(cube: Cube, state: int) -> Optional[List[str]]:
    # JS: size=9, if state>=30 size=3
    max_depth_exclusive = 3 if state >= 30 else 9

    for depth in range(1, max_depth_exclusive):
        path = ["U"] * depth  # placeholder
        cand, ok = _dls(cube, path, depth, state)
        if ok:
            return cand[:]  # list of move chars
    return None


def solve_edges(cube: Cube, num: int) -> None:
    if not edge_in_top(cube):
        iddfs(cube, num - 3)
        iddfs(cube, num - 2)
    iddfs(cube, num - 1)
    iddfs(cube, num)


def solver(cube: Cube) -> List[List[str]]:
    solution: List[List[str]] = []

    # First chunk: states 0..11
    for i in range(12):
        if check_state(cube, i):
            continue
        p = iddfs(cube, i)
        if p is None:
            raise RuntimeError(f"Invalid cube at state {i}")
        do_path(cube, p)
        solution.append(p)

    # Middle edges chunk: states 15..27 step 4 (as in your JS)
    for i in range(15, 28, 4):
        if check_state(cube, i):
            continue
        solve_edges(cube, i)

    # Last layer chunk: states 28..32
    for i in range(28, 33):
        if check_state(cube, i):
            continue
        p = iddfs(cube, i)
        if p is None:
            raise RuntimeError(f"Invalid cube at state {i}")
        do_path(cube, p)
        solution.append(p)

    return solution


# ---- ML-friendly utilities ----
COLOR_TO_INT = {"g": 0, "r": 1, "b": 2, "o": 3, "w": 4, "y": 5}

def cube_to_vec48(cube: Cube) -> List[int]:
    v: List[int] = []
    for f in range(6):
        for k in range(4):
            v.append(COLOR_TO_INT[cube.cube_edges[f][k]])
    for f in range(6):
        for k in range(4):
            v.append(COLOR_TO_INT[cube.cube_corners[f][k]])
    return v  # length 48


# ---- example usage ----
if __name__ == "__main__":
    c = Cube.solved()
    scramble = "RUruFDLBUlfrbu"
    do_path(c, scramble)
    sol = solver(c)
    print("Solution segments:", ["".join(s) for s in sol])
