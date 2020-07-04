#!flask/bin/python
from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'vers': u'Devant l\'éclair - Sublime est celui _ Qui ne sait rien !',
        'auteur': u'Basho',
        'description': u'Un premier vers', 
        'done': False
    },
    {
        'id': 2,
        'vers': u'Sous la pluie d\'été - Raccourcissent - Les pattes du héron.',
        'auteur': u'Basho',
        'description': u'un second vers', 
        'done': False
    }
]

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)