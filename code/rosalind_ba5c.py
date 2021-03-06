# ^_^ coding:utf-8 ^_^

"""
Find a Longest Common Subsequence of Two Strings
url: http://rosalind.info/problems/ba5c/

Given: Two strings.
Return: A longest common subsequence of these strings.
"""

import pprint

def LCS(s1, s2):
    m, n = len(s1), len(s2)
    DP = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                DP[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                DP[i][j] = DP[i-1][j-1]+1
            else:
                DP[i][j] = max(DP[i-1][j], DP[i][j-1])
    # pprint.pprint(DP)
    res = ""
    i, j = len(s1), len(s2)
    while (i>0 and j>0):
        if DP[i][j] == DP[i-1][j]:
            i -= 1
        elif DP[i][j] == DP[i][j-1]:
            j -= 1
        else:
            res = s1[i-1]+res
            i -= 1
            j -= 1
    print(res)
    return DP[m][n]

if __name__ == "__main__":
    with open("../data/rosalind_ba5c.txt", "r") as f:
        s1 = f.readline().strip()
        s2 = f.readline().strip()
    # s1 = "AACCTTGG"
    # s2 = "ACACTGTGA"
    res = LCS(s1, s2)