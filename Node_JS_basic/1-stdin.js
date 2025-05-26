/*eslint-disable*/
process.stdout.write('Welcome to Holberton School, what is your name?\n');

process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Your name is: ${name}`);
});

// Handle end of input (e.g., when piped or Ctrl+D)
process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
