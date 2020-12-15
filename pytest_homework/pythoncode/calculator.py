class Calculator:
    def add(self, a, b):
        return round(a + b, 2)

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return round(a * b,2)

    def div(self, a, b):
        if b == 0:
            return "分母不能为0"
        else:
            return round(a / b, 2)
