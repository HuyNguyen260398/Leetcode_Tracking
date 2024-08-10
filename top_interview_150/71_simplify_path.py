class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical_path = ["/"]
        dirs = path.split("/")
        for dir in dirs:
            if dir.strip() not in ["", ".", ".."]:
                canonical_path.append(dir)
                canonical_path.append("/")
            if dir == ".." and len(canonical_path) > 1:
                canonical_path.pop()
                canonical_path.pop()
        if len(canonical_path) == 0:
            canonical_path.append("/")
        if len(canonical_path) > 1:
            canonical_path.pop()
        return "".join(canonical_path)

    def simplifyPath2(self, path: str) -> str:
        canonical_path = []
        dirs = path.split("/")
        for dir in dirs:
            if dir in ["", "."]:
                continue
            elif dir == "..":
                if canonical_path:
                    canonical_path.pop()
            else:
                canonical_path.append(dir)
        return "/" + "/".join(canonical_path)
