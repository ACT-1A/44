total = 0
while True:
    number = int(input("enter integer(0 to exit): "))
    total += number
    if number == 0:
        break
print(f"total: {total}")