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
                eligible.sort(key=lambda t: next_release(time, t) + t['deadline'])
            elif algorithm == 'RM':
                eligible.sort(key=lambda t: t['period'])
            elif algorithm == 'DM':
                eligible.sort(key=lambda t: t['deadline'])
            elif algorithm == 'FIFO':
                pass  # garder l'ordre d'arrivée
            task = eligible[0]
            schedule.append({'time': time, 'task': task['name']})
        else:
            schedule.append({'time': time, 'task': 'Idle'})

    return schedule, utilization

def next_release(time, task):
    # Calcul de la prochaine release time de cette tâche
    return ((time // task['period']) + 1) * task['period']

def lcm(numbers):
    from math import gcd
    from functools import reduce
    def lcm_pair(a, b):
        return a * b // gcd(a, b)
    return reduce(lcm_pair, numbers)