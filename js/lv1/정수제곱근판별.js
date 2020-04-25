function solution(n) {
  const sqrt_n = parseInt(n ** (1 / 2));
  return n === sqrt_n ** 2 ? (sqrt_n + 1) ** 2 : -1;
}

N = [121, 3];
answer = [144, -1];

for (let i = 0; i < N.length; i++) {
  if (solution(N[i]) == answer[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}

// function nextSqaure(n) {
//   var result = 0;
//   var n = Math.sqrt(n);
//   result = Number.isInteger(n) ? Math.pow(n + 1, 2) : "no";
//   return result;
// }
