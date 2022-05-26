s=input()
#s="пара-ра-рам рам-пам-папам па-ра-па-дам"
lst=[i.split("-") for i in s.split()]
lib="ёуеыаоэяиюЁУЕЫАОЭЯИЮ"
sum_glass=[]
for i in lst:
    index=0
    for j in i:
        for k in j:
            if k in lib:index+=1
    sum_glass.append(index)
k=True
for i in sum_glass:
    if i!=sum_glass[0]:k=False
if k:print("Парам пам-пам")
else:print("Пам парам")
