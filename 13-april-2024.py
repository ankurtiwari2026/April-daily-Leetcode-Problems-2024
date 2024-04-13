class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        ans = 0
        h = [0] * N
        nextSmaller = [0] * N
        for i in range(M):
            for j in range(N):
                h[j] = 0 if matrix[i][j] == '0' else h[j] + 1
            stack = []
            for j in range(N - 1, -1, -1):
                while stack and h[j] <= h[stack[-1]]:
                    stack.pop()
                nextSmaller[j] = N if not stack else stack[-1]
                stack.append(j)
            stack = []
            for j in range(N):
                while stack and h[j] <= h[stack[-1]]:
                    stack.pop()
                prevSmaller = -1 if not stack else stack[-1]
                ans = max(ans, (nextSmaller[j] - prevSmaller - 1) * h[j])
                stack.append(j)
        return ans
