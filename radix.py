def count_sort(arr,exp):
    n=len(arr)
    output=[0]*n
    count=[0]*10 #0-->9 empty buckets for count of digits
    for i in range(n): #frequencies of units position of numbers
        index=(arr[i]//exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i]+=count[i-1]
    i=n-1
    while i>=0:
        index=(arr[i]//exp)%10
        output[count[index]-1]=arr[i]
        count[index]-=1
        i-=1
    for i in range(n):
        arr[i]=output[i]
def radix_sort(arr):
    max_num=max(arr)
    exp=1
    while max_num//exp>0:
        count_sort(arr,exp)
        exp*=10
arr=[432,8,530,90,88,231,11,45,677,199]
print("Before Sort:",arr)
radix_sort(arr)
print("After Sort:",arr)
