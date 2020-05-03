function solution(s) {
  return s.split("").sort().reverse().join("");
}

strings = ["Zbcdefg"];
answer = ["gfedcbZ"];

for (let i = 0; i < strings.length; i++) {
  if (solution(strings[i]) == answer[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}
