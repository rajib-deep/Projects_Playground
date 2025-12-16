
def with_out_swap(arry):
    n=len(arry)
    for i in range(n-1):
        min_val_at_index=i
        for j in range(i+1,n):
            if arry[j] < arry[min_val_at_index]: # use > to sort in descending order
                min_val_at_index = j

        min_value=arry.pop(min_val_at_index)
        arry.insert(i,min_value)
        print(f"Array in step {i}:{arry}")

    print(f"Sorted Array:{arry}")


arry = [12,15,3,45,87,2,75,95,13]
print(f"Array:{arry}")
with_out_swap(arry)