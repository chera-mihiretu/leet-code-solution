class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visited = {}
        for i in cpdomains:
            number, domains = i.split()
            domains = domains.split(".")
            for i in range(len(domains)):
                number = int(number)
                dom = ".".join(domains[i:])
                if dom in domain_visited:
                    domain_visited[dom] += number
                else:
                    domain_visited[dom] = number
        return_list = []
        for dom, visit in domain_visited.items():
            return_list.append(str(visit)+" "+dom)
        return return_list