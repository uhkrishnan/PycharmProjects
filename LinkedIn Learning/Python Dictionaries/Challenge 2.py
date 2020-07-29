import csv
with open('treeorderssubsetnodupes.csv', mode='r') as infile:
    reader = csv.reader(infile)

    tree_hash = {}
    #getting data into the dict
    for row in reader:
        key = row[0]
        if key not in tree_hash:
            tree_hash[key] = row[1]
        else:
            tree_hash[key] = int(tree_hash[key]) + int(row[1])
    print(tree_hash.items())

    infile.close()