

weight = 75
for date in range(365):
    if date < 180:
        weight = weight + 0.1
    else:
        weight = weight - 0.12
print("Your weight after a year is", weight)
