# sort by value
x = {"k0": 10,"k1": 2, "k2": 8, "k": 1}
sorted_x = dict(sorted(x.items(), key=lambda item: item[1]))
print(sorted_x)

# sort in the reverse order
sorted_x = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))
print(sorted_x)

