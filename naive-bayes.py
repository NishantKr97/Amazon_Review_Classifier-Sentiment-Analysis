import csv

posdata = []
with open('positive-data.csv', 'r') as myfile:
    reader = csv.reader(myfile, delimiter=',')
    for val in reader:
        posdata.append(val[0])

print (len(posdata))
print(posdata[0])

# for i in posdata:
#     print(i)