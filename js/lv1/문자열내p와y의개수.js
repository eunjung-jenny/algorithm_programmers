function solution(s) {
  const s_lower = s.toLowerCase();

  let num = 0;
  for (let i = 0; i < s.length; i++) {
    if (s_lower[i] === "p") num++;
    if (s_lower[i] === "y") num--;
  }

  const answer = num === 0 ? true : false;

  //   console.log(answer);
  return answer;
}

s1 = "pPoooyY";
answer1 = true;

s2 = "Pyy";
answer2 = false;

solution(s1);
solution(s2);

// function numPY(s){
//       return s.toUpperCase().split("P").length === s.toUpperCase().split("Y").length;
//   }
