#!/usr/bin/env python2
from peewee import *
import datetime
from sys import argv
import os
datestamp = datetime.datetime.now()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


db = PostgresqlDatabase('postgres', user='postgres',password="kobasica", host="postgres.cchbsaqj5jwd.eu-west-1.rds.amazonaws.com", port="54321")

class Tasks(Model):
    tasks = TextField()
    date = DateTimeField()
    finish = BooleanField (default=False)
    timedone = DateTimeField()
    urgent = IntegerField()
    important = IntegerField()
    
    class Meta:
        database = db


db.connect()
os.system('clear')
print bcolors.WARNING + "Welcome to m.tasks.03. Type 'help' for commands. Enjoy your day." + bcolors.ENDC
    
order =raw_input("Hi M, what do we need to do today >")

while order.strip() != 'exit':
    
    if order == 'new':
        newtask=raw_input("Add new task > ")
        Tasks.insert(tasks=newtask,date=datetime.datetime.now()).execute()
        
    elif order == 'all':
        entries = Tasks.select().order_by(Tasks.date.desc())
        for entry in entries:
            print bcolors.HEADER + (entry.tasks) + bcolors.ENDC
            
    elif order == 'show':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == True)
                  .order_by(Tasks.date.desc())
                  )
        for entry in entries:
            print bcolors.OKBLUE + (entry.tasks) + bcolors.ENDC
            
    elif order == 'todo':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == False)
                  .order_by(Tasks.date.desc())
                  )         
                  
        for entry in entries:
            timediff = datetime.datetime.now() - entry.date
            if timediff.days < 10:
                print bcolors.HEADER + (entry.tasks) + bcolors.ENDC + " | " +  bcolors.HEADER + str(timediff.days) + " days old" + bcolors.ENDC
            else: 
                print bcolors.HEADER + (entry.tasks) + bcolors.ENDC + " | " + bcolors.WARNING + str(timediff.days) + " days old" + bcolors.ENDC
                        
    elif order == 'done':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == False)
                  .order_by(Tasks.date.desc())
                  )
        for entry in entries:
            print(entry.tasks, entry.id)
            
        finishedtask=raw_input("ID of finished task > ")
        
        q = Tasks.update(finish=True,timedone=datetime.datetime.utcnow()).where(Tasks.id == finishedtask)
        q.execute()
        
        print 'Done'
        
    elif order == 'undone':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == True)
                  .order_by(Tasks.date.desc())
                  )
                  
        for entry in entries:
            print(entry.tasks, entry.id)
            
        finishedtask=raw_input("Which task do you want to revert > ")
        
        q = Tasks.update(finish=False).where(Tasks.id == finishedtask)
        q.execute()
        print 'Done'
        
    elif order == 'time':
        entries = (Tasks
                   .select()
                   .where(Tasks.id == 78)
                   )
        
        for entry in entries:
            
            print (entry.date)
      
            
    elif order == 'help':
        print bcolors.WARNING + "Type 'new' for adding new task" + bcolors.ENDC 
        print bcolors.WARNING + "Type 'all' to show all tasks" + bcolors.ENDC
        print bcolors.WARNING + "Type 'show' to show done tasks" + bcolors.ENDC
        print bcolors.WARNING + "Type 'todo' to show unfinished tasks" + bcolors.ENDC
        print bcolors.WARNING + "Type 'done' to finish the task" + bcolors.ENDC
        print bcolors.WARNING + "Type 'undone' to revert" + bcolors.ENDC
        
    else:
        print bcolors.FAIL + "This command is not supported. Type 'help' to get the list of all comands." + bcolors.ENDC
    
    #   elif order == 'delete':
            

    order =raw_input("Hi M, what do we need to do today >")