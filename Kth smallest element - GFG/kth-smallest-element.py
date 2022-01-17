#User function Template for python3
import random
def partition(A,left,right,test):
    p=random.randint(left,right)
    pivot=A[p]
    A[p],A[right]=A[right],A[p]
    j=left
    for i in range(left,right):
        if A[i]<=pivot:
            A[i],A[j]=A[j],A[i]
            j+=1
    A[j],A[right]=A[right],A[j]
    if(j==test):
        return A[test]
    elif(j<test):
        return partition(A,j+1,right,test)
    else:
        return partition(A,left,j-1,test)

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        return partition(arr,l,r,k-1)

    
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends