class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits: return []

        res = []
        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return
            for char in mapping[digits[i]]:
                curr.append(char)
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])
        return res 

