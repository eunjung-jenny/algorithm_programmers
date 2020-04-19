function solution(a, b) {
  if (a === b) {
    return a;
  } else {
    let sum = 0;
    if (a < b) {
      for (let n = a; n < b + 1; n++) {
        sum += n;
      }
    } else {
      for (let n = b; n < a + 1; n++) {
        sum += n;
      }
    }
    return sum;
  }
}

a = [3, 3, 5];
b = [5, 3, 3];
// result = [12, 3, 12]

for (let i = 0; i < 3; i++) {
  solution(a[i], b[i]);
}

// function solution(a, b, s = 0) {
//   for (var i = Math.min(a, b); i <= Math.max(a, b); i++)
//     s += i;
//   return s;
// }
