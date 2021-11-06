import time, re, pickle, bz2


with open("rickroll.ascii") as h:
    data = h.readlines()

output = []
tmp = []
for i in data:
    if i.startswith("sleep"):
        output.append(tmp)
        tmp = []
        output.append(float(i.split(" ")[1]))
    else:
        tmp.append(re.sub("(\'|echo -en )", "", i))


del output[0][0]
with bz2.BZ2File("rickroll.pbz2", "wb") as h:
    pickle.dump(output, h)
