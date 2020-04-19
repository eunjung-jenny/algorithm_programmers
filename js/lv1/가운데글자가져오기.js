function solution(s) {
  if (s.length % 2 === 0) {
    return s.slice(s.length / 2 - 1, s.length / 2 + 1);
  } else {
    return s[parseInt(s.length / 2)];
  }
}

s = ["abcde", "qwer"];
// result = ["c", "we"]

for (let i = 0; i < 2; i++) {
  solution(s[i]);
}

// function solution(s) {
//     return s.length % 2 == 0 ? s.substr(s.length / 2 - 1, 2) : s.substr(Math.floor(s.length / 2), 1);
// }
