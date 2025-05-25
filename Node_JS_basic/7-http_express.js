/*eslint-disable*/
const express = require('express');
const countStudents = require('./3-read_file_async');
const e = require('express');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async(req, res) => {
    let response = 'This is the list of our students\n';
    try {
        const data = await countStudents(database);
       response += `\n${data}`;
       res.set('Content-Type', 'text/plain');
       res.send(response);
    } catch (err) {
        response += `\n${err.message}`;
        res.set('Content-Type', 'text/plain');
        res.send(response);
    }
});

app.listen(1245);

module.exports = app;