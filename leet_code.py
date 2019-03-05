#test

'''
### This file is used in conjucntion with Goodrich's Algorithms and Datastructures in Python Book ###

##### 1. Python basics #####

import sys
#print(sys.version_info[0:]) #prints the python verison

import numpy as np

# n1 = np.array([[1,2,3],[11,22,33]])
# print(n1)
# print(n1.shape)

# for i in n1:
#   print(i)


# a = [1,2,3,4,5]
# b = [11,22,33,44]
# print('zip')
# for i,j in zip(a,b):
#   print(i,j)

# print('enumerate')
# for i,j in enumerate(b):
#   print(i,j)

# print()
# a = np.random.rand(2,2)
# b = np.random.rand(2,2)
# c = np.random.rand(2,2)

# lst = [a,b,c]
# print(lst)

# np_lst = np.array(lst)
# print()
# print(np_lst.shape)
# print(np_lst)


"""
Multiline python comments
continue with line 2 etc
"""


import os
def inference(file_name):
    print(file_name + ' newstring')
    print(file_name.replace(os.path.basename(file_name), ''))


if __name__ == '__main__':
    infile = sys.argv[-1]
    inference(infile)

a = 'amitpatel'
print(a[0:2])

var1 = None
print(var1)


var1 = [1,2]
var2 = var1
var2.append(100) #this keeps the alias
print(var1)
var2 = [1,2,3,4,5] #breaks the alias
print(var1)

var1 = int(10) #using constructor form
print(var1)
var1 = 10 #using literal form (onlys works for builtin datatypes). Gives same result as above.

var1 = [1,2,3] #literal form
print(var1)
var2 = list([1,2,3]) #using constructor
print(var2)

var1 = bool()
print(var1)

var1 = 1
print(type(var1))
var1 = float(1)
print(type(var1))
var1 = 1.0
print(type(var1))

str1 = 'C:drive\\amit'
print(str1)

set1 = {}
print(type(set1))
set1 = set()
print(type(set1))

var1 = 1.0
var2 = var1
print(var1 is var2)
var2 = 1.0
print(var1 is var2)
print(var1 == var2)

# print('Enter a number')
# var1 = input() #sublime text doesn't support console input
# print(var1)

# Keyword argument #
def my_function(a=1,b=2,c=3):
    print(a,b,c)
    return None

my_function()
my_function(c=111,a=1212)
# Keyword argument #

# import pdb; pdb.set_trace() #python debugger


#Python Generators#
def factors(n): # generator that computes factors
    """ This is an example of a generator """
    for k in range(1,n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            yield k
            yield 0 #can have as many yields as we want to
    print(dir())

print(factors(10))
print(factors(10))\

for factor in factors(3):
    print(factor)
#Python Generators#

a,b,c,d = factors(3) #can do this for any iterable and generators are iterables
print(a,b,c,d)

# print()
# print(dir()) #lists all the identifiers i.e. object and function names (identifiers are like pointers in C++) in the current namespace
# print(vars())

print(help(factors)) #prints the docstring

#Args
def func1(*n):
    print(n)
    print(*n)

func1(1,2,3)
print(*[1,2,3])

##### 1. End of Python basics #####



##### 2. classes in python #####
"""
Members that are declared as protected are accessible to subclasses, but not to the general
public, while members that are declared as private are not accessible to either.

Python does not support formal access control like in C++/Java, but names beginning with a single
underscore are conventionally akin to protected, while names beginning with a
double underscore (other than special methods e.g. operator overloading, constructor etc) are akin to private. 

Note: unlike C++, python does not support multiple constructors (i.e. with different number of arguments)
But similar results can be achieved using keyword argument (i.e. using default values for different parameters) or using *args and **kwargs
"""

class Vector(object):
    """Represent a vector in a multidimensional space"""
    """ All the methods beginning and ending with __ are overloaded methods"""

    vector_type = 'Real Valued' #this is a class-level member

    def __init__(self, d):
        """Constructor. Create a d-dimensional vector of zeros"""
        self._coords = [0]*d

    def __len__(self):
        """Returns the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self,j):
        """Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self,j,val):
        """Set jth coordinate of vector to given value"""
        self._coords[j] = val

    def __add__(self,other):
        """Return sum of two vectors"""
        if(len(self) != len(other)): #relies on the __len__() method
            raise ValueError('Dimensions Must Agree!')
        result = Vector(len(self)) #start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result


    def print_coordinates(self):
        print('The Vector is :', self._coords, 'and it is of type: ', Vector.vector_type)


vec1 = Vector(3)
vec2 = Vector(3)

vec1.print_coordinates()
print(vec1[1])


for ii in vec1:
    print(ii)


myvar = 'aa', 'bb', 'cc'
print(myvar)

"""
#Multiple Inheritence in Python#
print('Example 0')
class First(object):
    def __init__(self,a):
        super(First,self).__init__()
        print('First', a)

class Second(First):
    def __init__(self):
        super(Second,self).__init__(10)
        print('Second')

fst = First(10)
snd = Second()

print('\nExample 1a')
class First(object):
    def __init__(self):
        super(First,self).__init__()
        print('First')

class Second(object):
    def __init__(self):
        super(Second,self).__init__()
        print('Second')

class Third(First,Second):
    def __init__(self):
        super(Third,self).__init__()
        print('Third')

print(Third.mro())
print(Third())

# Third.mro() = [Third,First,Second,Object]
# When doing Third() it does the following (according to Third.mro()) and note that it is a stack:
# 1. Go to Third.__init__()
# 2.            Once inside, go to First.__init__()
# 4.                once inside go to Second.__init__() when hit the line super(First,self).__init__() (accoridng to mro)
# 5.                    once inside, go to object.__init__()
# 6.                            There's nothing inside object.__init__()
# 7.                    continue with rest of Second.__init__() i.e. print 'Second'
# 8.                continue with rest of First.__init__() i.e. print 'First'
# 9.            continue with rest of Third.__init__() i.e. print 'Third'

print('\nExample 1b')
class First(object):
    def __init__(self):
        #super(First,self).__init__()
        object.__init__(self) #doesn't follow the mro
        print('First')

class Second(object):
    def __init__(self):
        super(Second,self).__init__()
        #object.__init__(self)
        print('Second')

class Third(First,Second):
    def __init__(self):
        #First.__init__(self)
        super(Third,self).__init__()
        print('Third')

print(Third.mro())
print(Third())

#Note: super() resolves the call using the mro (i.e. takes the next element from the mro list priorty) whereas using the name of the parent class does not use mro.

print('\nExample 1C')
class First(object):
    def __init__(self):
        print("first")
class Second(First):
    def __init__(self):
        print("Second")
class Third(object):
    def __init__(self):
        print("Third")
class Fourth(Second,Third):
    def __init__(self):
        super(Fourth,self).__init__()
        print('Fourth')

print(Fourth.mro())
print(Fourth())


print('\nExample 1D')
class First(object):
    def __init__(self):
        super(First,self).__init__()
        print("first")
class Second(object):
    def __init__(self):
        super(Second,self).__init__()
        #super(object,self).__init__() #same results as above
        #super().__init__() #same results as above
        print("Second")
class Third(First,Second):
    def __init__(self):
        super(Third,self).__init__()
        print('Third')

print(Third.mro())
print(Third())


print('\nExample 2')
class First(object):
    def __init__(self):
        super(First,self).__init__()
        print('First')

class Second(First):
    def __init__(self):
        super(Second,self).__init__()
        print('Second')

class Third(First):
    def __init__(self):
        super(Third,self).__init__()
        print('Third')

class Fourth(Second, Third):
    def __init__(self):
        super(Fourth,self).__init__()
        #Second.__init__(self) #to specifically use __init__ from Second class
        print('Fourth')



print(Second.mro())
test1 = Second()
print()
print(Third.mro())
test1 = Third()
print()
print(Fourth.mro())
test1 = Fourth()


print('\nExample 3')
class First(object):
    def __init__(self):
        super(First,self).__init__()
        print('First')

class Second(First):
    def __init__(self):
        super(Second,self).__init__()
        print('Second')

class Third(Second):
    def __init__(self):
        super(Third,self).__init__()
        print('Third')

class Fourth(First):
    def __init__(self):
        super(Fourth,self).__init__()
        print('Fourth')

class Fifth(Third,Fourth):
    def __init__(self):
        super(Fifth,self).__init__()
        print('Fifth')


#Note MRO doesn't depend on whether using super() inside the __init__ or not. It is purely based on class inheritence
#The MRO for Fifth will be:
#MRO = [Fifth,Third,Second,First,Object,Fourth,First,Object]
#But the common classes are done at the end (their priority is dictated by their last usage and so the middle ones are deleted)
#Thus MRO will be = [Fifth,Third,Second,Fourth,First,Object]

#MRO priority is:child,left,right,parent (in that order)

print(Second.mro())
print(Third.mro())
print(Fourth.mro())
print(Fifth.mro())
test1 = Fifth()

print('\nExample 4')
class First(object):
    def __init__(self):
        #super(First,self).__init__()
        print('First')

class Second(First):
    def __init__(self):
        #super(Second,self).__init__()
        print('Second')

# class Third(First,Second): #inconsistent and will trhow error
#   def __init__(self):
#       #super(Third,self).__init__()
#       print('Third')

class Third(Second,First):
    def __init__(self):
        #super(Third,self).__init__()
        print('Third')

print(Third.mro()) #will throw an error saying cannot create a consistent mro
#mro = [Third,First,Object,Second,First,Object]
#=> mro = [Third,Second,First,Object]\
#this is makes us use the right one before left one
#hence its inconsistent
#Note: class Third(Second,First) is consistent with mro = [Third,Second,First,Object]
"""

##### 2. End of classes in python #####


##### 3. Algorithm Analysis in Python #####

# Data structure is a systematic way of organizing and accessing data
# Algorithms is a step-by-stp procedure of performing some task

import time
t1 = time.time()
c1 = time.clock()

for i in range(10000):
    a = i*10

print(time.time()-t1)
print(time.clock()-c1)

num_square = 10
num_grains = 0
for i in range(num_square):
    num_grains += 2**i

print(num_grains)

#a program with run time of log(n)
def logn_prgm(n):
    i = n
    out = []
    out.append(i)
    while(i>=1):
        i = i//2
        out.append(i)
    return out
print(logn_prgm(9))


#a program with run time of nlog(n)
def nlogn_prgm(n):
    for i in range(n):
        print(logn_prgm(i))
nlogn_prgm(9)
##### 3. END of Algorithm Analysis in Python #####



##### 4. Recursions #####
#Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))


#binary search
def binary_search(data,target,low,high):
    """
    Binary Search Algorithm:
    Return True is target is found in indictated portion of a python list
    The search only considers the portion from data[low] to data[high] inclusive
    Low and high are indices
    Assumes data is a sorted Python list.
    """

    if low > high:
        return False #interval is empty. No match.
    else:
        mid = (low+high) // 2 #this will floor to the closest integer
        if target == data[mid]:
            return (True,mid)
        elif target < data[mid]:
            #recur on the portion left of the middle
            return binary_search(data,target,low,mid-1)
        else:
            #recur on the portion right of the middle
            return binary_search(data,target,mid+1,high)

print('Binary Search')
data = [2,4,7,11,22,24,26,29,31,33,36,38]
print(binary_search(data,24,0,len(data)-1))

#binary search version2
#a method to search for an element in a sorted list
import math
def find_element_in_sorted_list(lst, e, adj_factor=0):
    #searches in big O of log(n)

    mid = math.ceil(len(lst)/2)-1
    print(mid)
    if mid > 0:
        if lst[mid] < e:
            new_lst = lst[mid+1:]
            #print(new_lst)
            adj_factor += mid+1
            pos = find_element_in_sorted_list(new_lst,e,adj_factor)
        elif lst[mid] > e:
            new_lst = lst[0:mid+1]
            #print(new_lst)
            pos = find_element_in_sorted_list(new_lst,e,adj_factor)
        else:
            pos = mid+adj_factor

    else:
        if lst[mid] == e:
            pos = mid+adj_factor
        else:
            pos = None

    return pos
my_list = [i for i in range(16)] #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
print(find_element_in_sorted_list(my_list, 15)) 

def binary_search_ver3(nums, target):
    occr = []
    temp = nums[:]
    lo = 0
    hi = len(temp)-1
    while hi > lo:
        mid = (hi+lo)//2
        if target == temp[mid]:
            occr.append(mid)
            break          
        elif target < temp[mid]:
            hi = mid
        else: #target > temp[mid]
            lo = mid
    print(occr)

nums = [1,2,3,4,5,5,6,7,8]
binary_search_ver3(nums, 5)

def binary_search_continuous(array, val, stp, strt=0):
    mid_p = (stp+strt) // 2
    print(mid_p)
    if (array[mid_p-1] <= val <= array[mid_p]):
        return (mid_p-1, mid_p)
    elif (val < array[mid_p]):
        return binary_search_continuous(array, val, mid_p, 0)
    else: # (val > array[mid_p])
        return binary_search_continuous(array, val, len(array), mid_p)

array = [1,2,3,4,5]
print(binary_search_continuous(array, 1.5, len(array)))

#continuous binary search ver 2
def continous_var_binary_search(arr, n):
    left = 0
    right = len(arr)-1
    mid = (left+right)//2
    while True:
        if arr[mid] <= n <= arr[mid+1]:
            return mid
        elif arr[mid] < n:
            left = mid
            mid = (left+right)//2
        else:
            right = mid
            mid = (left+right)//2
print(continous_var_binary_search([1,2,3,4,5,6,7,9], 6.534))


# disk usage function
import os
path = './test.py'
path = 'C:\\Amit_Other\\test.py'
dir1 = './'
dir1 = 'C:\\Amit_Other\\'
file_name = 'junk.txt'
print(os.path.getsize(path)) #returns the immediate disk usage
print(os.path.getsize(dir1)) #returns the immediate disk usage
print(os.path.isdir(path)) #checks if its a directory
print(os.listdir(dir1)) #returns a list of all entities within a directory
print(os.path.join(dir1,file_name)) #/ for linux and \ for windows
print()

counter = 0
def disk_usage(path):
    """ Returns the number of bytes used by a file/folder and any descendents"""
    total = os.path.getsize(path) #account for direct usage
    if os.path.isdir(path): #Check is this is a directory
        for file_name in os.listdir(path): #then for each child
            global counter
            counter = counter + 1
            child_path = os.path.join(path,file_name) #compose full path to child
            total += disk_usage(child_path) #add child's usage to the total

    print('{0:<7}'.format(total),path, ' ', counter) #descriptive output
    return total

disk_usage(dir1)

# Infinite recursion
# def fib(n):
#   return fib(n)

# fib(3)

import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

# Tower of Hanoi Problem
# pseudo code for the recursive version
remove_disk(disk, source_tower, dest_tower, temp_tower):
    if disk == 0:
        return None
    else:
        remove_disk(disk-1, source_tower, dest_tower, temp_tower)
        move disk to dest_tower
        remove_disk(disk-1, temp_tower, dest_tower, source_tower)


# Recursive version (this is wrong)
data = [4,3,2,1]
temp_data = []
new_data = []

def remove_data(Dlist,output_data):
    output_data.append(Dlist.pop())
    if len(Dlist)==0:
        return None
    else:
        return remove_data(Dlist,output_data)

remove_data(data,temp_data)
print(temp_data)

remove_data(temp_data,new_data)
print(new_data)

# # non-recursive version (iterative version of Tower of Hanoi)
# data = [4,3,2,1]
# temp_data = []
# new_data = []

# for i in range(len(data)):
#   temp_data.append(data.pop())

# print(temp_data)

# for i in range(len(temp_data)):
#   new_data.append(temp_data.pop())

# print(new_data)

##### 4. END Recursions #####




##### 5. Array Based Sequences #####

import sys
import array

lst = ['a',1,None]

a1 = 1
print(sys.getsizeof(a1))
a1 = 1.0
print(sys.getsizeof(a1))
a1 = [1]
print(sys.getsizeof(a1))

a1 = array.array('i',[1])
print(sys.getsizeof(a1))

a1.append(2)
print(a1)
print()

# An experiment to explore the relationship between a list’s length and its underlying size in Python.
data_list = []
data_array = array.array('i',[])
# print(data_array, sys.getsizeof(data_array))
# data_array.append(1)
# print(data_array, sys.getsizeof(data_array))

n = 10
print('Int List')
for k in range(n):
    a = len(data_list)
    b = sys.getsizeof(data_list)
    print('Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))
    data_list.append(1) #b'cse lists are referential structures, the actual data_list type doesn't affect the getsieof(list) that much
    #data_list.append(1.0) #b'cse lists are referential structures, the actual data_list type doesn't affect the getsieof(list) that much
    #data_list.append(None) #b'cse lists are referential structures, the actual data_list type doesn't affect the getsieof(list) that much

print('Int Array')
for k in range(n):
    a = len(data_array)
    b = sys.getsizeof(data_array)
    print('Length: {0:3d}; Size in bytes: {1:4d}' .format(a, b))
    data_array.append(1)



import time
data = list(range(int(1e8)))
strt = time.time()
print(5 in data)
stp = time.time()
print(stp-strt)

print()
strt = time.time()
print(99999999 in data)
stp = time.time()
print(stp-strt)

print()
strt = time.time()
print(-5 in data)
stp = time.time()
print(stp-strt)



lst1 = [1,200,300,400]
lst2 = [11,22,1,2]
print(lst1 < lst2) #its lexicographic comparison


# List comprehension is faster
from time import time
n = int(1e7)
strt = time()
squares = [k*k for k in range(1,n+1)] #list comprehension
print(time()-strt)

strt = time()
squares = []
for k in range(1,n+1):
    squares.append(k*k)

print(time()-strt)



# Strings in python

class GameEntry(object):
    """Represents one entry of a list of high scores."""
    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._name

    def __str__(self):
        return '({0},{1})'.format(self._name, self._score) #e.g. '(Bob,98)'

player1 = GameEntry('Bob',98)
print(player1)


def insertion_sort(A):
    """sort list of comparable elements into nondecreasing order."""
    for k in range(1,len(A)):
        curr = A[k]
        j = k
        while (j > 0 and A[j-1] > curr):
            A[j] = A[j-1]
            j -= 1
        A[j] = curr

data = [1,6,2,4,5,9,3,1,3,2,15,19,11]
insertion_sort(data)
print(data)


#simple cryptograph
#print(''.join(['a','b','c']))
newstr = str(['a','b','c'])
print(type(newstr))
list_newstr = list(newstr)
print(type(list_newstr))

print(5%26)
print(-5%26)

def my_modulo(num1,num2):
    a = int(num1//num2) #floor operation
    return num1 - a*num2


print(5%6, -5%6)
print(my_modulo(5,6), my_modulo(-5,6))


# this works but it has reference/aliasing problem so don't initialize multi-dimensaional lists this way
print([[0]*3]*2)
print([1,2,3]*2)
print([[1,2,3]]*2)
print([[[1,2,3]]]*2)


#initializing multi-dimensional arrays

#approach 1
m = 3
n = 3
arr = []
for i in range(n):
    arr.append([0]*m)

arr[0][1] = 10
print(arr)

#approach 2 using list comprehension
arr = [[0]*m for j in range(n)]
arr[1][1] = 100
print(arr)


print(1); print(2)

# Tic-Tac-Toe example
class TicTacToe(object):
    """Management of a Tic-Tac-Toe game (does not do strategy)"""

    def __init__(self):
        """starrt a new game"""
        self._board = [[' ']*3 for i in range(3)]
        self._player = 'X'

    def mark(self,i,j):
        """ Put an X or O mark at position(i,j) for next player's turn"""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError('Invalid Board Position!')
        if self._board[i][j] != ' ':
            raise ValueError('Board Position Occupied')
        if self.winner() is not None:
            raise ValueError('Game is already complete')

        self._board[i][j] = self._player

        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'

    def _is_win(self,mark):
        """ check if the board configuration is a win for the given player"""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or #row 0
                mark == board[1][0] == board[1][1] == board[1][2] or #row 1
                mark == board[2][0] == board[2][1] == board[2][2] or #row 2
                mark == board[0][0] == board[1][0] == board[2][0] or #col 0
                mark == board[0][1] == board[1][1] == board[2][1] or #col 1
                mark == board[0][2] == board[1][2] == board[2][2] or #col 0
                mark == board[0][0] == board[1][1] == board[2][1] or #diagonal
                mark == board[0][2] == board[1][1] == board[2][0]) #reverse diagonal

    def winner(self):
        """Return mark of winning player, or None to indicate a tie."""
        for mark in 'XO':
            if self._is_win(mark):
                return mark

        return None

    def __str__(self):
        """Return string representation of current game board"""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n-------\n'.join(rows)

my_game = TicTacToe()
print(my_game)
my_game.mark(0,0)
my_game.mark(1,1)
my_game.mark(0,1)
my_game.mark(0,2)
my_game.mark(2,2)
print(my_game)


##### 5. END Array Based Sequences #####

##### 6. Stacks, Queues, Double-Ended Queues #####

# Creating a stack class #
class Empty(Exception):
    """Error attempting to access an element from an empty container.
    This is a subclass based upon Python's Exception class.
    It is used in the stack class definition below"""
    pass


class ArrayStack(object):
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """create an empty stack"""
        self._data = [] #non public list instance

    def __len__(self):
        """Return number of elements in the stack. Don't raise exception even if its empty."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty"""
        return len(self) == 0 #note this is same as len(self._data) due to the __len() function

    def push(self,e):
        """Add element e to the top of the stack"""
        self._data.append(e) #new item stored at the end of the list

    def top(self):
        """Return (but do not remove) the element at the top of the stack
        Raise Exception if the stack is empty"""
        if len(self) == 0:
            raise Empty('Stack is empty')
        return self._data[-1]


    def pop(self):
        """Remove and return the element from the top of the stack (LIFO"""
        if len(self) == 0:
            raise Empty('Stack is empty')
        return self._data.pop()

    def __str__(self):
        """Used when priting a stack """
        return self._data.__str__()


# S = ArrayStack()
# S.push(5)
# S.push(3)
# print(len(S))
# print(S.pop())
# print(S.is_empty())


# str1 = 'amitisanalogdesigner\n'
# print(str1.rstrip('\n'))

def transfer(S,T):
    """Transfers all the contents from stack S to T 
    and T will have its contents in reverse order compared to S"""
    while S.is_empty() == False:
        T.push(S.pop())

S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)

print(S)
ArrayStack.pop(S) #this is same as S.pop()
print(S)

T = ArrayStack()
transfer(S,T)
print(S)
print(T)

S = T
print(S)
T = None
print(S)
print(T)

# Reversing the contents of a file
def reverse_file(filename):
    """Overwrite a given file with its contents line-by-line reverse"""
    S = ArrayStack()

    #read the contents of the file
    original = open(filename)
    for line in original:
        S.push(line.rstrip('\n')) #we will reinsert new lines when writing back tot he file
    original.close()

    #new we overwrite the contents in LIFO order
    output = open(filename, 'w') #reopening file overwite original
    while not S.is_empty():
        output.write(S.pop() + '\n') #reinsert newline characters
    output.close()

#reverse_file('./dummy.txt')


# Implementation of a Queue
class ArrayQueue(object):
    """FIFO queue implementation using a python list as underlying storage."""
    DEFAULT_CAPACITY = 3 #moderate capacity for all new queues

    def __init__(self):
        """create an empty queue"""
        self._size = 0
        self._front = 0
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY #self.DEFAULT_CAPACITY
        #print(self.DEFAULT_CAPACITY, 'yes')
        #print(ArrayQueue.DEFAULT_CAPACITY,'yes')

    def __len__(self):
        """Return the number of element in the queue."""
        return self._size #note it is NOT len(self._data)

    def is_empty(self):
        """Return true if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('The queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (FIFO)"""

        if self.is_empty():
            raise Empty('The Queue is empty')

        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        #shrink the underlying array if need be
        if(0 < self._size < len(self._data)//4):
            self._resize(len(self._data)//2)

        return answer

    def enqueue(self,e):
        """Add an element at the back of the queue"""
        #expand the underlying array if need be
        if self._size == len(self._data):
            self._resize(2*self._size) #double the array size
        pos = (self._front + self._size) % len(self._data)
        self._data[pos] = e
        self._size += 1

    def _resize(self,cap):
        """Resize to a new list of capacity >= len(self) """
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            pos = (walk + i) % len(old)
            self._data[i] = old[pos]
        self._front = 0

    def __str__(self):
        """used with the print function"""
        temp = []
        walk = self._front
        for i in range(self._size):
            pos = (walk + i) % len(self._data)
            temp.append(self._data[pos])
        return str(temp)

print('Queue section')
q1 = ArrayQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print(len(q1._data))
q1.enqueue(11)
print(len(q1._data))
q1.enqueue(21)
q1.enqueue(31)
q1.enqueue(31)
q1.enqueue(31)
q1.enqueue(31)
q1.enqueue(31)
print(len(q1._data))

q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(len(q1._data))
q1.dequeue()
q1.dequeue()
print(len(q1._data))
q1.dequeue()


print(q1)

q2 = ArrayQueue()
q2.enqueue(10)

print(q1.DEFAULT_CAPACITY, 'q1')
print(ArrayQueue.DEFAULT_CAPACITY, 'class')
q1.DEFAULT_CAPACITY = 5
print(q1.DEFAULT_CAPACITY, 'q1')
print(q2.DEFAULT_CAPACITY, 'q2')
print(ArrayQueue.DEFAULT_CAPACITY, 'class')


import collections
a = collections.deque() #python standard deque
print(type(a))


##### 6. END Stacks, Queues, Double-Ended Queues #####



##### 7. Linked Lists #####

""" With singly linked lists, it is efficient to insert or remove an element from the head as well as insert an element at the tail. Removing an element at the tail is not efficient. 

1. Stack: Therefore, to implement a stack (where a new element is added to the top of the stack as well as an element is removedf rom the top of the stack), it is efficient to implement a linked list stack by inserting and removing elements from the head of the linked list.

2. Queue: (where a new element is added at the back of the queue and an element is removed from the front of the queue). To implement a queue using linked list, we remove an element from the head of the queue and insert a new element to the tail of the queue.

"""
class Empty(Exception):
    """Error attempting to access an element from an empty container.
    This is a subclass based upon Python's Exception class.
    It is used in the stack class definition below"""
    pass

class LinkedStack(object):
    """LIFO Stack implementation using a singly linked list for storage"""

    #-----------------nested _Node class ---------------------------
    class _Node(object):
        """ Lightweight non-public class for storing a singly linked node."""
        __slot__ = '_element', '_next' #streamline memory usage

        def __init__(self,element,next):
            #initialize node's fields
            self._element = element
            self._next = next

    #------------------ stack methods -------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head = None #reference to the head
        self._size = 0 #number of stack elements

    def __len__(self):
        """return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return True is the stack is empty."""
        return len(self) == 0

    def push(self,e):
        """Add an element to the top of the stack."""
        # Note: class variables/objects/methods can be accessed by self.method_name() or class_name.method()
        # But a particular (i.e. instance specific) version of a class variable needs to be accessed only using self.class_variable_name
        self._head = self._Node(e,self._head) #Create and link a new node
        self._size += 1

    def top(self):
        """Return but do not remove the element at the top of the stack.
        Raise an Empty exception is stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is Empty')
        else:
            return self._head._element

    def pop(self):
        """Remove and return the element at the top of the stack.
        Raise empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        else:
            element_to_return = self._head._element
            self._head = self._head._next
            self._size -= 1

            return element_to_return

    def __str__(self):
        """used for pritning the stack"""
        str_list = [] #more efficient to fill a list and then convert to string as string object is immutable.
        curr_node = self._head
        for i in range(len(self)):
            str_list.append(curr_node._element)
            curr_node = curr_node._next
        return str(str_list)


# stk1 = LinkedStack()
# stk1.push(1)
# stk1.push(10)
# stk1.push('aaa')
# print(stk1)

# stk1.pop()
# print(stk1)
# stk1.pop()
# stk1.pop()
# print(stk1)


class LinkedQueue(object):
    """FIFO queue implementation using a singly linked list for storage."""

    #-----------------nested _Node class ---------------------------
    class _Node(object):
        """ Lightweight non-public class for storing a singly linked node."""
        __slot__ = '_element', '_next' #streamline memory usage

        def __init__(self,element,next):
            #initialize node's fields
            self._element = element
            self._next = next

    #------------------ queue methods -------------------------------

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0 #number of queue elements

    def __len__(self):
        """Returns the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return true if the queue is empty."""
        return len(self) == 0

    def first(self):
        """Return (but not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty('The queue is empty')

        else:
            return self._head._element #front or the queue is aligned with the head of the linked list

    def dequeue(self):
        """Remove and return the first element (from front of the queue) from the queue (i.e. FIFO)
        Raise Empty exception if the queue is empty
        """
        if self.is_empty():
            raise Empty('The queue is empty')

        answer = self._head._element
        self._head = self._head._next
        self._size -= 1

        if self.is_empty(): #special case is queue is empty
            self._tail = None #removed head had been the tail node

        return answer

    def enqueue(self,e):
        """Add an element to the back of the queue."""
        new_node = self._Node(e,None)
        curr_tail_node = self._tail
        if self.is_empty():
            self._head = new_node #special case when previously empty
        else:
            curr_tail_node._next = new_node     
        self._tail = new_node #update reference to tail node
        self._size += 1

    def __str__(self):
        """used for pritning the stack"""
        str_list = [] #more efficient to fill a list and then convert to string as string object is immutable.
        curr_node = self._head
        for i in range(len(self)):
            str_list.append(curr_node._element)
            curr_node = curr_node._next
        return str(str_list)

q1 = LinkedQueue()
print(q1)
q1.enqueue(1)
q1.enqueue(10)
q1.enqueue('abc')
print(q1)
q1.dequeue()
q1.dequeue()
print(q1)

##########
class CircularQueue(object):
    ###THIS IS INCOMPLETE. SO WON'T WORK!!!
    """Queue implementation using circularly linked list for storage."""

    #-----------------nested _Node class ---------------------------
    class _Node(object):
        """ Lightweight non-public class for storing a singly linked node."""
        __slot__ = '_element', '_next' #streamline memory usage

        def __init__(self,element,next):
            #initialize node's fields
            self._element = element
            self._next = next

    #------------------ queue methods -------------------------------

    def __init__(self):
        """Create an empty queue."""
        self._tail = None #will represent tail of queue
        self._size = 0 #number of queue elements

    def __len__(self):
        """return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """ Return True if the queue is empty."""
        return len(self) == 0

    def first(self):
        """Return but do not remove the element at the front of the queue.
        Raise Error exception if the queue is empty."""

        if self.is_empty():
            raise Empty('Queue is empty')

        head = self._tail._next
        return head._element

    def dequeue(self):
        """Remove the first element of the queue (i.e. FIFO).
        Raise exception if the queue is empty. """

        if self.is_empty():
            raise Empty('Queue is empty')

        old_head = self._tail._next
        if len(self) == 1:
            self._tail = None
        else:
            self._tail = old_head
        self._size -= 1

        return old_head._element


    def enqueue(self,e):
        """add an element to the back of the queue."""
        if self.is_empty():
            newest = self._Node(e,None)
            self._tail = newest
        else:
            old_head = self._tail._next
            newest = self._Node(e,old_head)
            self._tail = newest
        self._size += 1

##########

#Doubly Linked List
class _DoublyLinkedBased(object):
    """A base class providing a double linked list representation.
    Using sentinels (i.e. header and trailer nodes) simplifies the insertion/deletion logic"""

    class _Node(object):
        """Lightweight nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next' #streamline memory

        def __init__(self,element,prev,next): #initialize node's fields
            self._element = element #user's element
            self._prev = prev #previous node reference
            self._next = next #next node reference

    def __init__(self):
        """create and empty list"""
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer #trailer is after header
        self._trailer._prev = self._header #header is before trailer
        self._size = 0 #number of elements in the list

    def __len__(self):
        """return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Returns Trues if the list is empty."""
        return len(self)==0

    def _insert_between(self,e,predecessor,successor):
        """Add element e between two existing nodes and return the new node."""
        newest = self._Node(e,predecessor,successor) #linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        """Delete nonsentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        answer = node._element
        node._prev = node._next = node._element = None #deprecate node (helps Python's garbage collector)

        return node._element #return deleted node

    def __str__(self):
        """used by the print method."""
        lst_str = []
        curr = self._header._next
        for i in range(len(self)):
            lst_str.append(curr._element)
            curr = curr._next
        return str(lst_str)



# Deque implementation using doubly linked list
# Using sentinels (i.e. header and trailer nodes) really simplifies the insertion/deletion logic
class LinkedDeque(_DoublyLinkedBased): #Note the use of inheritence
    """Double-ended queue implementation based ona doubly linked list.

    The following methods are not modified (i.e. we use the inherited methods):
    __init__(), __len__(), is_empty(), __str__()

    """

    # def __init__(self):
    #   super().__init__()

    def first(self):
        """Return but do not remove the elment at the front of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._header._next._element #real item is just after header node

    def last(self):
        """Return but do not remove the element at the back of the deque."""
        if self.is_empty():
            raise Empty('Deque is empty')
        return self._trailer._prev._element #real item is just before trailer node

    def insert_first(self,e):
        """Add an element at the front of the deque."""
        self._insert_between(e,self._header,self._header._next) #add after header node

    def insert_last(self,e):
        """Add an element to the back of the deque."""
        self._insert_between(e,self._trailer._prev,self._trailer) #add before trailer node

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise empty exception if the Deque is empty."""
        if is_empty(self):
            raise Empty('Deque is empty')
        return self._delete_node(self._header._next) #use inherited method

    def delete_last(self):
        """Remove and return the element from the end of the deque.
        Raise empty exception if the deque is empty."""
        if is_empty(self):
            raise Empty('Deque is empty')
        return self._delete_node(self._trailer._prev) #use inherited method


print('\nDeque Section\n')
deq1 = LinkedDeque()
deq1.insert_first(1)
deq1.insert_first('abc')
deq1.insert_last(2)
print(deq1)

deq2 = LinkedDeque()
deq2.insert_first(1)
deq2.insert_first('abc')
deq2.insert_last(2)
print(deq2)
print(deq1 is deq2)
deq3 = deq1
print(deq1 is deq3)



# Positional list
class PositionalList(_DoublyLinkedBased):
    """A sequential container of elements allowing positional access."""

    #---------------- nested Position class -------------------------
    class Position(object):
        """ An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """ Constructor should note be invoked by the user."""
            self._container = container
            self._node = node #node is of the type _DoublyLinkedBased._node


        def element(self):
            """ Return the element stored at this position. """
            return self._node._element

        def __eq__(self,other):
            """ Return True if other is a position representing th same location. """
            return type(self) == type(other) and other._node is self._node

        def __ne__(self,other):
            """ Return True if other does not represent the same location."""
            return not(self.__eq__(other))

    #----------------- Utility method ---------------------------
    def _validate(self,p):
        """ Return position's node or raise appropriate error is invalid."""
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if not (p._container is self):
            raise ValueError('p does not belog to this container')
        if p._node._next is None: #convention for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self,node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None #boundary violation
        else:
            return self.Position(self,node) #legitimate position


    #----------------------- accessors ------------------------------------
    def first(self):
        """ Return the first position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)

    def last(self):
        """ Return the last position in the list (or None if the list is empty)"""
        return self._make_position(self._trailer._prev)

    def before(self,p):
        """ Return the position just after the position p or None if p is last """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self,p):
        """ Return the position just before the position p or None if p is the first """
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """ Generate a forward iteration of the elements of the lists."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #----------------------- mutators ------------------------------------
    #override inherited verison to return Position rather than Node
    def _insert_between(self,e,predecessor,successor):
        """ add element between existing nodes and return new position."""
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)

    def add_first(self,e):
        """ Insert element e at the front of the list and return new Position. """
        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):
        """ Insert element e at the back of the list and return new Posiiton."""
        return self._insert_between(e,self._trailer._prev,self._trailer)

    def add_before(self,p,e):
        """ Insert element e into list before Position p and return new Position."""
        original = self._validate(p) #to make sure p is a valid position
        return self._insert_between(e,original._prev,original)

    def add_after(self,p,e):
        """ Insert element e into list after Position p and return new Position."""
        original = self._validate(p) #to make sure p is a valid position
        return self._insert_between(e,original,original._next)

    def delete(self,p):
        """ Remove and return the element at Position p."""
        original = self._validate(p) #to make sure p is a valid position
        return self._delete_node(original) #inherited method returns the element

    def replace(self,p,e):
        """ Replace the element at Position p eith e."""
        original = self._validate(p) #to make sure p is a valid position
        old_value = original._element
        original._element = e
        return old_value

print('\nPositional List:\n')
pl1 = PositionalList()
pl1.add_first(10)
pl1.add_first(1)
print(pl1)

pos1 = pl1.first()
pl1.add_before(pos1,11)
print(pl1)

#test the iterator method
for a in pl1:
    print(a)

def my_insertion_sort(lst):
    for i in range(1,len(lst)):
        curr_val = lst[i]
        j = i
        while curr_val < lst[j-1] and j >= 1:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = curr_val
    return lst

a = [1,2,3,2,1,5,9]
print(my_insertion_sort(a))

#SORT POSITIONAL LIST#
def PL_Insertion_Sort(PL):
    """Sort PositionalList PL of comparable elements into nondecreasing order."""
    cursor = PL.first() #this is really the first element
    for i in range(len(PL)):

        curr_val = cursor.element()
        prev_cursor = PL.before(cursor)
        while prev_cursor != None and curr_val < prev_cursor.element():
            PL.replace(PL.after(prev_cursor), prev_cursor.element())
            prev_cursor = PL.before(prev_cursor)

        if prev_cursor == None:
            pos = PL.first()
        else:
            pos = PL.after(prev_cursor)
        PL.replace(pos, curr_val)
        cursor = PL.after(cursor)

    return PL

print('\nPositional List Sort')
print(pl1)

# pos = pl1.first()
# print(pos.element())
# pos = pl1.after(pos)
# print(pos.element())
# pos = pl1.after(pos)
# print(pos.element())

print(PL_Insertion_Sort(pl1))


#Favorites List
class FavoritesList(object):
    """List of elements ordered from most frequently accessed to least.
    The elements are of type _Item() """
    #---------------------- nested _Item class ----------------------------
    class _Item(object):
        __slots__ = '_value', '_count' #streamline memory usage

        def __init__(self,e):
            self._value = e #the user's element
            self._count = 0

    #------------------------- nonpublic utilities --------------------------
    def _find_position(self,e):
        """ Search for element e and return its Position (or None if not found)."""
        walk = self._data.first()

        while (walk != None and walk.element()._value != e):
            walk = self._data.after(walk)
        return walk

    def _move_up(self,p): #this is pretty much implementing insertion sort algorithm
        """Move item at Position p earlier in the list based on access count."""
        if p != self._data.first(): #consider moving if not the first element
            cnt = p.element()._count
            walk = self._data.before(p)
            if cnt > walk.element()._count: #must shift forward
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p)) #delete/insert

    #-------------- public methods ----------------------------------------
    def __init__(self):
        """create an empty list of favorites."""
        self._data = PositionalList() #will be list of _Item instances

    def __len__(self):
        """ Return number of entries on favorites list."""
        return len(self._data)

    def is_empty(self):
        """ Return True if list is empty."""
        return len(self) == 0

    def access(self,e):
        """ Access element e, thereby increasing tis access count."""
        p = self._find_position(e) #try to locate existing element
        if p == None:
            p = self._data.add_last(self._Item(e)) #if new, place at the end
        p.element()._count += 1 #always increment the counter
        self._move_up(p) #consider moving forward

    def remove(self,e):
        """ Remove element e from list of favorites."""
        p = self._find_position(e) #try to located existing element
        if p is not None:
            self._data.delete(p) #delete if found


    def top(self,k):
        """ Generate sequence of top k elements in terms of access count."""
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element() #element of list is _Item
            yield item._value   #report user's element
            walk = self._data.after(walk)



fav1 = FavoritesList()
fav1.access('Maharaj')
fav1.access('Maharaj')
fav1.access('Swami')
fav1.access('Swami')
fav1.access('Santo')
fav1.access('Santo')

print(len(fav1))


for fav in fav1.top(len(fav1)):
    print(fav)

##### 7. END Linked Lists #####


##### 8. Trees #####

#print(dir())
#print(vars())

class Tree(object):
    """Abstarct base class representing a tree structure."""

    #--------------- nested Position class -----------------
    class Position(object):
        """An abstarction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self,other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self,other):
            """Return True if other does not represnet the same location."""
            raise NotImplementedError('must be implemented by subclass')

    #----------- abstract methods that concrete subclass must support ------------
    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self,p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self,p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self,p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    #----------concrete methods implemented in this class----------------
    def is_root(self,p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self,p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self,p):
        """Return the number of levels separating Position p from the root."""
        """This is a recursive implementation of depth.
        1. If p is the root, then the depth of p is 0.
        2. Otherwise, the depth of p is one plus the depth of the parent of p.
        """
        if self.is_root(p):
            depth = 0
        else:
            depth = 1 + self.depth(self.parent(p))
        return depth

    def _height(self,p):
        """Returns the height of the subtree rooted at Position p."""
        """Recursively implemented as :
        1. if p is a leaf, then height of p is 0
        2. otherwise, height of p is one more than the maximum of the heights of p's children.
        """
        if self.is_leaf():
            height = 0
        else:
            height = 1 + max(self._height(c) for c in self.children(p)) #using generator comprehension syntax

            """ Alternative implementation.
            h_max_child = 0  #initialization
            max_child = 0 #initialization (not necessary)
            for child in self.children(p):
                h_child = self._height1(child)
                if h_child > h_max_child:
                    h_max_child = h_child
                    max_child = child #(not necessary)
            height = 1 + h_max_child
            """

        return height

    def height(self,p=None):
        """Return the height of the subtree rooted at Position p.
        if p is None, return the height of the entire tree."""

        if p is None:
            p = self.root()
        return self._height(p) #start _height() recursion

#print(Tree.__init__) #since constructor is not defined, inherits one from the base object class
#print(Tree.root)

class BinaryTree(Tree):
    """Abstarct Base Class representing a binary tree structure."""

    #------------- additional abstract methods--------------------
    def left(self,p):
        """Return a Position representing p's left child.
        Return None if p does not have a left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self,p):
        """Return a Position representing p's right child.
        Return None if p does not have a right child.
        """
        raise NotImplementedError('must be implemented by subclass')

    #-------- concrete methods implemented in this class ---------------
    def sibling(self,p):
        """Return a posiiton representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None: #p must be the root
            return None #root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent) #possibly None
            else:
                return self.left(parent) #possibly None

    def children(self,p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node(object):
        """lightweight nonpublic class for storing a node"""
        #__slots__ = '_element', '_parent', '_left', '_right' #for memory efficieny
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstarction representing the location of a single element."""
        def __init__(self, container, node):
            """ constructor should not be invoked by the user."""
            self._container = container #tells us which instance of LinkedBinaryTree does the given node belog to
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element

        def __eq__(self,other):
            """Return True if other is a Position representing the same location."""
            #uses the __eq__ method from the inherited object class for _Node class 
            #whereas for Position class, it has already been defined in the BinaryTree.Position class and thus needs to be explicitly implement (see abstarct base class for Tree)
            return type(other) == type(self) and other._node == self._node

    def _validate(self,p):
        """Return associated node, if Position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node: #convention for deprecated nodes
            raise ValueError('p is no longer valid')

        return p._node
    
    def _make_position(self,node):
        """Return Posiiton instance for given node (or None if no node)."""
        return self.position(self, node) if node is not None else None

    #------------------ binary tree constructor ----------------------------
    def __init__(self):
        """create an initially empty binary tree."""
        self._root  = None
        self._size = 0

    #------------------ public accessors -----------------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self,p):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)



lbt1 = LinkedBinaryTree()
N1 = lbt1._Node(10)
P1 = lbt1.Position(999,N1)
N2 = lbt1._Node(10)
P2 = lbt1.Position(999,N2)

print(N1 == N2)
print(N1 == N1)
print(P1 == P2)
print(P1 == P1)

aa = LinkedBinaryTree._Node(1)
print(aa)

#Note: chapter 8 is not completed. Will have to complete in the future.
'''

print('here')


'''

def func2(b):
    """this is func2 help"""
    return b+1

help(func2)

def func1(a):
    print('FUNC1')
    return func2

# def func1(a):
#     print('FUNC1BBBB')
#     return func2

m1 = func1(3)

print(m1(10))

m2 = func2
print(m2(10))



class dummy(object):

    def func1d(self, a):
        return a

    @staticmethod
    def func2d(a):
        #return func1d(a) #this fails
        return a

    def func3d(self, a):
        return self.func2d(a)
    
a = dummy()
print(a.func2d(1))
print(a.func2d)
print(a.__dict__)
a.var1 = 10
print(a.__dict__)
print(dummy.__dict__)

class my_namespace(object):
    """docstring for my_namespace"""
    v1 = 1
    v2 = 2

    @staticmethod
    def my_f1(a):
        return 2*a

    @staticmethod
    def my_f2(a):
        return my_namespace.my_f1(a/2)

mnsp1 = my_namespace()
print(mnsp1.my_f1(2))
print(mnsp1.my_f2(2))
print(mnsp1.__dict__)
print(my_namespace.__dict__)
        


"""VERY INTERESTING BEHAVIOR OF PYTHON COMPARED TO OTHER LANGUAGES"""
a = [1,2,3]
def func1(v):
    v = a
    return v

v_ = func1(a)
print(v_)
a[0] = 111
print(a)
print(v_) #'v_' is modified too as it's just a pointer to 'a' (even though func1() was not called again)

"""
//CPP VERSION OF THIS FOR COMPARISON
//Test CPP
#include <iostream>
#include <vector>
using namespace std;



vector <int> func1(vector <int> g)
{
    vector <int> rg;
    rg = g;
    return rg;
}


int main()
{
    cout << "CPP Playground:\n";
    
    //create a list
    vector <int> lst1; //lst1 = {1,2,3};
    lst1.push_back(1);
    lst1.push_back(2);
    lst1.push_back(3);
    
    vector <int> lst2;
    lst2 = func1(lst1);
    cout << lst2[0] << ' ' << lst2[1] << ' ' << lst2[2] << '\n';
    lst1[1] = 111;
    cout << lst2[0] << ' ' << lst2[1] << ' ' << lst2[2] << '\n';

    
    return 0;
}
//END CPP VERSION OF THIS FOR COMPARISON
"""

"""/END VERY INTERESTING BEHAVIOR OF PYTHON COMPARED TO OTHER LANGUAGES"""
"""


##############################################################



# sequence vs collection data types: 
# sequence data types are ordered e.g. list, stack etc (elements can be accessed in a particular ordder)
# collections data type are unordered and can have duplicate
# set data type is also unordered (if the hash function is unknown) but it has no duplicates
# set datatype is essentially a subset of the collections datatype.





"""
General Python

def myLog(n, b=2):
    """    Using binary search to efficiently (approximately) compute the value of any monotonic function whose value is less than its input
    Can use this same approad for square root, log, etc
    """
    left = 0
    right = n
    mid = (left+right)//2
    while True:
        print(mid)
        if 2**mid <= n <= 2**(mid+0.3):
            return mid
        elif 2**mid < n:
            left = mid
            mid = (left+right)//2
        else:
            right = mid
            mid = (left+right)//2


import math
print(myLog(32), math.log(32,2))


"""

'''
