from flask import Flask, render_template, request
from utils.scheduler import simulate
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Utilisation du port fourni par Render
    app.run(host="0.0.0.0", port=port)  # Démarrage du serveur sur 0.0.0.0 et port dynamique