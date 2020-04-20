function solution(arr1, arr2) {
  let answer = [];
  for (let i = 0; i < arr1.length; i++) {
    let arr = [];
    for (let j = 0; j < arr1[0].length; j++) {
      const num = arr1[i][j] + arr2[i][j];
      arr.push(num);
    }
    answer.push(arr);
  }
  return answer;
}

// arr1 = [[[1,2],[2,3]], [[1],[2]]]
// arr2 = [[[3,4],[5,6]], [[3],[4]]]
// for (let i=0; i<2; i++){
//     solution(arr1[i], arr2[i])
// }

// return = [[[4,6],[7,9]], [[4],[6]]]
