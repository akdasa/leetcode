class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation in ["--X", "X--"]:
                x = x - 1
            elif operation in ["++X", "X++"]:
                x = x + 1
        return x
