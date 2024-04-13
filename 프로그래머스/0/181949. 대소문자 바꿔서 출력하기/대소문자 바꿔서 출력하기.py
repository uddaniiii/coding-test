str = input()
str= "".join(s.lower() if s.isupper() else s.upper() for s in str )
print(str)