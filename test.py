# arr = []
# def missing_number(arr, n):
#     for i in range(0,n):
#         if arr[i] != i:
#             print(i)

# n = int(input("Enter the number of elements: "))

# for i in range (1,n+1):
#     arr.append(i)
    
# missing_number(arr,n)


# arr = ["😂","😍"]
# print(arr)

def max_product(arr):
    arr.sort(reverse=True)
    return arr[0]*arr[1]

print(max_product([1,4,2,5,3]))