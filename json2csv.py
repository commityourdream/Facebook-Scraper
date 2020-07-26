import csv
import json
input_file = open("data.json","r")
output_file = open("post.csv","w")
writer=csv.writer(output_file)
for row in json.loads(input_file.read()):
    writer.writerow(row)
