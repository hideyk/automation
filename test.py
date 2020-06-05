from collections import Counter


testlist = [1, 2, 3, 4, 5, 6, 7, 1, 2, 1]

abc = [item for item, count in Counter(testlist).items() if count > 1]
print(abc)

enumlist = list(enumerate(testlist))
print(enumlist)