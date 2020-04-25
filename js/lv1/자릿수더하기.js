function solution(n) {
  if (n < 10) {
    return n;
  }
  return (n % 10) + solution(Math.floor(n / 10));
}

N = [123, 987];
answer = [6, 24];

for (let i = 0; i < N.length; i++) {
  if (solution(N[i]) == answer[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}

// function solution(n) {
//   return (n + "")
//     .split("")
//     .reduce((acc, curr) => acc + parseInt(curr), 0);
// }
