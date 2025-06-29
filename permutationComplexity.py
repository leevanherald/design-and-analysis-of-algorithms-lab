import itertools

s = [5, 4, 6, 2, 7, 1, 3, 8, 9]
for p in itertools.permutations(s):
    print(p)

# Calculate the average number of max updates

array = [5, 4, 6, 2, 7, 1, 3, 8, 9]

count = 0
max = float('-inf')

for i in range(len(array)):
    if array[i] > max:
        max = array[i]
        count = count + 1
    print(max)
    print(count)
    print(array)
