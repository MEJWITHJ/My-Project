from LinkedStack import LinkedStack
from PositionalList import PositionalList
from ExpressionEvaluator import infixToPostfix
def bubble_sort(L):
    n = len(L)
    for i in range(n):
        swapped = False
        current = L.first()
        for j in range(n - i - 1):
            next = L.after(current)
            if current.element() > next.element():
                a = next.element()
                b = current.element()
                L.replace(current, a)
                L.replace(next, b)
                swapped = True
            current = next
        if not swapped:
            break
def insertion_sort(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value > marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
'''
 insertion_sort(P)
 print("The sorted list of elements are: ")
 # Print the sorted elements
 for x in P:
     print(x)
'''
def insertion_sort_descending(L):
    '''Sort the Positional List of comparable elements into non decreasing order.'''
    if len(L) > 1: #otherwise, no need to sort it
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)#next item to place
            value = pivot.element()
            if value < marker.element():#pivot is already sorted
                marker = pivot#pivot becomes new marker
            else:#must relocate pivot
                walk = marker#find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)#remove pivot
                L.add_before(walk, value)#insert pivot
'''
insertion_sort_descending(P)
print("The sorted list of elements are: ")
# Print the sorted elements
for x in P:
    print(x)
'''


#1

#2
s = PositionalList()
s.add_first(1)
s.add_first(72)
s.add_first(81)
s.add_first(25)
s.add_first(65)
s.add_first(91)
s.add_first(11)
print("Not sorted list: ")
for x in s:
    print(x)

insertion_sort(s)
print("The sorted list of elements are:(Ascending) ")
# Print the sorted elements
for x in s:
    print(x)
insertion_sort_descending(s)
print("The sorted list of elements are:(Descending) ")
# Print the sorted elements
for x in s:
    print(x)
