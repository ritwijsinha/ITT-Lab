states = "Mississippi Alabama Texas Massachusetts Kansas"
statesList = []
statesList.append([x for x in states.split() if x.endswith('xas')][0])
statesList.append([x for x in states.split() if x.lower().startswith('k') and x.lower().endswith('s')][0])
statesList.append([x for x in states.split() if x.startswith('M') and x.endswith('s')][0])
statesList.append([x for x in states.split() if x.endswith('a')][0])
statesList.append([x for x in states.split() if x.startswith('M')][0])
print statesList