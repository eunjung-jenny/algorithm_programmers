function solution(s) {
  return "*".repeat(s.length - 4) + s.slice(-4);
}

phone_number = ["01033334444", "027778888"];
result = ["*******4444", "*****8888"];

for (let i = 0; i < phone_number.length; i++) {
  if (solution(phone_number[i]) === result[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}
