s = """We are not what we should be!
     We are not what we need to be.
     But at least we are not what we used to be"""
z = s.split()
s = []
for word in z:
    a = word.strip('.!')
    s.append(a)
print(len(z))
print(s)
print(sorted(s, key=str.lower))





