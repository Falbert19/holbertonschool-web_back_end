/*eslint-disable*/
process.stdout.write('Welcome to Holberton School, what is your name?\r');

process.stdin.on('data', (data) => {
  const input = data.toString().trim();
  process.stdout.write(`Your name is: ${input}\r`);
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\r');
});