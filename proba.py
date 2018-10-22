#!/usr/bin/python
# automated script for sending emails

from peewee import *
from sys import argv
 
from email.mime.text import MIMEText
from subprocess import Popen, PIPE

import plotly.plotly as py
import plotly.graph_objs as go


db = PostgresqlDatabase('postgres', user='postgres',password="kobasica", host="postgres.cchbsaqj5jwd.eu-west-1.rds.amazonaws.com", port="54321")

class Tasks(Model):
    tasks = TextField()
    date = DateField()
    finish = BooleanField (default=False)
    timedone = DateField()
    urgent = IntegerField()
    important = IntegerField()
    impact = IntegerField()
    
    class Meta:
        database = db

db.connect()
tasks=[]
urgent=[]
important=[]
impact=[]

entries = (Tasks
           .select()
           .where(Tasks.finish == False)
           .order_by(Tasks.date.desc())
           )
for entry in entries:
     tasks.append (entry.tasks) 
     urgent.append (entry.urgent)
     important.append (entry.important)
     impact.append (entry.impact)

trace0 = go.Scatter(
    x=urgent,
    y=important,
    text=tasks,
    mode='markers',
    marker=dict(
        color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
        size=impact,
    )
)
data = [trace0]
layout = go.Layout(
    title='Todo.ai',
    xaxis=dict(
            title='Urgent'),
    yaxis=dict(
            title='Important'),
    showlegend=False,
    height=600,
    width=600,
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='todo.ai')




# https://plot.ly/~martinbirac/45
# msg = MIMEText(poruka)
# msg["From"] = "Todo.ai@tasks.email"
# msg["To"] = "m@mnlth.co"
# msg["Subject"] = "There is no try, only do."
# p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE, universal_newlines=True)
# p.communicate(msg.as_string())
