def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
size=int(input("enter the number of elements:"))
arr=[]
print("Enter the elements:")
for _ in range(size):
    arr.append(int(input()))
print("original list:",arr)
bubble_sort(arr)
print("Bubble Sorted:",arr)
#O(n)
#O(n^2)   
