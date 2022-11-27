class bounded_subsets:
    """
    This class creates an iterator that iterates over all the subsets of a given list, where the sum of the subset is less than a given sum. 
    >>> for i in bounded_subsets([0, 1, 2], 2): print(i, end="")
    [][0][1][1, 0][2][2, 0]

    >>> for i in bounded_subsets([0, 1, 2], 3): print(i, end="")
    [][0][1][1, 0][2][2, 0][2, 1][2, 1, 0]

    >>> for i in bounded_subsets([1, 2, 3], 4): print(i, end="")
    [][1][2][2, 1][3][3, 1]

    >>> for i in bounded_subsets(range(10, 13), 22): print(i, end="")
    [][10][11][12][11, 10][12, 10]
    """
    def __init__(self, s, c: float) -> None:
        self.lenS = len(s)
        self.s = list(s)
        self.c = c
        self.currSum = 0 # the "counter" of the iterator, once currSum == c we stop the iteration
        self.currResults = [] # used to save every result

        self.s.sort() # put zeros infront
        self.zeroIncluded = 0 in self.s # used in subsetSum() to append zeros to every result if needed

    def __iter__(self):
        return self

    def __next__(self):
        print(self.currResults)
        # if self.currResults is not empty, than we are still iterating through the results of the last subsetSum
        if len(self.currResults) != 0:
            return self.currResults.pop()

        # while the currSum of the subsets is less than the const self.c we were given
        while self.currSum <= self.c:
            if self.subsetSum(self.lenS-1, self.currSum):
                self.currSum += 1
                return self.currResults.pop()
            self.currSum += 1
        # stop iteration if the currSum is greater than self.c
        raise StopIteration
    
    def subsetSum(self, currentItem, sum, res=[]):
        """
        Solves the subset sub problem recursivly. 
        Gets an array, it's length-1, and a sum (for the subset sum problem)
        Returns true or false, if one of the paths in the tree (recursion) is true, then appends the result into self.currResults.
        >>> bounded_subsets([1,2,3], 4).subsetSum(2, 4)
        True
        >>> bounded_subsets([1,2,3], 4).subsetSum(2, 7)
        False
        """
        # if sum == 0 append the result and return true to stop recursion
        if sum == 0:
            if self.zeroIncluded:
               self.currResults.append(res+[0])
            self.currResults.append(res)
            return True
        # if we are out of items or sum is negative return false because current branch of recursion can't solve the problem
        if currentItem < 0 or sum < 0:
            return False
    
        # take the current item
        takeCurrentItem = self.subsetSum(currentItem - 1, sum - self.s[currentItem], res+[self.s[currentItem]])
        # dont take current item
        dontTakeCurrentItem = self.subsetSum(currentItem - 1, sum, res)
    
        return takeCurrentItem or dontTakeCurrentItem


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    print("\n---bounded_subsets([1,0,2,3], 4)---")
    for s in bounded_subsets([1,0,2,3], 4):
        print("|",s," sum:", sum(s), end=" ")

    print("\n\n---bounded_subsets(range(50,150), 103)---")

    for s in bounded_subsets(range(50,150), 103):
        print("|",s," sum:", sum(s), end=" ")

    print("\n\n---bounded_subsets(range(100), 1000000000000)---")
    for s in zip(range(5), bounded_subsets(range(100), 1000000000000)):
        print("|",s," sum:(s[1]):", sum(s[1]),end=" \n")