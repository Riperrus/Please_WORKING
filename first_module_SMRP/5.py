print("Как вас зовут?")
name=input()
def polite_input(question):
    global name
    word=input(f"{name}, {question}\n")
    return word
age = polite_input('укажите возраст')
school_number = polite_input('укажите номер школы')
class_num = polite_input('укажите полный номер класса')
