class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return f"газировка с {self.flavor} вкусом"
        else:
            return "обычная газировка"


s1 = Soda()
s2 = Soda('клубничным')
print(s1)
print(s2)