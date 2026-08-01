class Solution:
    def simplifyPath(self, path: str) -> str:
        simplified = []
        for section in path.split("/"):
            if section == "..":
                if simplified:
                    simplified.pop()
            elif section and section != ".":
                simplified.append(section)
        
        simplified = "/".join(simplified)
        return "/" + simplified

