from elections import *
import outputtypes as out
from typing import Callable

def elections(algorithm: Callable, input, combinedTuples, outtype: out.OutputType):
    """
    Gets an algrithm (callable), input(str or list(Party)), combinedTuples(list(tuple)) and outtype
    1.Handles the different kinds of inputs, 
    2.Performs the algorithm according to the requested algorithm
    3.Handles the output according to the requested output
    """

    """1. Handles the input:"""
    if isinstance(input, str):
        parties = initializePartiesFromFile(input)
    else:
        parties = input
    # create combinedParties for agreed upon deals according to a list of tuples (combinedTuples)
    if combinedTuples:
        usedIndex = list()
        combinedParties = list()
        for tuple in combinedTuples:
            party = parties[tuple[0]]
            usedIndex.append(tuple[0])
            for i in tuple[1:]:
                party += parties[i]
                usedIndex.append(i)
            combinedParties.append(party)
        for index, party in enumerate(parties):
            if index not in usedIndex:
                combinedParties.append(party)
    else:
        combinedParties = parties

    """2. Performs the algorithm:"""
    # allocate seats and return the amount of allocated seats    
    allocatedSeats = electionsAlgorithm(parties=combinedParties)
    # For each unallocated seats, run an algorithm to allocate the seats according to a method functuin
    apportionmentAlgorithm(start=allocatedSeats, end=120, methodFunction=algorithm, parties=combinedParties)
    # for each combined party, divide the seats according to the same algorithm we used for all the parties together
    for party in combinedParties:
        if party.originalParties is not None:
            newPartyList = list(party.originalParties)
            a = electionsAlgorithm(parties=newPartyList, seats=party.newSeats)
            apportionmentAlgorithm(start=a, end=party.newSeats, methodFunction=algorithm, parties=newPartyList)
    
    """3. Handle the output according to request"""
    return outtype.extract_output_from_calculated_list(parties)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    parties = elections(jeffersonsF, 'results.csv', [(0,2),(1,3),(4,5)], outtype=out.shortCsvOutput)
    parties = elections(webstersF, [Party("ot1", 200, 0), Party("ot2", 400, 0), Party("ot3", 150, 0), Party("ot4", 1000, 0)], None, outtype=out.shortPrintedOutput)
