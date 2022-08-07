from logic import TruthTable

var = input("Write an logical expression:" )

myTable = TruthTable([var])
a = myTable.table
myTable.display()
print(a)
print('\n')
total = 0
for item in a:
    b = item[1][0]
    if (b == 1):
        total = total + 1

if (total == len(a)):
    print(var + ' is a tautology.')
elif total == 0:
    print(var + ' is a contradiction')
else:
    print(var + ' is a contingency.')
