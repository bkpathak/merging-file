import csv
import sys
from collections import OrderedDict


def merge_file(arg_list):
	filenames = arg_list[0:-1:2] # extract filename from user input
	keynames = arg_list[1:-1:2]  # extract share column from user input
	shared_index = OrderedDict() # dictionary to merge files using shared key 
	column_names = []
	for filename, keyname in zip(filenames , keynames):
		with open(filename, "r") as fp: 
			read_file = csv.DictReader(fp)
			column_names.extend(read_file.fieldnames)
			for row in read_file:
				# update the dictionary for each files with shared key
				shared_index.setdefault(row[keyname], {}).update(row) 

	column_names = list(OrderedDict.fromkeys(column_names))
	with open("data/merged.csv", "w") as fp:
		write_file = csv.writer(fp)
		write_file.writerow(column_names)
		for row in shared_index.values():
			write_file.writerow([row.get(field, '') for field in column_names])



if __name__ == '__main__':
	merge_file(sys.argv[1:])



#    Alternatively using pandas 
'''
import pandas as pd
df1 = pd.read_csv('data/regions.csv')
df2 = pd.read_csv('data/countries.csv')
merged = df1.merge(df2, on="id", how="outer").fillna("")
merged.to_csv("merged.csv", index=False)
'''
