class check:
    def __init__(self):
        self.items=[]
        self.index=1



def add_item(item_name, item_cost):
    global check_one
    check_one.items.append([item_name,item_cost])
def print_receipt():
    global check_one
    if len(check_one.items)!=0:
        print(f"Чек {check_one.index}. Всего предметов: {len(check_one.items)}")
        for i in check_one.items:
            print(f"{i[0]} - {i[1]}")
        print(f"Итого: {sum([j[1] for j in check_one.items])}\n-----")
        check_one.index += 1
        check_one.items = []

check_one=check()

