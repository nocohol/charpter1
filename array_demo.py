bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# print first item and capitalize first letter
print(bicycles[0].title())

# print last one
print(bicycles[-1].title())

# delete first item
del bicycles[0]
print(bicycles)

# pop last item
bicycles.pop()
print(bicycles)

# remove 'redline'
bicycles.remove('redline')
print(bicycles)

n = [1,3,2,5,4]
# sort items in ascending order
n.sort()
print(n)
# sort items in decending order
n.sort(reverse=1)
print(n)

for i in n:
    print(i)

# range of 1 - 10 with step 2
for value in range(1, 10, 2):
    print(value)

squares = [value**2 for value in range(1, 11)]
print(squares)
