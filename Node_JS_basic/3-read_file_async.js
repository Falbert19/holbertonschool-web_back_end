/*eslint-disable*/
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter(line => line.trim() !== '');
      const students = lines.slice(1); // skip header
      const fields = {};

      for (const student of students) {
        const parts = student.split(',');
        if (parts.length < 4) continue; // skip invalid line

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

      resolve();
    });
  });
}

module.exports = countStudents;
