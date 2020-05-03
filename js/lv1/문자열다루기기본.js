function solution(s) {
  return (
    parseInt(s) == s && (s.length === 4 || s.length === 6)
  );
}

strings = ["a234", "1234", "2e11"];
answer = [false, true, false];

for (let i = 0; i < strings.length; i++) {
  if (solution(strings[i]) == answer[i]) {
    // console.log(`${i + 1}: pass`);
  } else {
    // console.log(`${i + 1}: fail`);
  }
}
