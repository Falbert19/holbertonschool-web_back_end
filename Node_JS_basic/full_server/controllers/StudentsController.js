/*eslint-disable*/
import { readDatabase } from '../utils.js';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const filePath = process.argv[2];
      const fields = await readDatabase(filePath);
      let response = 'This is the list of our students';

      const sortedFields = Object.keys(fields).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
      for (const field of sortedFields) {
        const list = fields[field];
        response += `\nNumber of students in ${field}: ${list.length}. List: ${list.join(', ')}`;
      }

      res.status(200).send(response);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const major = req.params.major;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const filePath = process.argv[2];
      const fields = await readDatabase(filePath);
      const list = fields[major] || [];
      res.status(200).send(`List: ${list.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

export default StudentsController;