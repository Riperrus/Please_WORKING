s = input()
lib={}
for i in range(2,11):
    lib[i]=i
lib[11]="Валет"
lib[12]="Дама"
lib[13]="Король"
lib[14]="Туз"
words=["пик","треф","бубен","червей"]
for i in range(2,15):
    for j in words:
        if j==s:continue
        print(f'{lib[i]} {j}')
        