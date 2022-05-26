def continue_fibonacci_sequence(sequence, n):
    #sequence.append(1)
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        sequence.append(next_element) # это исправляет, так как данный способ не создаёт новый объект
        #sequence = sequence + [next_element] # так как данный способ создаёт новый объект внутри функции, то по завершению функции данный объект подчищается мусорщиком
        #print(id(sequence))

sequence=[1]
continue_fibonacci_sequence(sequence,2)
print(*sequence)