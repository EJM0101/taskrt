from flask import Flask, render_template, request
from utils.scheduler import simulate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        names = request.form.getlist("name")
        executions = request.form.getlist("execution")
        periods = request.form.getlist("period")
        deadlines = request.form.getlist("deadline")
        algorithm = request.form.get("algorithm")

        tasks = []
        for i in range(len(names)):
            task = {
                'name': names[i],
                'execution': int(executions[i]),
                'period': int(periods[i]),
                'deadline': int(deadlines[i]) if deadlines[i] else int(periods[i])
            }
            tasks.append(task)

        schedule, utilization = simulate(tasks, algorithm)
        feasible = utilization <= 1.0

        return render_template("result.html",
                               schedule=schedule,
                               utilization=utilization,
                               feasible=feasible,
                               algorithm=algorithm)

    return render_template("index.html")