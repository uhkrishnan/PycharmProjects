def helper(filename):
  words = []
  helper_dict = {}
  f = open(filename, 'r')
  for line in f:
    print(line)
    words=line.split()
    print(words)
    for word in words:
        word = word.lower()
    for word in sorted(words):
      if word not in helper_dict:
        helper_dict[word] = 1
      else:
        helper_dict[word] = int(helper_dict[word]) + 1


  print(helper_dict)

def main():
    helper('small.txt')

if __name__ == '__main__':
    main()
