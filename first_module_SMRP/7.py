def count_food(days):
    global daily_food
    return sum([daily_food[i-1] for i in days])
daily_food = [0, 150, 150]
print(count_food([1]))
print(count_food([2, 3]))
