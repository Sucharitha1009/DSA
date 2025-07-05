def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
size=int(input("enter the number of elements:"))
arr=[]
print("Enter", size, "elements")
for _ in range(size):
    number=int(input())
    arr.append(number)
result=insertion_sort(arr)
print("Sorted Array",result)
