# Uses python3
import sys


def KPartitionK(nums, k):
        if len(nums) < k:
            return 0
        
        summ = sum(nums)
        if summ % k != 0:
            return 0
        
        nums.sort(reverse=True)
        target = [summ / k] * k

        def dfs(idx):
            if idx == len(nums): 
                return 1
            
            for i in range(k):
                if target[i] >= nums[idx]:
                    target[i] -= nums[idx]
                    if dfs(idx + 1):
                        return 1
                    target[i] += nums[idx] 
            return 0
        return dfs(0)
                        

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(KPartitionK(A,3))
