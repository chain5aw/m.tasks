from sys import argv
import os

os.system('clear')

print"Welcome to m.tasks.01. Type 'help' for commands. Enjoy your day."
order =raw_input("Hi M, what do we need to do today >")


if order == 'open tasks':
    txt = open("tasks.txt")
    print txt.read()
    
elif order== 'new task':
    newtask=raw_input("Add new task > ")
    txt = open("tasks.txt", "a")
    txt.write("\n")
    txt.write(newtask)

else:
    print "Thanks for using m.tasks"
