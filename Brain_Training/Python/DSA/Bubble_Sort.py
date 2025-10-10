array1 = [12,15,3,45,87,2,75,95,13]
print(f"Array:{array1}")
n=len(array1)

for i in range(n-1): # n-1 as in the below loop last value will be already replaced.
    print(f"Array in sorting step: {array1}")
    for j in range(n-i-1):
        if  array1[j] > array1[j+1]:
            array1[j], array1[j+1] = array1[j+1], array1[j]

print(f"Sorted Array : {array1}")
