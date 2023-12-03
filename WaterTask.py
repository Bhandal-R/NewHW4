import sys
import random

def water(lst, taps):
    """
    Fills water bottles with the tap pressure 100ml per second.
 
    Args:
    lst: Array of integars representing the people and their water bottle.
    taps: Amount of taps available.
 
    Returns:
        Integar: An integar which shows the total seconds to fill all water bottles.
    """

    # validation
    if not isinstance(taps, int):
        print("Please enter an integer for taps")
        sys.exit(1)

    if not isinstance(lst, list):
        print("Please enter a valid list")
        sys.exit(1)

    if all(type(e) == int for e in lst) == False:
        print("Please enter a list containing integars only")
        sys.exit(1)

    if len(lst) == 0:
        print("Please enter a list")
        sys.exit(1)

    if taps <= 0:
        print("Please enter a tap value greater than 0")
        sys.exit(1)

    # one tap / more taps to people calculation
    if taps >= len(lst):
        return (max(lst)/100)
    elif taps == 1:
        return sum(lst)/100

    queue = []
    timer = 0
    # assigns people to taps
    while len(lst) > 0:
        if len(queue) < taps:
            queue.append(lst.pop(0))
            if len(lst) != 0:
                continue
        
        # get smallest watter bottle value
        val = queue.pop(queue.index(min(queue)))

        # add time it takes to fill
        timer += (val / 100)

        # remove the value from others 
        queue = [x - val for x in queue]

        # remaining sec added
        if len(lst) == 0:
            timer+=(max(queue)/100)


    return print("Total seconds:",timer)

# water([450,750,1000],2)

def water(lst, taps, extraSec):
    """
    Alternative version which takes in the extra seconds to walk to the tap.
 
    Args:
    lst: Array of integars representing the people and their water bottle.
    taps: Amount of taps available.
    extraSec: Fixed time it takes for people to walk to the taps.
 
    Returns:
        Integar: An integar which shows the total seconds to fill all water bottles including extraSec.
    """

    # validation
    if not isinstance(taps, int):
        print("Please enter an integer for taps")
        sys.exit(1)

    if not isinstance(lst, list):
        print("Please enter a valid list")
        sys.exit(1)

    if all(type(e) == int for e in lst) == False:
        print("Please enter a list containing integars only")
        sys.exit(1)

    if len(lst) == 0:
        print("Please enter a list")
        sys.exit(1)

    if taps <= 0:
        print("Please enter a tap value greater than 0")
        sys.exit(1)

    # one tap / more taps to people calculation
    if taps >= len(lst):
        return (max(lst)/100)
    elif taps == 1:
        return (sum(lst)/100)+(len(lst)*extraSec)

    queue = []
    timer = 0
    # assigns people to taps
    while len(lst) > 0:
        if len(queue) < taps:
            queue.append(lst.pop(0))
            if len(lst) != 0:
                continue

        # get smallest watter bottle value
        val = queue.pop(queue.index(min(queue)))

        # add time it takes to fill
        timer += (val / 100)
        timer+=extraSec

        # remove the value from others 
        queue = [x - val for x in queue]

        # remaining sec added
        if len(lst) == 0:
            timer+=(max(queue)/100)
            timer+=extraSec

    return print("Total seconds:",timer)


# water([450,750,1000,400],2,2)

def water(lst, taps):
    """
    Modified version which takes in the different pressure taps.
 
    Args:
    lst: Array of integars representing the people and their water bottle.
    taps: Amount of taps available.
 
    Returns:
        Integar: An integar which shows the total seconds to fill all water bottles.
    """
    # validation
    if not isinstance(taps, int):
        print("Please enter an integer for taps")
        sys.exit(1)

    if not isinstance(lst, list):
        print("Please enter a valid list")
        sys.exit(1)

    if all(type(e) == int for e in lst) == False:
        print("Please enter a list containing integars only")
        sys.exit(1)

    if len(lst) == 0:
        print("Please enter a list")
        sys.exit(1)

    if taps <= 0:
        print("Please enter a tap value greater than 0")
        sys.exit(1)

    # random tap pressures
    flow_rate = [0] * taps

    for i in range(taps):
        flow_rate[i] = 50 * random.randint(1, 20)
    
    print("Tap pressure:"," ".join([str(x)+"ml" for x in flow_rate]))

    # one tap calculation
    if taps == 1:
        return sum(lst)/flow_rate[0]

    # assigns people to taps
    if len(lst)>=taps:
        queue = lst[:taps]
        lst = lst[taps:]
    else:
        queue = lst
        queue = (queue + taps * [0])[:taps]
        lst = []

    timer = 0

    while sum(queue) > 0:

        for i in range(taps):
            # fills based on pressure
            queue[i]-=flow_rate[i]
            # second added once all taps threshold
            if i+1 == taps:
                timer+=1
            # assigns next in line
            if queue[i]<=0:
                if len(lst) != 0:
                    queue[i] = lst.pop(0)
                else:
                    queue[i] = 0
        continue


    return print("Total seconds:",timer)

# water([450,750,1000],2)

def water(lst, taps):
    """
    Precision version with different pressure taps
    (This version calculates the time precisely).
 
    Args:
    lst: Array of integars representing the people and their water bottle.
    taps: Amount of taps available.
 
    Returns:
        Integar: An integar which shows the total seconds to fill all water bottles.
    """
    # validation
    if not isinstance(taps, int):
        print("Please enter an integer for taps")
        sys.exit(1)

    if not isinstance(lst, list):
        print("Please enter a valid list")
        sys.exit(1)

    if all(type(e) == int for e in lst) == False:
        print("Please enter a list containing integars only")
        sys.exit(1)

    if len(lst) == 0:
        print("Please enter a list")
        sys.exit(1)

    if taps <= 0:
        print("Please enter a tap value greater than 0")
        sys.exit(1)

    # random tap pressures
    flow_rate = [0] * taps

    for i in range(taps):
        flow_rate[i] = 50 * random.randint(1, 20)
    
    print("Tap pressure:"," ".join([str(x)+"ml" for x in flow_rate]))
    
    # one tap calculation
    if taps == 1:
        return sum(lst)/flow_rate[0]

    # assigns people to taps
    if len(lst)>=taps:
        queue = lst[:taps]
        lst = lst[taps:]
    else:
        queue = lst
        queue = (queue + taps * [0])[:taps]
        lst = []

    # calculates time to complete filling
    def diff(queue,tap):
        diff = []
        diff = [0] * len(queue)
        for i in range(len(queue)):
            diff[i] = queue[i] / tap[i]
            if diff[i] == 0:
                diff[i] = 10000
        return diff
    
    timer = float(0)

    while sum(queue) > 0:
        difference = diff(queue,flow_rate)
        smallest = min(difference)
        for i in range(len(queue)):
            switch = 0
            # removes/changes quickest filling bottle
            if difference.index(smallest) == i:
                if len(lst) != 0:
                    queue[i] = lst.pop(0)
                    switch+=1
                else:
                    queue[i] = 0

            # removes difference from numbers in queue
            if queue[i] != 0 and switch == 0:
                queue[i] = queue[i] - (flow_rate[i]*smallest)
        timer+=smallest
        continue
    return print("Total seconds:",round(timer, 2))

# water([450,700,1000,400],2)

def water(lst, taps, pressure):
    """
    Shows time taken to fill water bottles with different pressures
    (This is purely used to show higher pressure = lower time).
 
    Args:
    lst: Array of integars representing the people and their water bottle.
    taps: Amount of taps available.
 
    Returns:
        Integar: An integar which shows the total seconds to fill all water bottles.
    """

    # validation
    if not isinstance(taps, int):
        print("Please enter an integer for taps")
        sys.exit(1)

    if not isinstance(lst, list):
        print("Please enter a valid list")
        sys.exit(1)

    if all(type(e) == int for e in lst) == False:
        print("Please enter a list containing integars only")
        sys.exit(1)

    if len(lst) == 0:
        print("Please enter a list")
        sys.exit(1)

    if taps <= 0:
        print("Please enter a tap value greater than 0")
        sys.exit(1)

    # 1 tap calculation
    if taps == 1:
        return sum(lst)/pressure[0]

    # assigns people to taps
    if len(lst)>=taps:
        queue = lst[:taps]
        lst = lst[taps:]
    else:
        queue = lst
        queue = (queue + taps * [0])[:taps]
        lst = []

    timer = 0

    while sum(queue) > 0:

        for i in range(taps):
            # fills based on pressure
            queue[i]-=pressure[i]
            # second added once all taps threshold
            if i+1 == taps:
                timer+=1

            # assigns next in line
            if queue[i]<=0:
                if len(lst) != 0:
                    queue[i] = lst.pop(0)
                else:
                    queue[i] = 0
        continue


    return print("Total seconds:",timer)

# low pressure

# water([400,600,800],3,[200,300,200])

# higher pressure

# water([400,600,800],3,[200,300,400])
