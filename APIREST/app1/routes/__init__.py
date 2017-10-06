from app import app
from app.stream import iniciaCaptura
from app.cronometro import cronoFutPlay
import datetime
import time
from app import jsonify

@app.route('/')
def index():
    return "sillas flask"

@app.route('/start')
def startCrono():
    i =0
    i += 1
    tempo_atual = datetime.timedelta(seconds=i)
    a = str(tempo_atual)


    cronoFutPlay.comecar()




@app.route('/gol')
def gol():
    return 'GOL'

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]
    return jsonify({'tasks': tasks})
