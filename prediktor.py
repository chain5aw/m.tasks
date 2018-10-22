from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from peewee import *
import datetime
from sys import argv
datestamp = datetime.datetime.now()

db = PostgresqlDatabase('postgres', user='postgres',password="kobasica", host="postgres.cchbsaqj5jwd.eu-west-1.rds.amazonaws.com", port="54321")

class Tasks(Model):
    tasks = TextField()
    date = DateTimeField()
    finish = BooleanField (default=False)
    timedone = DateTimeField()
    urgent = IntegerField()
    important = IntegerField()
    category = TextField()

    class Meta:
        database = db


db.connect()

urgent_tasks=[]
urgent_score=[]

entries = (Tasks
          .select()
          .where(Tasks.finish == True)
          .order_by(Tasks.date.desc())
          )

for entry in entries:
    urgent_tasks = urgent_tasks + [entry.tasks]

entries = (Tasks
          .select()
          .where(Tasks.finish == True)
          .order_by(Tasks.date.desc())
          )

for entry in entries:
    urgent_score = urgent_score + [entry.urgent]


train_tasks = urgent_tasks[:200]
test_tasks = urgent_tasks[200:]

train_labels = urgent_score[:200]
test_labels = urgent_score[200:]

vectorizer = TfidfVectorizer()
svm = LinearSVC()

train_vectors = vectorizer.fit_transform(train_tasks)
test_vectors = vectorizer.transform(test_tasks)

svm.fit(train_vectors, train_labels)

predictions = svm.predict(test_vectors)

print (test_tasks[0:5])
print (predictions[0:5])

new_tasks = ["Send Proposal To Tica", 'Send proposal to Hunkemoller','Ing Credit Card','Drink Beer']
new_vectors = vectorizer.transform(new_tasks)
new_predictions = svm.predict(new_vectors)


print ("New tasks:", new_tasks,"Predictions of urgency", new_predictions)
