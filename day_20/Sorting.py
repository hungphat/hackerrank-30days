import sys
s = '3 2 1'
a = list(map(int, s.strip().split(' ')))
# Write Your Code Here
count = 0
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            count +=1
            a[j+1], a[j] = a[j], a[j+1]

print('Array is sorted in',count,'swaps.')
print('First Element:', a[0])
print('Last Element:', a[-1])
