def all(mas):
    s=sum(mas[0])
    for i in range(len(mas)):
        if sum(mas[i])!=s:return "No"
        if sum([mas[j][i] for j in range(len(mas))])!=s:"No"
    return "Yes"
lst=[[4,9,2],[3,5,7],[8,1,6]]
print(all(lst))
