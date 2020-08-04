import pickle

allFiles = []
with open("allFiles.txt", "r") as F:
    contents = F.readlines()
    for line in contents:
        cur = line[:-1]
        allFiles.append(cur)

count = 0
while count < len(allFiles):
    i = count+ 10
    name = "files" + str(i)
    filename = "%s.py" % name
    with open(filename, "w") as G:
        end = count + 10
        subset = allFiles[count:end]
        pickle.dump(subset, G)
    count += 10

#last few
#extra = len(allFiles) % 10

