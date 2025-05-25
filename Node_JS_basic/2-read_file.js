/*eslint-disable*/
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8').split('\n');
    const students = data.filter(line => line.trim() !== '' && !line.startsWith('firstname'));

    const fields = {};

    for (const student of students) {
      const parts = student.split(',');
      const firstName = parts[0];
      const field = parts[3];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    }

    console.log(`Number of students: ${students.length}`);
    for (const field in fields) {
      console.log(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;