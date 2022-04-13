import json
import os

path=""

f = open('customobjects.json')
objects = json.load(f)
f.close()
f = open('objects_et.json')
objects2 = json.load(f)
f.close()


subtask=set()

filelist=os.listdir(path+'train/')

for file in filelist:
    f = open(path+'edh_samples/'+file)
    data = json.load(f)
    subtask.update(data['history_subgoals'])
    subtask.update(data['future_subgoals'])
    f.close()

remaining=[h for h in subtask if ((h not in objects["objects"])and(h not in objects2["objects"]))]
print(remaining)
