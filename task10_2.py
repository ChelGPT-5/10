class Math:
    def addition(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtraction(self, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiplication(self, a, b):
        print(f"{a} * {b} = {a * b}")

    def division(self, a, b):
        if b == 0:
            print("Ошибка: деление на ноль!")
        else:
            print(f"{a} / {b} = {a / b}")


m = Math()
m.addition(20, 23)
m.subtraction(51, 4)
m.multiplication(16, 7)
m.division(9, 3)
m.division(10, 0)