import json
import queue
import time

taskList = []
gate = queue.Queue()


columns = 10
rows = 10
xout = 9
yout = 9
zout = 9

#initiate gate positions
for i in range(10):
    for j in range(10):
        gate.put((0,i,j))

def sendTasksToAVR(packages):
    print(packages)
    
    
    
def excuiteTasks():
    todo = list(taskList)
    taskcnt = len(todo)
    taskStrings = []
    packages = []
    
    #transform each task to a string
    for i in range(taskcnt):
        task = todo[i]
        t=""
        for k in task:
            t +=  str(task[k]) if task[k] > 9 else "0" +str(task[k])
            t += "/"
        t = t[:-1]
        taskStrings.append(t)
        taskcnt-=1
            
    print(taskStrings)
    
    tempTaskStrings = list(taskStrings)
    #form packages
    while len(tempTaskStrings):
        packagecnt = min(len(tempTaskStrings),3)
        package  = ""
        package += "0"+str(packagecnt)+"/"
        
        for i in range(packagecnt):
           package +=  tempTaskStrings[0] + "/"
           tempTaskStrings.pop(0)
        package = package[:-1] + "#"
        packages.append((packagecnt,package))
    sendTasksToAVR(packages)
    
    
#read data from server
jsonData = open('task.json').read()  
respond = json.loads(jsonData)

#repeat till sucess response
while respond['success'] == False:
    jsonData = open('task.json').read()  
    respond = json.loads(jsonData)

#duplicate server Tasks to work on them
serverTasks = list(respond['result'])

#repate until finish all serverTasks
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
            taskList.append(tempTask)
            serverTasks.remove(task)
        
        elif gate.empty() is False:
            g = gate.get()
            tempTask['xSt'] = g[0]
            tempTask['ySt'] = g[1]
            tempTask['zSt'] = g[2]
            
            tempTask['xEn'] = task['x']
            tempTask['yEn'] = task['y']
            tempTask['zEn'] = task['z']
            taskList.append(tempTask)
            serverTasks.remove(task)
            
        #if the task is input and the gate is avialbe pos is empty 
        else :
            continue
            
    if len(serverTasks) == 0 or gate.empty is True:
            print('--Tasks loaded on gate & Ready To be Excuited--')
            
print('--Tasks recived form server FINISHED--')
excuiteTasks()

    
taskList_str=queue.Queue()

for i in range(0,len(taskList)):
    print(taskList[i])
    task_str=""
    for key in taskList[i]:
        item_str=""        
        if taskList[i][key] < 10:
            item_str +="0"
        item_str += str(taskList[i][key])
        item_str +="/"
        task_str += item_str
    taskList_str.put(task_str)

#print(taskList_str)
no_of_tasks=0
if not taskList_str.empty():
    package_str="0"
    if taskList_str.qsize()>3:
        no_of_tasks=3
        package_str+="3/"
    else:
        no_of_tasks=taskList_str.qsize()
        package_str+=str(taskList_str.qsize())
        package_str+="/"
    for i in range(0,no_of_tasks):
        package_str +=taskList_str.get()
    packageList_str=list(package_str)
    packageList_str[-1]='#'
    package_str=''.join(packageList_str)
    print(package_str)


 ##end to 3 tasks to the micro
    

'''
"02/01/00/01/01/02/03/02/02/01/02/03/02/00/01/02#"     
          
'''      
