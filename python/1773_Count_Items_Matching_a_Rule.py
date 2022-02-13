class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            q=0
        elif ruleKey=="color":
            q=1
        else:
            q=2
        c=0
        for i in items:
            if i[q]==ruleValue:
                c+=1
        return c