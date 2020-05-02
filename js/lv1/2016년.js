function solution(a, b) {
  const days = [
    31,
    29,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31,
  ];
  const date = [
    "fri",
    "sat",
    "sun",
    "mon",
    "tue",
    "wed",
    "thu",
  ];
  const diff_days =
    days.slice(0, a - 1).reduce((a, b) => a + b) + b - 1;
  return date[diff_days % 7].toUpperCase();
}

const a = [5];
const b = [24];
const answer = ["TUE"];

for (let i = 0; i < a.length; i++) {
  if (solution(a[i], b[i]) == answer[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}
