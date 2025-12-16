#  we need to search the lowest value from the array

def find_lowest(*args):
    smallest = args[0]
    position = 0
    for i,item in enumerate(args):
        if smallest > item:
            smallest = item
            position = i

    print(f"Lowest value in the array is: {smallest} and position is : {position}")
my_arr=[43,21,53,45,85,65,2,47,25,12,10,23] # although this is list in python
print(f"Array: {my_arr}")
find_lowest(*my_arr)

# Time complexity would be O(n) as we need to traverse through n No of item.