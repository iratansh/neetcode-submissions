class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # name, emails
        # merge accounts: two emails belong to the same user if there is a common email between both of them.
        # union all the accounts that share similar emails?
        n = len(accounts)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(i):
            if par[i] != i:
                par[i] = find(par[par[i]])
            return par[i]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            r1, r2 = rank[p1], rank[p2]
            if r1 > r2:
                par[p2] = p1
                rank[p1] += r2
            else:
                par[p1] = p2
                rank[p2] += r1
            return True
        
        emailToAcc = {} # email: index of acc
        # for each accounts emails if the email was seen before union the current acc with prev owner
        # otherwise record curr acc as the owner
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    # union 
                    union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list) # index of acc: list of emails
        for e, i in emailToAcc.items():
            leader = find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        return res
