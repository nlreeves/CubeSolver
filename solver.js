// cube setup
export default class Cube {
  cubeEdges = [6];
  cubeCorners = [6];
  constructor(arrayEdges, arrayCorners) {
    for (let i = 0; i < 6; i++) this.cubeEdges[i] = arrayEdges[i];
    for (let i = 0; i < 6; i++) this.cubeCorners[i] = arrayCorners[i];
  }

  right() {
    this.cubeEdges[1].unshift(this.cubeEdges[1].pop());
    this.cubeCorners[1].unshift(this.cubeCorners[1].pop());

    let temp = this.cubeEdges[0][1];
    this.cubeEdges[0][1] = this.cubeEdges[5][1];
    this.cubeEdges[5][1] = this.cubeEdges[2][1];
    this.cubeEdges[2][1] = this.cubeEdges[4][1];
    this.cubeEdges[4][1] = temp;

    temp = this.cubeCorners[0][1];
    let temp2 = this.cubeCorners[0][2];
    this.cubeCorners[0][1] = this.cubeCorners[5][1];
    this.cubeCorners[0][2] = this.cubeCorners[5][2];
    this.cubeCorners[5][1] = this.cubeCorners[2][1];
    this.cubeCorners[5][2] = this.cubeCorners[2][2];
    this.cubeCorners[2][1] = this.cubeCorners[4][1];
    this.cubeCorners[2][2] = this.cubeCorners[4][2];
    this.cubeCorners[4][1] = temp;
    this.cubeCorners[4][2] = temp2;
  }

  rightPrime() {
    this.right();
    this.right();
    this.right();
  }

  left() {
    this.cubeEdges[3].unshift(this.cubeEdges[3].pop());
    this.cubeCorners[3].unshift(this.cubeCorners[3].pop());

    let temp = this.cubeEdges[0][3];
    this.cubeEdges[0][3] = this.cubeEdges[4][3];
    this.cubeEdges[4][3] = this.cubeEdges[2][3];
    this.cubeEdges[2][3] = this.cubeEdges[5][3];
    this.cubeEdges[5][3] = temp;

    temp = this.cubeCorners[0][0];
    let temp2 = this.cubeCorners[0][3];
    this.cubeCorners[0][0] = this.cubeCorners[4][0];
    this.cubeCorners[0][3] = this.cubeCorners[4][3];
    this.cubeCorners[4][0] = this.cubeCorners[2][0];
    this.cubeCorners[4][3] = this.cubeCorners[2][3];
    this.cubeCorners[2][0] = this.cubeCorners[5][0];
    this.cubeCorners[2][3] = this.cubeCorners[5][3];
    this.cubeCorners[5][0] = temp;
    this.cubeCorners[5][3] = temp2;
  }

  leftPrime() {
    this.left();
    this.left();
    this.left();
  }

  up() {
    this.cubeEdges[4].unshift(this.cubeEdges[4].pop());
    this.cubeCorners[4].unshift(this.cubeCorners[4].pop());

    let temp = this.cubeEdges[0][0];
    this.cubeEdges[0][0] = this.cubeEdges[1][0];
    this.cubeEdges[1][0] = this.cubeEdges[2][2];
    this.cubeEdges[2][2] = this.cubeEdges[3][0];
    this.cubeEdges[3][0] = temp;

    temp = this.cubeCorners[0][0];
    let temp2 = this.cubeCorners[0][1];
    this.cubeCorners[0][0] = this.cubeCorners[1][0];
    this.cubeCorners[0][1] = this.cubeCorners[1][1];
    this.cubeCorners[1][0] = this.cubeCorners[2][2];
    this.cubeCorners[1][1] = this.cubeCorners[2][3];
    this.cubeCorners[2][2] = this.cubeCorners[3][0];
    this.cubeCorners[2][3] = this.cubeCorners[3][1];
    this.cubeCorners[3][0] = temp;
    this.cubeCorners[3][1] = temp2;
  }

  upPrime() {
    this.up();
    this.up();
    this.up();
  }

  down() {
    this.cubeEdges[5].unshift(this.cubeEdges[5].pop());
    this.cubeCorners[5].unshift(this.cubeCorners[5].pop());

    let temp = this.cubeEdges[0][2];
    this.cubeEdges[0][2] = this.cubeEdges[3][2];
    this.cubeEdges[3][2] = this.cubeEdges[2][0];
    this.cubeEdges[2][0] = this.cubeEdges[1][2];
    this.cubeEdges[1][2] = temp;

    temp = this.cubeCorners[0][2];
    let temp2 = this.cubeCorners[0][3];
    this.cubeCorners[0][2] = this.cubeCorners[3][2];
    this.cubeCorners[0][3] = this.cubeCorners[3][3];
    this.cubeCorners[3][2] = this.cubeCorners[2][0];
    this.cubeCorners[3][3] = this.cubeCorners[2][1];
    this.cubeCorners[2][0] = this.cubeCorners[1][2];
    this.cubeCorners[2][1] = this.cubeCorners[1][3];
    this.cubeCorners[1][2] = temp;
    this.cubeCorners[1][3] = temp2;
  }

  downPrime() {
    this.down();
    this.down();
    this.down();
  }

  front() {
    this.cubeEdges[0].unshift(this.cubeEdges[0].pop());
    this.cubeCorners[0].unshift(this.cubeCorners[0].pop());

    let temp = this.cubeEdges[4][2];
    this.cubeEdges[4][2] = this.cubeEdges[3][1];
    this.cubeEdges[3][1] = this.cubeEdges[5][0];
    this.cubeEdges[5][0] = this.cubeEdges[1][3];
    this.cubeEdges[1][3] = temp;

    temp = this.cubeCorners[4][3];
    let temp2 = this.cubeCorners[4][2];
    this.cubeCorners[4][2] = this.cubeCorners[3][1];
    this.cubeCorners[4][3] = this.cubeCorners[3][2];
    this.cubeCorners[3][1] = this.cubeCorners[5][0];
    this.cubeCorners[3][2] = this.cubeCorners[5][1];
    this.cubeCorners[5][0] = this.cubeCorners[1][3];
    this.cubeCorners[5][1] = this.cubeCorners[1][0];
    this.cubeCorners[1][0] = temp;
    this.cubeCorners[1][3] = temp2;
  }

  frontPrime() {
    this.front();
    this.front();
    this.front();
  }

  back() {
    this.cubeEdges[2].unshift(this.cubeEdges[2].pop());
    this.cubeCorners[2].unshift(this.cubeCorners[2].pop());

    let temp = this.cubeEdges[4][0];
    this.cubeEdges[4][0] = this.cubeEdges[1][1];
    this.cubeEdges[1][1] = this.cubeEdges[5][2];
    this.cubeEdges[5][2] = this.cubeEdges[3][3];
    this.cubeEdges[3][3] = temp;

    temp = this.cubeCorners[4][0];
    let temp2 = this.cubeCorners[4][1];
    this.cubeCorners[4][0] = this.cubeCorners[1][1];
    this.cubeCorners[4][1] = this.cubeCorners[1][2];
    this.cubeCorners[1][1] = this.cubeCorners[5][2];
    this.cubeCorners[1][2] = this.cubeCorners[5][3];
    this.cubeCorners[5][2] = this.cubeCorners[3][3];
    this.cubeCorners[5][3] = this.cubeCorners[3][0];
    this.cubeCorners[3][3] = temp;
    this.cubeCorners[3][0] = temp2;
  }

  backPrime() {
    this.back();
    this.back();
    this.back();
  }
}

function makeCube() {
  let arrayEdges = [6];
  let arrayCorners = [6];
  arrayCorners[0] = ["g", "g", "g", "g"];
  arrayCorners[1] = ["r", "r", "r", "r"];
  arrayCorners[2] = ["b", "b", "b", "b"];
  arrayCorners[3] = ["o", "o", "o", "o"];
  arrayCorners[4] = ["w", "w", "w", "w"];
  arrayCorners[5] = ["y", "y", "y", "y"];

  arrayEdges[0] = ["g", "g", "g", "g"];
  arrayEdges[1] = ["r", "r", "r", "r"];
  arrayEdges[2] = ["b", "b", "b", "b"];
  arrayEdges[3] = ["o", "o", "o", "o"];
  arrayEdges[4] = ["w", "w", "w", "w"];
  arrayEdges[5] = ["y", "y", "y", "y"];
  return new Cube(arrayEdges, arrayCorners);
}
// do path
function doPath(cube, path, state) {
  let size = path.length;
  for (let i = 0; i < size; i++) {
    switch (path[i]) {
      case "R":
        cube.right();
        break;
      case "r":
        cube.rightPrime();
        break;
      case "L":
        cube.left();
        break;
      case "l":
        cube.leftPrime();
        break;
      case "U":
        cube.up();
        break;
      case "u":
        cube.upPrime();
        break;
      case "D":
        cube.down();
        break;
      case "d":
        cube.downPrime();
        break;
      case "F":
        cube.front();
        break;
      case "f":
        cube.frontPrime();
        break;
      case "B":
        cube.back();
        break;
      case "b":
        cube.backPrime();
        break;
      default:
        return;
    }
  }
}
// undo path
function undoPath(cube, path, state) {
  let size = path.length;
  for (let i = size - 1; i >= 0; i--) {
    switch (path[i]) {
      case "R":
        cube.rightPrime();
        break;
      case "r":
        cube.right();
        break;
      case "L":
        cube.leftPrime();
        break;
      case "l":
        cube.left();
        break;
      case "U":
        cube.upPrime();
        break;
      case "u":
        cube.up();
        break;
      case "D":
        cube.downPrime();
        break;
      case "d":
        cube.down();
        break;
      case "F":
        cube.frontPrime();
        break;
      case "f":
        cube.front();
        break;
      case "B":
        cube.backPrime();
        break;
      case "b":
        cube.back();
        break;
      default:
        return;
    }
  }
}

function checkBottomEdges(cube, num) {
  let count = 0;
  if (cube.cubeEdges[0][2] === "g" && cube.cubeEdges[5][0] === "y") count++;
  if (cube.cubeEdges[1][2] === "r" && cube.cubeEdges[5][1] === "y") count++;
  if (cube.cubeEdges[3][2] === "o" && cube.cubeEdges[5][3] === "y") count++;
  if (cube.cubeEdges[2][0] === "b" && cube.cubeEdges[5][2] === "y") count++;

  return num <= count;
}

function checkBottomCorners(cube, num) {
  let count = 0;
  if (
    cube.cubeCorners[1][2] === "r" &&
    cube.cubeCorners[5][2] === "y" &&
    cube.cubeCorners[2][1] === "b"
  )
    count++;
  if (
    cube.cubeCorners[3][3] === "o" &&
    cube.cubeCorners[5][3] === "y" &&
    cube.cubeCorners[2][0] === "b"
  )
    count++;
  if (
    cube.cubeCorners[0][3] === "g" &&
    cube.cubeCorners[5][0] === "y" &&
    cube.cubeCorners[3][2] === "o"
  )
    count++;
  if (
    cube.cubeCorners[0][2] === "g" &&
    cube.cubeCorners[5][1] === "y" &&
    cube.cubeCorners[1][3] === "r"
  )
    count++;

  return num <= count;
}

function checkMiddleEdges(cube, num) {
  let count = 0;
  if (
    cube.cubeEdges[2][1] === "b" &&
    cube.cubeEdges[1][1] === "r" &&
    cube.cubeCorners[5][2] === "y" &&
    cube.cubeCorners[1][2] === "r" &&
    cube.cubeCorners[2][1] === "b"
  )
    count++;
  if (
    cube.cubeEdges[2][3] === "b" &&
    cube.cubeEdges[3][3] === "o" &&
    cube.cubeCorners[5][3] === "y" &&
    cube.cubeCorners[3][3] === "o" &&
    cube.cubeCorners[2][0] === "b"
  )
    count++;
  if (
    cube.cubeEdges[0][1] === "g" &&
    cube.cubeEdges[1][3] === "r" &&
    cube.cubeCorners[5][1] === "y" &&
    cube.cubeCorners[1][3] === "r" &&
    cube.cubeCorners[0][2] === "g"
  )
    count++;
  if (
    cube.cubeEdges[0][3] === "g" &&
    cube.cubeEdges[3][1] === "o" &&
    cube.cubeCorners[5][0] === "y" &&
    cube.cubeCorners[3][2] === "o" &&
    cube.cubeCorners[0][3] === "g"
  )
    count++;

  return num <= count;
}

function cornerInTop(cube) {
  if (cube.cubeCorners[0][0] === "y" || cube.cubeCorners[0][1] === "y")
    return true;
  if (cube.cubeCorners[1][0] === "y" || cube.cubeCorners[1][1] === "y")
    return true;
  if (cube.cubeCorners[2][2] === "y" || cube.cubeCorners[2][3] === "y")
    return true;
  if (cube.cubeCorners[3][0] === "y" || cube.cubeCorners[3][1] === "y")
    return true;

  return false;
}

function edgeInTop(cube) {
  if (
    (cube.cubeEdges[0][0] !== "w" && cube.cubeEdges[4][2] !== "w") ||
    (cube.cubeEdges[3][0] !== "w" && cube.cubeEdges[4][3] !== "w") ||
    (cube.cubeEdges[1][0] !== "w" && cube.cubeEdges[4][1] !== "w") ||
    (cube.cubeEdges[2][2] !== "w" && cube.cubeEdges[4][0] !== "w")
  )
    return true;
  return false;
}

function cornerEdgePair(cube) {
  if (
    cube.cubeCorners[0][0] === "y" &&
    cube.cubeCorners[4][3] === cube.cubeEdges[4][3] &&
    cube.cubeCorners[3][1] === cube.cubeEdges[3][0]
  )
    return true;
  if (
    cube.cubeCorners[0][1] === "y" &&
    cube.cubeCorners[4][2] === cube.cubeEdges[4][1] &&
    cube.cubeCorners[1][0] === cube.cubeEdges[1][0]
  )
    return true;
  if (
    cube.cubeCorners[3][1] === "y" &&
    cube.cubeCorners[4][3] === cube.cubeEdges[4][2] &&
    cube.cubeCorners[0][0] === cube.cubeEdges[0][0]
  )
    return true;
  if (
    cube.cubeCorners[3][0] === "y" &&
    cube.cubeCorners[4][0] === cube.cubeEdges[4][0] &&
    cube.cubeCorners[2][3] === cube.cubeEdges[2][2]
  )
    return true;
  if (
    cube.cubeCorners[2][3] === "y" &&
    cube.cubeCorners[4][0] === cube.cubeEdges[4][3] &&
    cube.cubeCorners[3][0] === cube.cubeEdges[3][0]
  )
    return true;
  if (
    cube.cubeCorners[2][2] === "y" &&
    cube.cubeCorners[4][1] === cube.cubeEdges[4][1] &&
    cube.cubeCorners[1][1] === cube.cubeEdges[1][0]
  )
    return true;
  if (
    cube.cubeCorners[1][1] === "y" &&
    cube.cubeCorners[4][1] === cube.cubeEdges[4][0] &&
    cube.cubeCorners[2][2] === cube.cubeEdges[2][2]
  )
    return true;
  if (
    cube.cubeCorners[1][0] === "y" &&
    cube.cubeCorners[4][2] === cube.cubeEdges[4][2] &&
    cube.cubeCorners[0][1] === cube.cubeEdges[0][0]
  )
    return true;
  return false;
}

function checkTopEdges(cube, num) {
  let count = 0;
  if (cube.cubeEdges[4][0] === "w") count++;
  if (cube.cubeEdges[4][1] === "w") count++;
  if (cube.cubeEdges[4][2] === "w") count++;
  if (cube.cubeEdges[4][3] === "w") count++;
  if (num === 2 && cube.cubeEdges[4][0] !== "w") return false;
  return count >= num;
}

function checkTopCorners(cube) {
  let count = 0;
  if (cube.cubeCorners[4][0] === "w") count++;
  if (cube.cubeCorners[4][1] === "w") count++;
  if (cube.cubeCorners[4][2] === "w") count++;
  if (cube.cubeCorners[4][3] === "w") count++;

  return count === 4;
}

function checkPLL(cube) {
  let count = 0;
  if (
    cube.cubeCorners[0][0] === cube.cubeCorners[0][1] &&
    cube.cubeEdges[0][0] === cube.cubeCorners[0][1]
  )
    count++;
  if (
    cube.cubeCorners[1][0] === cube.cubeCorners[1][1] &&
    cube.cubeEdges[1][0] === cube.cubeCorners[1][1]
  )
    count++;
  if (
    cube.cubeCorners[3][0] === cube.cubeCorners[3][1] &&
    cube.cubeEdges[3][0] === cube.cubeCorners[3][1]
  )
    count++;
  if (
    cube.cubeCorners[2][2] === cube.cubeCorners[2][3] &&
    cube.cubeEdges[2][2] === cube.cubeCorners[2][3]
  )
    count++;

  return count === 4;
}

function checkAUF(cube) {
  return cube.cubeEdges[0][0] === "g";
}

function checkState(cube, state) {
  switch (state) {
    case 0:
      return checkBottomEdges(cube, 1);

    case 1:
      return checkBottomEdges(cube, 2);

    case 2:
      return checkBottomEdges(cube, 3);

    case 3:
      return checkBottomEdges(cube, 4);

    case 4:
      return checkBottomEdges(cube, 4) && cornerInTop(cube);

    case 5:
      return checkBottomEdges(cube, 4) && checkBottomCorners(cube, 1);

    case 6:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 1) &&
        cornerInTop(cube)
      );

    case 7:
      return checkBottomEdges(cube, 4) && checkBottomCorners(cube, 2);

    case 8:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 2) &&
        cornerInTop(cube)
      );

    case 9:
      return checkBottomEdges(cube, 4) && checkBottomCorners(cube, 3);

    case 10:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        cornerInTop(cube)
      );

    case 11:
      return checkBottomEdges(cube, 4) && checkBottomCorners(cube, 4);

    case 12:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        edgeInTop(cube)
      );

    case 13:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        edgeInTop(cube)
      );

    case 14:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        cornerEdgePair(cube)
      );

    case 15:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 1)
      );

    case 16:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        edgeInTop(cube) &&
        checkMiddleEdges(cube, 1)
      );

    case 17:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        edgeInTop(cube) &&
        checkMiddleEdges(cube, 1)
      );

    case 18:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        cornerEdgePair(cube) &&
        checkMiddleEdges(cube, 1)
      );

    case 19:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 2)
      );

    case 20:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        edgeInTop(cube) &&
        checkMiddleEdges(cube, 2)
      );

    case 21:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        edgeInTop(cube) &&
        checkMiddleEdges(cube, 2)
      );

    case 22:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        cornerEdgePair(cube) &&
        checkMiddleEdges(cube, 2)
      );
    case 23:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 3)
      );
    case 24:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        edgeInTop(cube) &&
        checkMiddleEdges(cube, 3)
      );
    case 25:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        edgeInTop(cube) &&
        checkMiddleEdges(cube, 3)
      );
    case 26:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 3) &&
        cornerEdgePair(cube) &&
        checkMiddleEdges(cube, 3)
      );

    case 27:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 4)
      );

    case 28:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 4) &&
        checkTopEdges(cube, 2)
      );

    case 29:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 4) &&
        checkTopEdges(cube, 4)
      );

    case 30:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 4) &&
        checkTopEdges(cube, 4) &&
        checkTopCorners(cube)
      );

    case 31:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 4) &&
        checkTopEdges(cube, 4) &&
        checkTopCorners(cube) &&
        checkPLL(cube)
      );

    case 32:
      return (
        checkBottomEdges(cube, 4) &&
        checkBottomCorners(cube, 4) &&
        checkMiddleEdges(cube, 4) &&
        checkTopEdges(cube, 4) &&
        checkTopCorners(cube) &&
        checkPLL(cube) &&
        checkAUF(cube)
      );
    default:
      return;
  }
}

function iddfs(cube, state) {
  console.log(state);
  let size = 9;
  if (state >= 30) size = 3;
  for (let depth = 1; depth < size; depth++) {
    let p = [[depth], false];
    path = dls(cube, p, depth, state);
    if (path[1]) {
      for (let i = 0; i < path[0].length; i++) {
        let g = path[0][i];
        process.stdout.write(
          !(g === g.toUpperCase()) ? g.toUpperCase() + "' " : g + " "
        );
      }
      console.log();
      return path[0];
    }
  }
  if (!path[1]) console.log("Invalid cube at state " + state);

  return null;
}

function dls(cube, path, depth, state) {
  if (depth === 0) {
    if (state === 30) {
      let algs = [
        "RUruRUUr",
        "RUUruRur",
        "RUURRuRRuRRUUR",
        "RUrURurURUUr",
        "RRDrUURdrUUr",
        "rFRbrfRB",
        "RURDruRdRR",
      ];
      for (let i = 0; i < 7; i++) {
        let temp = path[0].join("");
        doPath(cube, temp + algs[i], state);
        if (checkState(cube, state)) {
          // console.log(path[0]);
          return [(path[0].join("") + algs[i]).split(""), true];
        } else undoPath(cube, temp + algs[i], state);
      }
      return [path[0], false];
    }

    if (state === 31) {
      let algs = [
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
      ];
      for (let i = 0; i < 21; i++) {
        let temp = path[0].join("");
        doPath(cube, temp + algs[i], state);
        // console.log(path[0].join("") + algs[i]);
        if (checkState(cube, state)) {
          return [(path[0].join("") + algs[i]).split(""), true];
        } else undoPath(cube, temp + algs[i], state);
      }
      return [path[0], false];
    }

    doPath(cube, path[0], state);
    if (checkState(cube, state)) {
      // console.log(path[0]);
      return [path[0], true];
    } else {
      undoPath(cube, path[0], state);
      return [path[0], false];
    }
  } else {
    let size = 12;
    if (state > 27) size = 6;
    if (state > 29) size = 2;
    for (let i = 0; i < size; i++) {
      switch (i) {
        case 0:
          path[0][depth - 1] = "U";
          break;
        case 1:
          path[0][depth - 1] = "u";
          break;
        case 2:
          path[0][depth - 1] = "R";
          break;
        case 3:
          path[0][depth - 1] = "r";
          break;
        case 4:
          path[0][depth - 1] = "F";
          break;
        case 5:
          path[0][depth - 1] = "f";
          break;
        case 6:
          path[0][depth - 1] = "D";
          break;
        case 7:
          path[0][depth - 1] = "d";
          break;
        case 8:
          path[0][depth - 1] = "L";
          break;
        case 9:
          path[0][depth - 1] = "l";
          break;
        case 10:
          path[0][depth - 1] = "B";
          break;
        case 11:
          path[0][depth - 1] = "b";
          break;
        default:
          return;
      }

      path = dls(cube, path, depth - 1, state);

      if (path[1]) return path;
    }
    return path;
  }
}

function solveEdges(cube, num) {
  if (!edgeInTop(cube)) {
    iddfs(cube, num - 3);
    iddfs(cube, num - 2);
  }
  iddfs(cube, num - 1);
  iddfs(cube, num);
}

function solver(cube) {
  let solution = [];
  for (let i = 0; i < 12; i++) {
    if (checkState(cube, i)) continue;
    if (i > 11 && i < 16) {
      edgeInTop(cube);
      solution.push(iddfs(cube, i));
    }
    solution.push(iddfs(cube, i));
  }
  for (let i = 15; i < 28; i += 4) {
    if (checkState(cube, i)) continue;
    solveEdges(cube, i);
  }
  for (let i = 28; i < 33; i++) {
    if (checkState(cube, i)) continue;
    solution.push(iddfs(cube, i));
  }
}
let cube = makeCube();
let path = "RUruFDLBUlfrbu";
doPath(cube, path, 0);

solver(cube);

// console.log(cube);
