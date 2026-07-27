class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            alp = [0]*26
            for c in s:
                alp[ord(c) - ord('a')] += 1
            
            str_map[tuple(alp)].append(s)
        
        return list(str_map.values())