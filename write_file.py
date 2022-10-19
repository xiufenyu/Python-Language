import pandas as pd
print("-------------------pandas write files------------------")

# write list of list to csv
mylist = [["hello", 1], ["world", 2], ["python", 3]]
df = pd.DataFrame(mylist, columns=["name", "count"])
df.to_csv("list.csv")


# write dict of list to csv
data = {
    "item1": [0, 1],
    "item2": [3, 4],
    "item3": [5, 6]
}
df = pd.DataFrame.from_dict(data, orient='index')
df.to_csv("dict.csv")
