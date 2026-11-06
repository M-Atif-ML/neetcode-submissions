class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)

        for string in strs:
            key =[0] * 26
     
            for char in string:
          
                key[ord(char)-ord('a')] +=1
            temp[tuple(key)].append(string)

        return list(temp.values())