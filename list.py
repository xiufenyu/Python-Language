data = [10, 8, 4, 1, 2, 3, 4, 5]

# reverse list in order:
data.reverse()
print(data)


# sort list of list:
l = [[0, 1, 'f'], [4, 2, 't'], [9, 4, 'afsd']]
# in place:
l.sort(key=lambda x: x[2])
print(l)
# not in place:
l2 = sorted(l, key=lambda x: x[2])
print(l2)

# insert an item at place i
l.insert(1, [10, 6, 'bacon'])
print(l)
