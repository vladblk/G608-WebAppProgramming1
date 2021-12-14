n = int(input('number of plants: '))
plants = set()

plant_heights = input().split()
heights = []

for i in plant_heights:
    heights.append(int(i))

for i in heights:
    plants.add(i)

average = sum(plants) / len(plants)
print(average)
