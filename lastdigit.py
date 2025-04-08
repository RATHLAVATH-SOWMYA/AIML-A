x=12345
for i in [1,2]:
    r=x%10
    x=int(x/10)
    print(r)

x=-12386
x=-x
print("last digits is ",str(x%100))

x=12.345
print(type(x))
y=str(x)
print(type(y))
print(y[-2:])
print(x)
print(y)
