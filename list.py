#week 5B


name.append(x)
name.extend()
name.pop()
name.index()
name.remove()
name.clear()
name.




>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.append('mango')
>>> fruits.extend('apple')
>>> fruits
['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'mango', 'a', 'p', 'p', 'l', 'e']
>>> fruits.clear()
>>> fruits
[]
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.count('banana')
2
>>> fruits.count('pear')
1
>>> fruits.index('orange')
6
>>> fruits.index('apple')
1
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
>>> fruits.pop()
'orange'
>>> fruits
['apple', 'apple', 'banana', 'banana', 'kiwi']
>>> fruits.remove('banana')
>>> fruits
['apple', 'apple', 'banana', 'kiwi']



>>> student
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko']
>>> student.append('Phyu Phyu')
>>> student.append('Ni Ni')
>>> student
['Mg Mg', 'Aye Aye', 'Mya Mya', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']
>>> student.remove('Mya Mya')
>>> student
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu', 'Ni Ni']
>>> student.pop()
'Ni Ni'
>>> student
['Mg Mg', 'Aye Aye', 'Ko Ko', 'Phyu Phyu']


>>> from collections import deque
>>> queue = deque(["Eric", "John", "Micheal"])
>>> queue.append("Trerry")
>>> queue.append("Graham")
>>> queue.popleft()
'Eric'
>>> queue
deque(['John', 'Micheal', 'Trerry', 'Graham'])

>>> cube = []
>>> for i in range(10):
...     cube.append(i**2)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>>
>>> for i in range(20):
...     cube.append(i**3)
...
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>>
>>> cube.clear()
>>> cube
[]
>>> cube = list(map(lambda x: x**2, range(10)))
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube = [x**2 for x in range(10)]
>>> cube
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

>>> [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>> [(x, y)
... for x in [1, 2, 3]
...     for y in [3, 1, 4]
...             if x != y
...             ]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
>>>
>>> combs = []
>>> for x in [1, 2, 3]:
...     for y in [3, 1, 4]:
...             if x != y:
...                     combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

>>> matrix = [
...     [1, 2, 3, 4, 5],
...     [6, 7, 8, 9, 10],
...     [11, 12, 13, 14, 15],
... ]
>>> transposed = []
>>> for i in range(4):
...     transposed_row = []
...     for row in matrix:
...             transposed_row.append(row[i])
...     transposed.append(transposed_row)
...
>>> transposed
[[1, 6, 11], [2, 7, 12], [3, 8, 13], [4, 9, 14]]

>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

>>> matrix = [
...     [1, 2, 3, 4, 5],
...     [6, 7, 8, 9, 10],
...     [11, 12, 13, 14, 15],
... ]
>>> list(zip(*matrix))
[(1, 6, 11), (2, 7, 12), (3, 8, 13), (4, 9, 14), (5, 10, 15)]