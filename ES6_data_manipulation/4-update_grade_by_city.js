export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeRecord = newGrades.find((g) => g.studentId === student.id);
      return {
        ...student,
        grade: gradeRecord ? gradeRecord.grade : 'N/A',
      };
    });
}
