
class Solution(object):
    words = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
    11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
    19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}
    
    places = {10: "ten", 100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion", 1000000000000: "trillion",
    1000000000000000: "quadrillion", 1000000000000000000: "quintillion"}

    def to_english(self, number):
        if number == 0:
            return Solution.words[0]
    
        answer = ''
        i = 1
        if number >= 1000:
            num1 = int(str(number)[-3:])
            answer_1 = self.helper(num1)
            num_2 = int(str(number)[:-3])
        
            while num_2 > 0:
      
                if num_2 % 1000 != 0:
                    answer = self.helper(num_2%1000) + Solution.places[1000**i] + ' ' + answer
                    i += 1
                    num_2 = num_2 // 1000
            return answer + answer_1
        else:
            return self.helper(number)

    def helper(self, num):   #999까지쓸수 있음. 세자리용
        if num <= 20:
            return Solution.words[num]+ ' '
        elif num < 100:
            num_1 = num - int(str(num)[1])
            return Solution.words[num_1] + '-' + Solution.words[int(str(num)[1])] + ' '
        else:
            return Solution.words[num//100] + ' ' + Solution.places[100] + ' ' + self.helper(num%100)

solution = Solution()
print(solution.to_english(7))
print(solution.to_english(575))
print(solution.to_english(78193512))




# to_english(575) -> five hundred seventy-five
# to_english(575575) -> five hundred seventy-five thousand fivehundred seventy-five
# to_english(575575575) -> five hundred seventy-five million five hundred seventy-five thousand fivehundred sevnty-five

# to_english(75)  ->  fifty-five
# to_english(7575)  -> seven thousand five hundred fifty-five
# to_english(57575) -> fifty-seven thousand five hundred fifty-five

