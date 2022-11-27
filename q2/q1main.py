from elections import *

def elections(algorithm: callable, input, combinedTuples,outtype):
    if isinstance(input, str):
        parties = initializePartiesFromFile(input)
    else:
        parties = input
    
    j=1-0.959369642829895 # f(s) = s+1-j
    # if j == 0:
    #     print("jeffersons f(s) = s +", str(1-j))
    # elif j == 0.5:
    #     print("websters f(s) = s +", str(1-j))
    # else:
    #     print("calculating for f(s) = s +", str(1-j))

    # create combinedParties for agreed upon deals between parties prior to elections: (hardcoded)
    if combinedTuples:
        combinedParties = list()
        combinedParties.append(parties[0]+parties[2]) # likud + bengvir
        combinedParties.append(parties[1]+parties[3]) # yesh atid + ganz
        combinedParties.append(parties[4]+parties[5]) # shas + tora
        combinedParties.append(parties[6])
        combinedParties.append(parties[7])
        combinedParties.append(parties[8])
        combinedParties.append(parties[9])
        #combinedParties.append(parties[9]+parties[10]) # mrz + ha'avoda
    else:
        combinedParties = parties

    # First, allocate seats and return the amount of allocated seats    
    allocatedSeats = electionsAlgorithm(parties=combinedParties)

    # For each unallocated seats, run an algorithm to allocate the seats according to a method functuin
    apportionmentAlgorithm(start=allocatedSeats, end=120, methodFunction=algorithm, parties=combinedParties, y=j)

    # for each combined party, divide the seats according to the same algorithm we used for all the parties together
    for party in combinedParties:
        if party.originalParties is not None:
            newPartyList = list(party.originalParties)
            a = electionsAlgorithm(parties=newPartyList, seats=party.newSeats)
            apportionmentAlgorithm(start=a, end=party.newSeats, methodFunction=algorithm, parties=newPartyList,y=j)
    
    return parties

parties = elections(webstersF, 'results.csv', None, None)
#parties = elections(webstersF, [Party("ot1", 200, 0), Party("ot2", 400, 0), Party("ot3", 150, 0), Party("ot4", 1000, 0)], None, None)
print("\t"+"          ", "\t| S E A T S |")
print("\t"+"party name", "\t","new","\t", "IRL")
for party in parties:
    print("\t"+party.name, "\t",party.newSeats,"\t", party.seats)