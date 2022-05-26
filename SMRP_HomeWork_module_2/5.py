def same_by(characteristic, objects):
    lst=list(filter(characteristic,objects))
    if len(lst)==0:return True
    return False


#values = [0, 2, 10, 6]
values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
