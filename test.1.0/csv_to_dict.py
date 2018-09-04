import csv
with open('output.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	l=[]                                                           
	for row in spamreader:
		if row:
			l.append(row[0].split("|"))
d={}                                     
for i in range(len(l[0])):

    d[l[0][i].strip()] = l[2][i].strip() if l[2][i] else None
