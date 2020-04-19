function solution(n) {
  const i = parseInt(n / 2);
  let answer = null;
  if (n % 2 === 0) {
    answer = "수박".repeat(i);
  } else {
    answer = "수박".repeat(i) + "수";
  }
  return answer;
}

n = [3, 4];

// result = ["수박수", "수박수박"]

// function waterMelon(n){
//     return "수박".repeat(n/2) + ((n%2) ? '수' : '');
// }

// function waterMelon(n){
//     var result = "";
//     for(var i = 0 ; i < n ; i++) {
//         result += i % 2 == 0 ? "수" : "박";
//     }
//     return result;
// }
