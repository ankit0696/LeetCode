#User function Template for python3

class Solution:
    def maxSubArraySum(self,arr,N):
        maxSum,sum = arr[0], 0
        for ele in arr:
            sum += ele
            if maxSum < sum:
                maxSum = sum
            if sum < 0:
                sum = 0
        if maxSum == 0:
            maxSum = arr[0]
            for ele in arr:
                if ele > maxSum:
                    maxSum = ele
        return maxSum
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends