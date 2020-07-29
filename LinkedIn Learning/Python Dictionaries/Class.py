import csv
with open('treeorderssubsetnodupes.csv', 'r') as infile:
    reader = csv.reader(infile)

    trees_dict = {}
    for row in reader:
        key = row[0]
        trees_dict[key] = row[1]

    for obj in trees_dict:
        print(obj, ':', trees_dict[obj])

    # if key in trees_dict:
    #     print('key is present: ', key, trees_dict[key])
    # else:
    #     print('no key')
    key = 999
    if key not in trees_dict:
        print('key error')

#.get method - fetches the key value else message
    ele_alpha = trees_dict.get('477', 'alpha not found')
    ele_beta = trees_dict.get('999', 'beta not found')
    print(ele_alpha)
    print(ele_beta)

    key_list = trees_dict.keys()
    print(key_list)

    values_list = trees_dict.values()
    print(values_list)

    item_list = trees_dict.items()
    print(item_list)

    max_key = max(trees_dict)
    min_key = min(trees_dict)
    print('max_key ', max_key)
    print('min_key ', min_key)

    for k, v in trees_dict.items():
        print('The key is : ', k, 'and the corr. value is : ', v)

    print(sorted(trees_dict.keys()))
    print(sorted(trees_dict.values()))

    infile.close()