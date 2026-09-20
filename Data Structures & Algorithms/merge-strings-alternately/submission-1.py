class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3=[]
        i,j=0,0
        while i<len(word1) and j<len(word2):
            word3.append((word1[i]+word2[j]))
            i+=1
            j+=1
        for i in range(i,len(word1)):
            word3.append(word1[i])
        for j in range(j,len(word2)):
            word3.append(word2[j])
        return "".join(word3)