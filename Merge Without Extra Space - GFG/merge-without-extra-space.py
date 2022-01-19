#User function Template for python3

class Solution:
    def merge(self, arr1, arr2, n, m): 
        # code here
        arr = arr1 + arr2
        # print('before',arr)
        arr.sort()
        i = 0
        while i < n:
            arr1[i] = arr[i]
            i+=1
        i = 0
        while i <m:
            arr2[i] = arr[n+i]
            i+=1
        
        return arr1,arr2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends