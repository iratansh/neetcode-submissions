class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # guaranteed that all people will have weight <= limit
        people.sort()
        res, l, r = 0, 0, len(people) - 1

        while l <= r:
            currWeight = people[l] + people[r]
            if currWeight <= limit:
                res += 1
                l += 1
                r -= 1
            else:
                # will need 1 boat in this case?
                # the heaviest person cant match with the lightest person
                res += 1
                r -= 1

        return res