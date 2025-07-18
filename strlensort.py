'''perform insertion sort on strings based on length of the words'''
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and len(arr[j])>len(key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
size=int(input("enter the number of elements:"))
arr=[]
print("Enter", size, "elements")
for _ in range(size):
    number=(input())
    arr.append(number)
result=insertion_sort(arr)
print("Sorted Array",result)
