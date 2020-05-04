const N = 1000000;
let prime_nums = new Array(N + 1).fill(true);
prime_nums[0] = false;
prime_nums[1] = false;

for (let i = 2; i < parseInt((N + 1) / 2); i++) {
  for (let j = 2 * i; j < N + 1; j = j + i) {
    if (prime_nums[j] == true) {
      prime_nums[j] = false;
    }
  }
}

function solution(n) {
  const range = prime_nums.slice(0, n + 1);
  let answer = 0;
  range.forEach((check) => {
    if (check === true) {
      answer++;
    }
  });
  return answer;
}

n = [10, 5];
result = [4, 3];

for (let i = 0; i < n.length; i++) {
  if (solution(n[i]) === result[i]) {
    console.log(`${i}: pass`);
  } else {
    console.log(`${i}: fail`);
  }
}
