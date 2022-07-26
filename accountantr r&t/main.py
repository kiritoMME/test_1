import csv
a=dict()
b=dict()
c=list()
with open("buy.csv",mode="r") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for i in csv_reader:
        if i["id"] not in a.keys():a[i["id"]]=int(i["number"])
        else: a[i["id"]]+=int(i["number"])
with open("sell.csv",mode="r") as csv_file:
    csv_reader=csv.DictReader(csv_file)
    for i in csv_reader:
        if i["id"] not in b.keys():b[i["id"]]=int(i["number"])
        else: b[i["id"]]+=int(i["number"])
all_ids=list(set([*a,*b]))
print(all_ids)
print(a)
print(b)
for i in all_ids:
    if i in a.keys() and i in b.keys():c.append([i,str(a[i]-b[i])])
    elif i in a.keys():c.append([i,str(a[i])])
    elif i in b.keys():c.append([i,str(-b[i])])
f=open("summary.csv",mode="w")
f.write("id,number\n")
print(c)
for i in c:
    f.write(",".join(i)+"\n")
