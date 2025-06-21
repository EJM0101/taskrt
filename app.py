
from flask import Flask, render_template, request
from utils.scheduler import simulate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def run_simulation():
    tasks = []
    for i in range(len(request.form.getlist('name'))):
        task = {
            'name': request.form.getlist('name')[i],
            'execution': int(request.form.getlist('execution')[i]),
            'period': int(request.form.getlist('period')[i]),
            'deadline': int(request.form.getlist('deadline')[i])
        }
        tasks.append(task)

    algo = request.form['algorithm']
    result, utilization = simulate(tasks, algo)
    overload = utilization > 1.0

    return render_template('result.html', tasks=tasks, result=result, utilization=utilization, overload=overload, algo=algo)
