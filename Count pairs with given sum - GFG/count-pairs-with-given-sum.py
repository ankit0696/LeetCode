#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count = 0
        dic = {}
        for ele in arr:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
                

        for ele in arr:
            temp = k - ele
            dic[ele] -= 1
            if temp in dic:
                count += dic[temp]
    
         
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends