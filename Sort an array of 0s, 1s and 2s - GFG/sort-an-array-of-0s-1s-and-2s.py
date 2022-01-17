#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        zero,one,two= 0,0,0
        for ele in arr:
            if ele == 0:
                zero +=1
            elif ele == 1:
                one += 1
            else:
                two +=1

        index = 0
        while zero > 0:
            arr[index] = 0
            zero -=1
            index +=1
        while one > 0:
            arr[index] = 1
            one -=1
            index +=1
        while two > 0:
            arr[index] = 2
            two -=1
            index +=1
        
        return arr
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends