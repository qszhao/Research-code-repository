def main():
	import re
	i = 0
	d = {}
	t = []
	num = []
	index = []
	indexnum = []
	writer = csv.writer(open('dict.csv', 'wb'))
	file = open('0.5_0.25_0.25.txt','r')
	for line in file:
		t.append(line)
	
	
	while i < 60:

		num.append(float(t[i]))
		index = re.findall('\d+',t[i+1])
		indexnum.append(int(index[0]))
		i += 2
	for i in range(30):

		d[indexnum[i]] = num[i]

	print d
	print num
	print indexnum
	for key, value in d.items():
		writer.writerow([key, value])


if __name__ == '__main__':
	import csv
	main()