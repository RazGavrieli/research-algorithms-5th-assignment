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
        self.currSum = 0
        self.currResults = []

        self.s.sort() # put zeros infront
        self.zeroIncluded = 0 in self.s




    def __iter__(self):
        return self

    def __next__(self):
        if len(self.currResults) != 0:
            return self.currResults.pop()

        while self.currSum <= self.c:
            if self.subsetSum(self.lenS-1, self.currSum):
                self.currSum += 1
                return self.currResults.pop()
            self.currSum += 1
        raise StopIteration
        

    def subsetSum(self, n, sum, res=[]):
        """
        Sovles the subset sub problem recursivly. 
        Gets an array, it's length-1, and a sum (for the subset sum problem)
        Returns true or false, if one of the paths in the tree (recursion) is true, then appends the result into self.currResults.
        >>> bounded_subsets([1,2,3], 4).subsetSum(2, 4)
        True
        >>> bounded_subsets([1,2,3], 4).subsetSum(2, 7)
        False
        """
        # return true if the sum becomes 0 (subset found)
        if sum == 0:
            if self.zeroIncluded:
               self.currResults.append(res+[0])
            self.currResults.append(res)
            return True

        # base case: no items left, or sum becomes negative
        if n < 0 or sum < 0:
            return False
    
        # Case 1. Include the current item `arr[n]` in the subset and recur
        # for the remaining items `n-1` with the remaining total `sum-arr[n]`
        include = self.subsetSum(n - 1, sum - self.s[n], res+[self.s[n]])
    
        # Case 2. Exclude the current item `arr[n]` from the subset and recur for
        # the remaining items `n-1`
        exclude = self.subsetSum(n - 1, sum, res)
    
        # return true if we can get subset by including or excluding the
        # current item
        return include or exclude



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # for s in bounded_subsets([1,0,2,3], 4):
    #     print(s, sum(s))

    # print("-----")

    # for s in bounded_subsets(range(50,150), 103):
    #     print(s, sum(s), end="\n")


    # print("-----")
    # for t in zip(range(5), bounded_subsets(range(100), 1000000000000)):
    #     print(t)