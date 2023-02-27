
def get_event_intervals(dfAdaptation) -> list:
    intervals = []
    workloads = []
    currentTime = 0
    currentDirection = 'less'
    currentWorkload = 'low'
    for idx, row in dfAdaptation.iterrows():
        if idx == 0:
            currentTime = row['Time']
            currentDirection = row['Direction']
            continue
        if currentDirection == row['Direction']:
            currentTime = row['Time']
            currentDirection = row['Direction']
        if currentDirection != row['Direction']:
            intervals.append((currentTime, row['Time']))
            currentTime = row['Time']
            oldDirection = currentDirection
            currentDirection = row['Direction']
            if oldDirection == 'less' and currentDirection == 'more':
                currentWorkload = 'low'
            elif oldDirection == 'more' and currentDirection == 'less':
                currentWorkload = 'high'
            workloads.append(currentWorkload)
    return intervals, workloads
