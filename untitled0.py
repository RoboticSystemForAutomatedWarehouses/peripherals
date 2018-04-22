import json
import time
jsonData = open('task.json').read()   
respond = json.loads(jsonData)
serverTasks = None
columns = 10
rows = 10
xout = 9
yout = 9
zout = 9
gate = []

for i in range(10):
    for j in range(10):
        gate.append((0,i,j))

print(len(gate))

if respond['success'] == True:
    serverTasks = list(respond['result'])
    print(type(serverTasks))

    while serverTasks:
    
        Tasks = list(serverTasks)
        for task in Tasks:
            tempTask = {}
            
            tempTask['id']  = task['id']
    
            if task['isOut'] == True:
                tempTask['xSt'] = task['x']
                tempTask['ySt'] = task['y']
                tempTask['zSt'] = task['z']
                
                tempTask['xEn'] = xout
                tempTask['yEn'] = yout
                tempTask['zEn'] = zout
                serverTasks.remove(task)
            
            elif len(gate):
                tempTask['xSt'] = gate[0][0]
                tempTask['ySt'] = gate[0][1]
                tempTask['zSt'] = gate[0][2]
                
                tempTask['xEn'] = task['x']
                tempTask['yEn'] = task['y']
                tempTask['zEn'] = task['z']
                
                gate.pop(0)
                serverTasks.remove(task)
            else :
                time.sleep(1)
                
            print(tempTask)

print(len(serverTasks))
print(len(gate))
print(respond['result'])            
            
        

            
            
