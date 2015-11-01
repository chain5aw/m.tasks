#!/usr/bin/env python2
from peewee import *
import datetime
from sys import argv
import os
datestamp = datetime.datetime.utcnow()

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
    date = DateField()
    finish = BooleanField (default=False)
    
    class Meta:
        database = db


db.connect()
os.system('clear')
print bcolors.WARNING + "Welcome to m.tasks.02. Type 'help' for commands. Enjoy your day." + bcolors.ENDC
    
order =raw_input("Hi M, what do we need to do today >")

while order.strip() != 'exit':
    
    if order == 'new task':
        newtask=raw_input("Add new task > ")
        Tasks.insert(tasks=newtask,date=datestamp).execute()
        
    elif order == 'show':
        entries = Tasks.select().order_by(Tasks.date.desc())
        for entry in entries:
            print bcolors.HEADER + (entry.tasks) + bcolors.ENDC
            
    elif order == 'work':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == False)
                  )
        for entry in entries:
            print bcolors.UNDERLINE + (entry.tasks) + bcolors.ENDC
            
    elif order == 'done':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == False)
                  )
        for entry in entries:
            print(entry.tasks, entry.id)
            
        finishedtask=raw_input("ID of finished task > ")
        
        q = Tasks.update(finish=True).where(Tasks.id == finishedtask)
        q.execute()
        print 'Done'
        
    elif order == 'undone':
        entries = (Tasks
                  .select()
                  .where(Tasks.finish == True)
                  )
        for entry in entries:
            print(entry.tasks, entry.id)
            
        finishedtask=raw_input("Which task do you want to revert > ")
        
        q = Tasks.update(finish=False).where(Tasks.id == finishedtask)
        q.execute()
        print 'Done'
      
            
    elif order == 'help':
        print bcolors.WARNING + "Type 'new task' for adding new task, 'show' to show all tasks, 'work' to show unfinished tasks, 'done' to finish the task, 'undone' to revert" + bcolors.ENDC
        
    
    #   elif order == 'delete':
            

    order =raw_input("Hi M, what do we need to do today >")
    