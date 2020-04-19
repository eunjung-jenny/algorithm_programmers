function solution(array, commands) {
  return commands.map(
    (command) =>
      array
        .slice(command[0] - 1, command[1])
        .sort((a, b) => a - b)[command[2] - 1]
  );
}

array = [1, 5, 2, 6, 3, 7, 4];
commands = [
  [2, 5, 3],
  [4, 4, 1],
  [1, 7, 3],
];

solution(array, commands);

// return = [5, 6, 3]
