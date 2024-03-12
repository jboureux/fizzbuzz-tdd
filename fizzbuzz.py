class FizzBuzz:

    def generateNumber(self, number: int):
        result = ""

        if number % 15 == 0 :
            result = "FizzBuzz"
        elif number % 3 == 0 :
            result = "Fizz"
        elif number % 5 == 0 :
            result = "Buzz"
        else :
            result = str(number)

        return result


    def generate(self, mini: int, maxi: int):
        result = ""
        for number in range(mini, maxi+1):
            result += self.generateNumber(number)
        return result