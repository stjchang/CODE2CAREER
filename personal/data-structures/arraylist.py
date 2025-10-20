import numpy as np

class ArrayList(list):
    """ Array List
    
    This class implements a List ADT using numpy.
    
    Attributes
    ----------
    _length : int
        The length of the array that implements the list.
    _vector : numpy array
        Array used to implement the list.
    _size : int
        Number of elements in the list.
        
    Improvements that could be made:
    
    1. Implementing resizing the array during appends and inserts where size == length (length * 2)
    2. shrinking array 
    
    """
    
    def __init__(self, length):
            self._length = length
            self._size = 0 # number of elements in the list
            self._vector = np.empty(length, dtype=object)
            
    def __len__(self):
        return self._size
    
    def __str__(self):
        if self._size == 0: print("[]")
        else:
            result = "["
            for i in range(0, self._size-1):
                result += (str(self._vector[i]) + ", ")
            result += str(self._vector[self._size - 1] + "]")
            
        return result
    
    # return element at a given position after checking valid index
    def get(self, index):
        if index >= 0 and index < self._size:
            return self._vector[index]
        raise IndexError(f"index: {index} out of range")
    
    # find the index of a given element or we get to the end of the list
    # returns index of element or -1
    def search(self, x):
        if self._size == 0:
            raise IndexError("Empty list")
        else:
            for i in range(0, self._size):
                if self._vector[i] == x:
                    return i
            return -1
        
        
    # shift all elements to the right of index by 1 using a backwards loop
    def insert(self, index, x):
        if index >= 0 and index < self._size:
            if self._size == len(self._vector):
                raise IndexError("List is full")
            else:
                for i in range(self._size, index - 1, -1):
                    self._vector[i+1] = self._vector[i]
                    
                self.vector[index] = x
                self._size += 1
        else:
            raise IndexError(f"Index {index} out of bounds")
        
    def append(self, x):
        if self._size == self._length:
            raise IndexError("list is full")
        else:
            self._vector[self._size] = x
            self._size += 1
        
    def remove_by_index(self, index):
        # check if index is valid
        if index >= 0 and index < self._size:
            if self._size == 0:
                raise IndexError("Empty list")
            else:
                for i in range(index, self._size - 1):
                    self._vector[i] = self._vector[i + 1]
                
                self._vector[index] = None
                self._size -= 1
        else: 
            raise IndexError(f"Index {index} out of bounds")
        
    def remove_by_value(self, x):
        index = self.search(x)

        if index == -1:
            raise KeyError(f"Element {x} is not in the list")
        else:
            self.remove_by_index(index)
        
    # sets all elements to Null
    def clean(self):
        for i in self._vector:
            i = None
    
        self._size = 0

        
    # checks if list is empty
    def empty(self):
        return self._size == 0