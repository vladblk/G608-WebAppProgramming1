n = int(input('n: '))
nums = []
for i in range(n):
    nums.append(int(i+1))
print(nums)
t = tuple(nums)
print(hash(t))