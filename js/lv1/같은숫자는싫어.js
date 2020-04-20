function solution(arr) {
  let answer = [arr[0]];
  arr.slice(1).forEach((num) => {
    if (answer[answer.length - 1] !== num) {
      answer.push(num);
    }
  });
  return answer;
}

// function solution(arr) {
//   return arr.filter((val, index) => val != arr[index + 1]);
// }
