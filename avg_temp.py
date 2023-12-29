x = int(input("How many days? "))
arr = []
for i in range(0,x):
    temp = int(input("Enter the highest temp: "))
    arr.append(temp)

avg = sum(arr)/x

print("The Avg Temp is ",avg)