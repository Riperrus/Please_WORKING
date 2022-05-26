def transpose(mas):
    '''temp_matrix=[]
    for i in range(len(mas[0])):
        temp=[]
        for j in range(len(mas)):
            temp+=[mas[j][i]]
        temp_matrix+=[temp]
    print(temp_matrix)'''
    return [[mas[j][i] for j in range(len(mas))] for i in range(len(mas[0]))]



arr=[[1,2,3],[4,5,6]]
arr = transpose(arr)
for i in range(len(arr)):
    print("| ",end='')
    for j in range(len(arr[0])):
        print(arr[i][j],end=" ")
    print("|")
