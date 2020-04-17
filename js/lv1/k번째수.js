function solution(array, commands) {
  let answer = [];
  for (const sub_arr of commands) {
    const n_arr = array.slice(sub_arr[0] - 1, sub_arr[1]);
    const sort_arr = n_arr.sort();
    const target = sort_arr[sub_arr[2] - 1];
    answer.push(target);
  }
  return answer;
}

array = [1, 5, 2, 6, 3, 7, 4];
commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];

solution(array, commands);

// return = [5, 6, 3]
