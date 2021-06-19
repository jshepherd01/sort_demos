from os import stat
from utilities import *
from random import shuffle, randint

# sorting algorithms

# each algo will have 4-5 functions: Init, Inner, Outer, End, Display
# each one has three control signals (return values): 0 (run 'End'), 1 (run 'Inner'), 2 (run 'Outer')
# Init and End don't return anything. Init should set state, End should unset it (state = {})
# Inner, Outer and End should always be run with **state as their arguments
# Display should take the current state and print a coloured representation of it to the terminal

# Selection Sort

def selectionInit(alist):
    print(bannerText('SELECTION SORT', '#'))
    print("Performing selection sort on list:")
    print(prettyList(alist, []))
    global state
    state = {
        "alg": "sel",
        "alist": alist,
        "i": 0,
        "j": 0,
        "k": 0,
        "code": 1,
        "timer": 0,
    }
    print("(s)tep for inner loop.")
    print("(n)ext for outer loop.")
    print("(r)un to skip to end.")

def selectionInner(alg, alist, i, j, k, code, timer):
    if alist[k] < alist[j]:
        j = k
    k += 1

    global state
    state['j'] = j
    state['k'] = k
    if k == len(alist):
        state['code'] = 2
    else:
        state['code'] = 1
    state['timer'] += 1

def selectionOuter(alg, alist, i, j, k, code, timer):
    temp = alist[j]
    alist[j] = alist[i]
    alist[i] = temp
    i += 1
    j = i
    k = i

    global state
    state['alist'] = alist
    state['i'] = i
    state['j'] = j
    state['k'] = k
    if i == len(alist):
        state['code'] = 0
    else:
        state['code'] = 1

def selectionEnd(alg, alist, i, j, k, code, timer):
    print(bannerText("FINISHED", '#'))
    print("...after",timer,"comparisons")
    print(prettyList(alist,['c']*len(alist)))
    global state
    state = {}

def selectionDisplay(alg, alist, i, j, k, code, timer):
    coloursList = ['c']*i + [None]*(len(alist)-i)
    if i-1 >= 0:
        coloursList[i-1] = 'b'
    if i < len(alist):
        coloursList[i] = 'r'
    if j < len(alist):
        coloursList[j] = 'g'
    if k < len(alist):
        coloursList[k] = 'y'

    print(prettyList(alist, coloursList))

# Insertion Sort

def insertionInit(alist):
    print(bannerText('INSERTION SORT', '#'))
    print("Performing insertion sort on list:")
    print(prettyList(alist, []))
    if len(alist) == 1:
        code = 0
    else:
        code = 1
    global state
    state = {
        "alg": "ins",
        "alist": alist,
        "i": 1,
        "j": 1,
        "code": code,
        "timer": 0,
    }
    print("(s)tep for inner loop.")
    print("(n)ext for outer loop.")
    print("(r)un to skip to end.")

def insertionInner(alg, alist, i, j, code, timer):
    if alist[j-1] > alist[j]:
        temp = alist[j]
        alist[j] = alist[j-1]
        alist[j-1] = temp
        j -= 1
        code = 1
    else:
        code = 2
    if j == 0:
        code = 2
    
    global state
    state['alist'] = alist
    state['j'] = j
    state['code'] = code
    state['timer'] += 1

def insertionOuter(alg, alist, i, j, code, timer):
    i += 1
    j = i

    global state
    state['i'] = i
    state['j'] = j
    if i == len(alist):
        state['code'] = 0
    else:
        state['code'] = 1

def insertionEnd(alg, alist, i, j, code, timer):
    print(bannerText("FINISHED", '#'))
    print("...after",timer,"comparisons")
    print(prettyList(alist,['c']*len(alist)))
    global state
    state = {}

def insertionDisplay(alg, alist, i, j, code, timer):
    coloursList = ['c']*i + [None]*(len(alist)-i)
    if j != i:
        coloursList[i] = 'c'
    if j >= 0 and j < len(alist):
        if code == 2:
            coloursList[j] = 'g'
        elif code == 1:
            coloursList[j] = 'y'

    print(prettyList(alist, coloursList))

# Bubble Sort

# Bogo Sort

# Monkey Sort

# Quick Sort

# Merge Sort

# Bucket Sort

# Radix Sort

# Heap Sort


# data functions

def dataShuffle(n):
    out = list(range(1,n+1))
    shuffle(out)
    return out

def dataRand(n):
    out = [randint(1,100) for i in range(n)]
    return out

def dataOrder(n):
    out = list(range(1,n+1))
    return out

def dataReverse(n):
    out = list(range(1,n+1))
    return out[::-1]

def dataLit(alist):
    return alist[:]

def dataNand(n):
    out = [randint(1,10) for i in range(n)]
    return out

# validation/conversion functions

def isPositiveInteger(n):
    return (type(n) == int or (type(n) == str and n.isnumeric())) and int(n)>=1

# globals/initialisation

init = {
    'sel': selectionInit,
    'ins': insertionInit,
}

step = {
    'sel': selectionInner,
    'ins': insertionInner,
}

next = {
    'sel': selectionOuter,
    'ins': insertionOuter,
}

end = {
    'sel': selectionEnd,
    'ins': insertionEnd,
}

display = {
    'sel': selectionDisplay,
    'ins': insertionDisplay,
}

datafuncs = {
    'shuffle': [dataShuffle, isPositiveInteger, int],
    'rand': [dataRand, isPositiveInteger, int],
    'order': [dataOrder, isPositiveInteger, int],
    'reverse': [dataReverse, isPositiveInteger, int],
    'lit': [dataLit, lambda *n: all(isPositiveInteger(i) for i in n), lambda *n: [int(i) for i in n]],
    'nand': [dataNand, isPositiveInteger, int],
}

prevcmd = ""
datafunc = dataShuffle
datafuncargs = 5

state = {}

#
#   Main Loop
#

while True:
    args = input(">>> ").lower().split()
    if len(args) == 0:
        cmd = prevcmd
        if cmd == "":
            print(errorText("No command specified."))
            continue
    else:
        cmd = args.pop(0)
    prevcmd = ""

#
#   (h)elp
#

    if cmd == "h" or cmd == "help":
        print(bannerText("HELP",'#'))
        print("\t(h)elp: displays this message.")
        print("\t(r)un ALG: run the specified sorting algorithm. Only the first three characters of ALG need to be specified.")
        print("\t\tIf an algorithm is already running, skips to the end of that algorithm and shows the result.")
        print("\t\tCurrently supported algorithms are:")
        print("\t\t - Selection Sort")
        print("\t\t - Insertion Sort")
        print()
        print("\t(s)tep: move to the next step of the inner loop.")
        print("\t(n)ext: move to the next step of the outer loop, stepping over the inner loop.")
        print("\t(q)uit: stop executing the current algorithm. If no algorithm is running, exit the program.")
        print()
        print("\t(d)ata: specify the data to be passed to the next algorithm.")
        print("\t\trand N: a list of N random numbers, between 1 and 100.")
        print("\t\tnand N: a list of N random numbers, between 1 and 10.")
        print("\t\tshuffle N: the numbers 1-N in a random order.")
        print("\t\torder N: the numbers 1-N in order.")
        print("\t\treverse N: the numbers 1-N in reverse order.")
        print("\t\tlit A [B ...]: the list given, in the order it is given.")

#
#   (r)un
#

    elif cmd == "r" or cmd == "run":
        if 'alg' in state:
            while state['code'] != 0:
                if state['code'] == 1:
                    step[state['alg']](**state)
                elif state['code'] == 2:
                    display[state['alg']](**state)
                    next[state['alg']](**state)
            end[state['alg']](**state)
        else:
            if len(args) == 0:
                print(errorText("No algorithm specified."))
                continue
            if args[0][:3] not in init:
                print(errorText("Algorithm not found."))
                continue
            init[args[0][:3]](datafunc(datafuncargs))
            display[state['alg']](**state)

#
#   (s)tep
#

    elif cmd == "s" or cmd == "step":
        if 'alg' in state:
            if state['code'] == 1:
                step[state['alg']](**state)
                display[state['alg']](**state)
                prevcmd = "s"
            elif state['code'] == 2:
                next[state['alg']](**state)
                display[state['alg']](**state)
                prevcmd = "s"
            elif state['code'] == 0:
                end[state['alg']](**state)
                prevcmd = ""
        else:
            print(errorText("No algorithm running."))
            continue

#
#   (n)ext
#

    elif cmd == "n" or cmd == "next":
        if 'alg' in state:
            if state['code'] == 2:
                next[state['alg']](**state)
            while state['code'] == 1:
                step[state['alg']](**state)
            if state['code'] == 0:
                end[state['alg']](**state)
                prevcmd = ""
            else:
                display[state['alg']](**state)
                next[state['alg']](**state)
                prevcmd = "n"
        else:
            print(errorText("No algorithm running."))
            continue

#
#   (d)ata
#

    elif cmd == "d" or cmd == "data":
        if len(args) == 0:
            print(errorText("No data specified."))
            continue
        if len(args) == 1:
            print(errorText("No argument specified."))
            continue
        if args[0] not in datafuncs:
            print(errorText("Data type not found."))
            continue

        record = datafuncs[args[0]]

        try:
            if record[1](*args[1:]):
                datafunc = record[0]
                datafuncargs = record[2](*args[1:])
                print("Data type set.")
            else:
                print(errorText("Argument not valid."))
                continue
        except TypeError:
            print(errorText('Argument not valid.'))
            continue

#
#   (q)uit
#

    elif cmd == "q" or cmd == "quit":
        if 'alg' in state:
            state = {}
            print(bannerText("ALGORITHM ABORTED", '#'))
        else:
            exit()

    else:
        print(errorText('Command not recognised'))
