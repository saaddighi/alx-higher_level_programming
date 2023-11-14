l = []
for i in range(0, 100):
    if i < 10:
        i = f'0{i}'
    
    l.append(i)
l = ', '.join(map(str, l))
print('{}'.format((l)))
