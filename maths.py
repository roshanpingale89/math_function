import pdb
class Utilities:
    def __init__(self, values1, value2):
        self.a = values1
        self.b = value2
    def add(self):
        result = self.a + self.b
        return  result
    def mul(self):
        result = self.a * self.b
        return result
objUtilites = Utilities(10,20)
final_result = objUtilites.add()
print(final_result)
final_mul = objUtilites.mul()
print(final_mul)

