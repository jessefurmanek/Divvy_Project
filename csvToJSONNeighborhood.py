import csv
import json

csvfile = open('neighborhood_table.csv', 'r')
jsonfile = open('divvy_neighborhoods_test.json', 'w')

#choose fieldnames to be attached
fieldnames = ("name", "number", "latitude","longitude")
output = {'neighborhoods': []}


reader = csv.DictReader(csvfile)
for row in reader:
    output['neighborhoods'].append({
        row['number']:{
            'name': row['name'],
            'number': row['number'],
            'latitude': row['latitude'],
            'longitude': row ['longitude']
        },
    })    
json.dump(output, jsonfile)
print "done"
