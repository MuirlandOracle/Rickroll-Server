import time, re


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
with open("rickroll.py", "w") as h:
    h.write(f"roll = {str(output)}")
