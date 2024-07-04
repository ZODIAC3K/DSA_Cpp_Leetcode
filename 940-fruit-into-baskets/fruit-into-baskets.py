class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        maxlen = 0
        basket = dict()
        
        while r < len(fruits):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            
            if len(basket) <= 2:
                maxlen = max(maxlen, r - l + 1)
            
            if len(basket) > 2:

                basket[fruits[l]] -= 1

                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                    
                l += 1
            
            r += 1

        return maxlen

        