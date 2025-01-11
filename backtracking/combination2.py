class Solution:
    solution = []
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr = []
        total = 0
        ans = []
        candidates.sort()
        def dfs(i,total,curr):
            if total == target:
                ans.append(curr.copy())
                return
            elif total > target or i >= len(candidates):
                return
            else:
                #include candidates[i]
                curr.append(candidates[i])
                dfs(i+1, total + candidates[i],curr)
                curr.pop()
                #exclude candidates[i]
                while  i + 1 < len(candidates) and  candidates[i] == candidates[i+1] :
                    i += 1
                dfs(i+1,total,curr)
        dfs(0,0,[])
        solution = [list(i) for i in ans]
        return solution
        