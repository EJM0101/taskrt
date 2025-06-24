import os
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


# Lancement correct local + Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render fournit PORT sinon 5000 en local
    app.run(host="0.0.0.0", port=port)