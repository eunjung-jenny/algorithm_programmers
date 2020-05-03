function solution(strings, n) {
  strings.sort((a, b) =>
    a[n] !== b[n]
      ? a[n].localeCompare(b[n])
      : a.localeCompare(b)
  );
  return strings;
}

strings = [
  ["sun", "bed", "car"],
  ["abce", "abcd", "cdx"],
];

n = [1, 2];

answer = [
  ["car", "bed", "sun"],
  ["abcd", "abce", "cdx"],
];

for (let i = 0; i < strings.length; i++) {
  if (solution(strings[i], n[i]) === answer[i]) {
    console.log(`${i + 1}: pass`);
  } else {
    console.log(`${i + 1}: fail`);
  }
}
