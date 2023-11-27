list_1 = [[1, 2], [3, 5], [6, 7]]

list = []
dict = {}

for i in list_1:
  dict['fi'] = i[0]
  dict['se'] = i[1]
  list.append(dict)

print(list)
