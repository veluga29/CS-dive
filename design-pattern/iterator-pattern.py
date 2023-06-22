arr = [i for i in range(10)]
dic = {c: i for c, i in zip(("a", "b", "c"), range(3))}
st = {i for i in range(3)}

for i in arr:
    print(i)
for i in dic.items():
    print(i)
for i in st:
    print(i)
