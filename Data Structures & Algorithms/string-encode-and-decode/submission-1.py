class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "emptykenni"
        return "kennijeez".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "emptykenni": return []
        return s.split("kennijeez")