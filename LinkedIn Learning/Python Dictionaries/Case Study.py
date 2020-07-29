import csv
with open('TreeOrdersSubset.csv', mode='r') as infile:
    reader = csv.reader(infile)
    TreeOrderDict = {}
    for row in reader:
        key = row[0]
        if key in TreeOrderDict.keys():
            TreeOrderDict[key] = int(TreeOrderDict[key]) + int(row[1])
        else:
            TreeOrderDict[key] = int(row[1])
    print(TreeOrderDict)

    treeOrders10 = { k:v for k, v in TreeOrderDict.items() if v > 10}
    print(treeOrders10)
