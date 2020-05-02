function solution(n, lost, reserve) {
  let clothes = new Array(n).fill(1);
  lost.forEach((id) => (clothes[id - 1] -= 1));
  reserve.forEach((id) => (clothes[id - 1] += 1));

  let answer = 0;
  for (let i = 0; i < n; i++) {
    if (clothes[i] === 0) {
      if (i - 1 > 0 && clothes[i - 1] === 2) {
        clothes[i] += 1;
        clothes[i - 1] -= 1;
        answer += 1;
      } else if (i + 1 < n && clothes[i + 1] === 2) {
        clothes[i] += 1;
        clothes[i + 1] -= 1;
        answer += 1;
      }
    } else {
      answer += 1;
    }
  }
  return answer;
}

N = [5, 5, 3];
lost = [[2, 4], [2, 4], [3]];
reserve = [[1, 3, 5], [3], [1]];
answer = [5, 4, 2];

for (let i = 0; i < N.length; i++) {
  if (solution(N[i], lost[i], reserve[i]) == answer[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}
