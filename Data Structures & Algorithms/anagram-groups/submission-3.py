class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            alp = [0]*26
            for c in s:
                alp[ord(c) - ord('a')] += 1
            key = '_'.join([str(a) for a in alp])
            str_map[key].append(s)
        
        result = [vals for vals in str_map.values()]
        return result