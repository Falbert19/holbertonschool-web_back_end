/*eslint-disable*/
class AppController {
    static getHomepage(req, res) {
        res.status(200).send('Hello Holberton School!');
    }
}

export default AppController;