from logic import TruthTable

myTable = TruthTable(['p', 'q'], ['((p -> q) and p) -> q'])
myTable.display()
myTable.latex()

myTable = TruthTable(['p', 'q'], ['(-q and (p -> q)) -> -p'])
myTable.display()

myTable = TruthTable(['p', 'q', 'r'], ['((p -> q) and (q -> r)) -> (p -> r)'])
myTable.display()

myTable = TruthTable(['p', 'q'], ['((p or q) and -p) -> q'])
myTable.display()

myTable = TruthTable(['p', 'q'], ['p -> (p or q)'])
myTable.display()

myTable = TruthTable(['p', 'q'], ['(p and q) -> p'])
myTable.display()

myTable = TruthTable(['p', 'q'], ['((p) and (q)) -> (p and q)'])
myTable.display()

myTable = TruthTable(['p', 'q', 'r'], ['((p or q) and (-p or r)) -> (q or r)'])
myTable.display()
