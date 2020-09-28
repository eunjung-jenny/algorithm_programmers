function solution(numbers) {
  const answerSet = new Set();

  for (let i = 0; i < numbers.length; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      answerSet.add(numbers[i] + numbers[j]);
    }
  }

  return Array.from(answerSet).sort((a, b) => a - b);
}

const numbers = [
  [2, 1, 3, 4, 1],
  [5, 0, 2, 7],
];

const result = [
  [2, 3, 4, 5, 6, 7],
  [2, 5, 7, 9, 12],
];

for (let i = 0; i < numbers.length; i++) {
  console.log(solution(numbers[i]));
}
