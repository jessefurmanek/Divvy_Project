import csv
import json

csvfile = open('Divvy_Stations_2013.csv', 'r')
jsonfile = open('divvy_stationstest.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.reader( csvfile)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n'.join(','))