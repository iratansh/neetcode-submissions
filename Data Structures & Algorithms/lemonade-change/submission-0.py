class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # each lemonade costs 5$
        # the customer pays with bills[i]
        # need to keep track of bills 
        five = ten = 0

        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            else:
                if not ten:
                    if five < 3:
                        return False
                    five -= 3
                else:
                    if five == 0:
                        return False
                    ten -= 1
                    five -=1

        return True