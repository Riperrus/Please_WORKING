def mirror(arr):
    #mirrored_part = arr.reverse() # данная метод изменяет список, к которому применяется и возвращает None
    mirrored_part=arr[::-1] # в данном случае можно испоьзовать слайс, так как он не изменяает исходный список
    arr = arr +  mirrored_part
