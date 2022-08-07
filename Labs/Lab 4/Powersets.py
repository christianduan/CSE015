elements = ()
sets = set([])
state = False
element = list(elements)

while True:
    a = input('Enter one more element? [Y/N]: ')

    if a.capitalize() == "Y":
        state = True
    if a.capitalize() == "N":
        state = False
        break
    if state:
        x = int(input('Enter the new element in the set: '))
        element.append(x)

elements = tuple(element)
for x in elements:
    sets.add(x)

b = 0
c = 1
d = 0

while(b < len(elements)):
    for x in elements [c:len(elements)]:
        temp = (elements[d], x)
        sets.add(temp)

    b = b + 1
    c = c + 1
    d = d + 1

sets.add(elements)

print(sets)