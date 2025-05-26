/*eslint-disable*/
import express form 'express';
import AppController fromm '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

const router = express.Router();

router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;