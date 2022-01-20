#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        i = 0
        count =0
        if i == n-1:
            return 0
        if arr[0]==0:
            return -1
        if arr[i]!=0:    
            while i<n-1:
                b = arr[i+1:i+arr[i]+1]
                for j in range(len(b)):
                    b[j]+=j
                if i + len(b)+1>=len(arr):
                    count +=1
                    break
                else:
                    if max(b)-b.index(max(b)) ==0:
                        return -1
                    else:
                        i += (b.index(max(b))+1)
                        count +=1
                b.clear()
        else:
            return -1
        
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends