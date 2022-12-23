result = []
def divider(a, b):
 if a < b:
    raise ValueError
 if b > 100:
    raise IndexError
 return a / b
data = {10: 2, 2: 5, 123: 4, 18: 0, 9: 15, 8: 4}
try:
 for key in data:
  res = divider(key, data[key])
except:
 result.append(res)
print(result)
