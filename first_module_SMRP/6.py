global friends_list
friends_list={}
def add_friends(name_of_person, list_of_friends):
    friends_list[name_of_person]=list_of_friends

def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in friends_list[name_of_person1]:
        return True
    else: return False

def print_friends(name_of_person):
    if name_of_person in friends_list.keys():
        print(" ".join(i for i in sorted(friends_list[name_of_person])))
    else: print(f"Алиса не помнит друзей {name_of_person}")
add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))
