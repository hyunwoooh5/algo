class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(i):
            if parent[i] == i:
                return i

            # path compression
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                parent[root_i] = root_j

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]

            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name
                union(first_email, email)

        res_groups = {}
        for email in parent:
            root = find(email)
            if root not in res_groups:
                res_groups[root] = []
            res_groups[root].append(email)

        ans = []
        for root in res_groups:
            sorted_emails = sorted(res_groups[root])
            ans.append([email_to_name[root]] + sorted_emails)

        return ans
