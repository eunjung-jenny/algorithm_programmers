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
    days.slice(0, a - 1).reduce((a, b) => a + b, 0) + b - 1;
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

// function getDayName(a,b){
//   var arr = ['SUN','MON','TUE','WED','THU','FRI','SAT'];
//   var date = new Date(`2016-${a}-${b}`);
// var day = date.getDay()
//   return arr[day];
// }

// function getDayName(a,b){
//   var date = new Date(2016, (a - 1), b);
//     return date.toString().slice(0, 3).toUpperCase();
// }
