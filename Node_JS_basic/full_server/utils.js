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
      if (lines.length < 2) {
        // No valid students
        resolve({});
        return;
      }

      const fields = {};
      const header = lines[0].split(',');
      const fieldIndex = header.indexOf('field');
      const nameIndex = header.indexOf('firstname');

      for (const line of lines.slice(1)) {
        const parts = line.split(',');
        if (parts.length <= Math.max(fieldIndex, nameIndex)) continue;

        const firstName = parts[nameIndex];
        const field = parts[fieldIndex];

        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }

      resolve(fields);
    });
  });
}