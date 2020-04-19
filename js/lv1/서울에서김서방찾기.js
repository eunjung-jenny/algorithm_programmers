function solution(seoul) {
  return `김서방은 ${seoul.findIndex(
    (elem) => elem == "Kim"
  )}에 있다`;
}

seoul = ["Jane", "Kim"];
// result = "김서방은 1에 있다"

function solution(seoul) {
  return `김서방은 ${seoul.indexOf("Kim")}에 있다`;
}
