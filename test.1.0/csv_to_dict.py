import csv
with open('output.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile)
	l=[]                                                           
	for row in spamreader:
		# pr		int row
		if row:
			l.append(row[0].split("|"))
d_list = []
l=l[:-1]
for each_entry in range(len(l[2:])):
	d={}
	for i in range(len(l[0])):
		number = each_entry+2
		d[l[0][i].strip()] = l[number][i].strip() if l[number][i] else None
	d_list.append(d)