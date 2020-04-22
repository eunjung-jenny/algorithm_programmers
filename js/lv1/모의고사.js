function solution(answers) {
  let answer = [];

  const p1 = [1, 2, 3, 4, 5];
  const p2 = [2, 1, 2, 3, 2, 4, 2, 5];
  const p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

  let scores = new Array(3).fill(0, 0, 3);
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === p1[i % p1.length]) {
      scores[0] += 1;
    }
    if (answers[i] === p2[i % p2.length]) {
      scores[1] += 1;
    }
    if (answers[i] === p3[i % p3.length]) {
      scores[2] += 1;
    }
  }

  const max_score = Math.max(...scores);
  for (let i = 0; i < 3; i++) {
    if (max_score === scores[i]) {
      answer.push(i + 1);
    }
  }
  //   console.log(answer);
  return answer;
}

// answers1 = [1, 2, 3, 4, 5];
// answers2 = [1, 3, 2, 4, 2];
// solution(answers1);
// solution(answers2);

// function solution(answers) {
//     var answer = [];
//     var a1 = [1, 2, 3, 4, 5];
//     var a2 = [2, 1, 2, 3, 2, 4, 2, 5]
//     var a3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

//     var a1c = answers.filter((a,i)=> a === a1[i%a1.length]).length;
//     var a2c = answers.filter((a,i)=> a === a2[i%a2.length]).length;
//     var a3c = answers.filter((a,i)=> a === a3[i%a3.length]).length;
//     var max = Math.max(a1c,a2c,a3c);

//     if (a1c === max) {answer.push(1)};
//     if (a2c === max) {answer.push(2)};
//     if (a3c === max) {answer.push(3)};

//     return answer;
// }
