class Solution:
    def getBinaryRep(self, n):
        binary = bin(n)[2:]
        return "0" * (30 - len(binary)) + str(binary)


n = 625
ob = Solution()
ans = ob.getBinaryRep(n)
print(ans)
