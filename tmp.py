a, b = "", ""
while not a and not b:
    print("ВВедите два числа через пробел: ")
    ls = input().split()
    if len(ls) == 2 and ls[0].isnumeric() and ls[1].isnumeric():
        a, b = ls
        
        
print(f"== {a}, {b} ==")

