import csv

import reader as reader

reader = csv.reader(open("top50.csv", encoding="ISO-8859-1", delimiter=",")
sortedList = sorted(reader, key=lambda row: row[10], reverse=True)
for key,data in enumerate(sortedList):
if key > 0 and key < 1:
  print(data)