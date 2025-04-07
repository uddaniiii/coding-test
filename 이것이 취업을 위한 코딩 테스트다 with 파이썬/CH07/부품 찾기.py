# 이진 탐색을 이용한 풀이

'''
def binary_search(arr,target,start,end):
    # 반복문 이용
    # while start<=end:
    #     mid=(start+end)//2
    #     if arr[mid]==target:
    #         return mid
    #     elif arr[mid]<target:
    #         start=mid+1
    #     else:
    #         end=mid-1
    # return None

    # 재귀함수 이용
    if start>end:
        return None
    mid=(start+end)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr,target,mid+1,end)
    else:
        return binary_search(arr,target,start,mid-1)

N= int(input())
nList=list(map(int,input().split()))
# print(nList)
nList.sort()

M=int(input())
mList=list(map(int,input().split()))

for i in mList:
    result=binary_search(nList, i,0,N-1)

    if result!=None:
        print("yes",end=" ")
    else:
        print("no",end=" ")

'''

# 계수 정렬을 이용한 풀이

'''
N= int(input())
nList=list(map(int,input().split()))

array=[0]*1000001
for i in nList:
    array[i]=1

M=int(input())
mList=list(map(int,input().split()))

for i in mList:
    if array[i]==1:
        print("yes",end=" ")
    else:
        print("no",end=" ")
'''

# 집합 자료형을 이용한 풀이

n=int(input())
nList=set(map(int,input().split()))

m=int(input())
mList=list(map(int,input().split()))

for i in mList:
    if i in nList:
        print("yes",end=" ")
    else:
        print("no",end=" ")