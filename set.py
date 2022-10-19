# add one word into a set
word = "word"
data = set([word])
print(data)

# items in set1 not in set2
data1 = set(["abc", "def", "ghi"])
data2 = set(["abc", "def", "123"])
diff = data1 - data2
print(diff)


# add or merge 2 sets: |
merge = data1 | data2
print(merge)

# add or merge 2 sets: update
data1.update(data2)
print(data1)