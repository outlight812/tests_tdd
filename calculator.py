class Calculator:
    def __init__(self):
        self.operators = "+-*/**"

    def calc(self,expression: str):
        data = self.input(expression)
        if data[1] == "+":
            return data[0] + data[2]
        elif data[1] == "-":
            return data[0] - data[2]
        elif data[1] == "*":
            return data[0] * data[2]
        elif data[1] == "/":
            return data[0] / data[2]
        elif data[1] == "**":
            return data[0] ** data[2]

    def input(self,expression: str):
        data = expression.split()
        if len(data) != 3:
            raise ValueError("не правильное выражение")
        if data[1] not in self.operators:
            raise ValueError("не верный оператор")
        num1 = data[0]
        if num1.startswith("-"):
            num1 = num1[1:]
        num2 = data[2]
        if num2.startswith("-"):
            num2 = num2[1:]
        if not num1.isdigit() or not num2.isdigit():
            raise ValueError("в выражении могут быть только числа")
        return [int(data[0]),data[1],int(data[2])]
