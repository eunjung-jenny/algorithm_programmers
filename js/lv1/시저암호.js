function solution(s, n) {
  let answer = "";
  for (let i = 0; i < s.length; i++) {
    const char = s.charAt(i);
    if (char === " ") {
      answer += " ";
    } else {
      let ascii = char.charCodeAt(0) + n;
      const isUpperCase = char.toUpperCase() === char;
      if (isUpperCase) {
        if (ascii > "Z".charCodeAt(0)) {
          ascii = ascii - 26;
        }
      } else {
        if (ascii > "z".charCodeAt(0)) {
          ascii = ascii - 26;
        }
      }
      answer += String.fromCharCode(ascii);
    }
  }
  return answer;
}

s = ["AB", "z", "a B z", "AaZz"];
n = [1, 1, 4, 25];
result = ["BC", "a", "e F d", "ZzYy"];

for (let i = 0; i < s.length; i++) {
  if (solution(s[i], n[i]) == result[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}
