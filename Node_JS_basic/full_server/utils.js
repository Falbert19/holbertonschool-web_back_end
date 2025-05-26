/*eslint-disable*/
import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter(line => line.trim() !== '');
      const students = lines.slice(1); // Skip header
      const fields = {};

      for (const line of students) {
        const [first, , , field] = line.split(',');
        if (field) {
          if (!fields[field]) fields[field] = [];
          fields[field].push(first);
        }
      }

      resolve(fields);
    });
  });
}