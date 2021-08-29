def merge(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        first=arr[:mid]
        second=arr[mid:]
        merge(first)
        merge(second)
        i=0
        j=0
        k=0
        while(i<len(first) and j<len(second)):
            if(first[i]<second[j]):
                arr[k] =first[i]
                i=i+1
                k=k+1
            else:
                arr[k]=second[j]
                j=j+1
                k=k+1
                
                
        while(i<len(first)):
            arr[k]=first[i]
            i=i+1
            k=k+1
        while(j<len(second)):
            arr[k]=second[j]
            j=j+1
            k=k+1
            
n= int(input())
x=list(map(int,input().split()))
merge(x)
print(*x)