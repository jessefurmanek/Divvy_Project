import csv
import json

csvfile = open('Neighborhood_table.csv', 'r')
jsonfile = open('divvy_neighborhoods.json', 'w')

#choose fieldnames to be attached
fieldnames = ("name", "number", "latitude","longitude")

reader = csv.DictReader(csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write(', ')
print "done"
