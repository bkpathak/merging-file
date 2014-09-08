merging-file
============

The program creates the dictionary with the key from the shared key and update the order dictionary as new files is read.It used the python csv.DictReader which creates the dictionary from each line of csv file with key as a column name.The program is created using python 3.4.

#### Running the program

Pass the filenames and share key column id as pair to the program.
```
python merge_csv.py <filename> <shared column id>  <filename> <shared column id>  ....
python merge_csv.py data/countries.csv id data/regions.csv id
```

The sample csv file *countries.csv* and *regions.csv* under folder *data* contains information about the airports.The files have shared key which is named ***id*** , the id of the airport.The program merge two file using ***id*** as shared key. The output is written to *merged.csv* file under *data*

#### Alternative method

The merge of multiples files can also be done using python ***pandas*** library. The ***merge*** function provides the similar functionality of SQL merge. 