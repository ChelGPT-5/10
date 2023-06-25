class SuperStr(str):
    def is_repeatance(self, s):
        if not isinstance(s, str):
            raise TypeError("s - строка ")
        if len(s) == 0:
            return False
        return self == s * (len(self) // len(s))

    def is_palindrom(self):
        s = self.lower()
        return s == s[::-1]


s1 = SuperStr('abcabcabcabc')
print(s1.is_repeatance('abc'))
print(s1.is_repeatance('cba'))
s2 = SuperStr('level')
print(s2.is_palindrom())
s3 = SuperStr('Level')
print(s3.is_palindrom())
s4 = SuperStr('12321')
print(s4.is_palindrom())
s5 = SuperStr('')
print(s5.is_palindrom())
print(s5.is_repeatance('abc'))