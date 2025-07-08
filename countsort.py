def csort(arr):
    if not arr:
        return [] 
    max_val=max(arr)
    count=[0]*(max_val+1)
    for num in arr:#freq
        count[num]+=1
    for i in range(1,len(count)):#count
        count[i]+=count[i-1]
    output=[0]*len(arr)
    for num in reversed(arr):#stablesort
        output[count[num]-1]=num
        count[num]-=1
    for i in range(len(arr)):#copin sorted list
       arr[i]=output[i]
arr=[4,2,2,8,3,1]
print("Before:",arr)
csort(arr)
print("After:",arr)
