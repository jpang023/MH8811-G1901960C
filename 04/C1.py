min = None
for i in [9,41,12,3,74,15]:
    print(i)
    if min is None:
        min=i
    elif i < min:
        min = i
print(min)
        