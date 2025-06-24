from math import gcd
from functools import reduce

def simulate(tasks, algorithm):
    hyperperiod = lcm([t['period'] for t in tasks])
    schedule = []
    utilization = sum(t['execution'] / t['period'] for t in tasks)

    for time in range(hyperperiod):
        eligible = []
        for task in tasks:
            if time % task['period'] < task['execution']:
                eligible.append(task)

        if eligible:
            if algorithm == 'EDF':
                eligible.sort(key=lambda t: ((time // t['period'] + 1) * t['period']))
            elif algorithm == 'RM':
                eligible.sort(key=lambda t: t['period'])
            elif algorithm == 'DM':
                eligible.sort(key=lambda t: t['deadline'])
            elif algorithm == 'FIFO':
                pass  # ordre d'arrivée
            task = eligible[0]
            schedule.append({'time': time, 'task': task['name']})
        else:
            schedule.append({'time': time, 'task': 'Idle'})

    return schedule, utilization

def lcm(numbers):
    return reduce(lambda a, b: a * b // gcd(a, b), numbers)