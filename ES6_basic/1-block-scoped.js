/**
 * Ensures block-scoped variables are not overwritten.
 * @param {boolean} trueOrFalse - Condition to execute the block.
 * @return {boolean[]} The values of task and task2.
 */
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    console.log('Inside block scope');
  }

  return [task, task2];
}
