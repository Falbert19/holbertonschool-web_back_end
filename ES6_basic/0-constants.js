/**
 * Returns a task string.
 * @return {string} The task string.
 */
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

/**
 * Returns a fixed string.
 * @return {string} The last part of the sentence.
 */
export function getLast() {
  return ' is okay';
}

/**
 * Returns a sentence with a 
 * @return {string} A sentence using let.
 */
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();
  return combination;
}
