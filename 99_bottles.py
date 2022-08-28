first = "bottles of beer on the wall"

second = "bottles of beer"

third = "Take one down, pass it around"

last = "bottles of beer on the wall"

number = 99

for i in range(5):
    print(f"{number} {first}")
    print(f"{number} {second}")
    print(f"{third}")
    number -= 1
    print(f"{number} {last}")