def bubble_sort(array):
    n=len(arry)
    for i in range(n-2): # n-2 as in the below loop last value will be already replaced.
        print(f"Array in sorting step: {arry}")
        for j in range(n-i-1):
            if  arry[j] > arry[j+1]:
                arry[j], arry[j+1] = arry[j+1], arry[j]

    print(f"Sorted Array : {arry}")

arry = [12,15,3,45,87,2,75,95,13]
print(f"Array:{arry}")
bubble_sort(arry)
# Time complexity would be O(n^2) as after one loop, the array is looped through again and again n times.
# This means there are n⋅n comparisons done in total, so the time complexity for Bubble Sort is: n^2
