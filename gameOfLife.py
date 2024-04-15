"""
Author contact information:
Name: Liam Guetg

Features:
(1) The Program runs a text based version of Conway's "Game of Life".
(2) How the application works:
    (2.1) Begins with a "starting world" that is specified by the user.
    (2.2) Each turn, the birth and death rules are applied to get the resulting "New world"
    (2.3) After each turn the "old world" (the BEFORE) and the "New world" (the AFTER) are displayed.
(3) The birth and death rules are as follows:
    (3.1) If a square is empty then it will remain empty unless exactly 3 of the surrounding squares are occupied by
    a critter, then a "birth" will occur there; and a critter will appear in that square.
    (3.2) If a square has a critter and less than two of the surrounding squares have a critter, then the critter will
    "die" of loneliness; and be replaced for an empty square.
    (3.3) If a square has a critter and exactly 3 of the surrounding squares have a critter, then the critter will
    "live"; and remain as is.
    (3.4) If a square has a critter and more than 3 of the surrounding squares have a critter, then the critter will
    "die" of overpopulation; and be replaced for an empty square.

(4) The program will accept any text file starting pattern that contains spaces that are either empty (" ") or have
a critter ("*"), so long as the "world" forms a rectangle.
(5) This program has thee de-bugging flags:
    (5.1) 'deBugSurroundingEachPos' shows the immediately surrounding positions for each spot on the map.
    (5.2) 'deBugSurroundingList' displays the 2D list that shows the number of surrounding critters each position has.
    (5.3) 'deBugShowStartingWorld' shows the starting world and number of columns and rows, to ensure the world was
    properly loaded.

Limitations:
(1) The program cannot suggest an appropriate file if the entered file is invalid or empty.
(2) This program will only work for file with the appropriate format (square or rectangle)
(3) The program is text based and as a result a graphical interface is not available, making navigating the program
more difficult.
"""

deBugSurroundingEachPos = False
deBugShowStartingWorld = False
deBugShowWorldChange = False
deBugSurroundingList = False
CRITTER = "*"
EMPTY = " "
NOTHING = ""
NEW_LINE = "\n"


# Function: startingWorldOptions
# @ startingWorldOptions(list)
# @ return(list, int, int)
# Features:
# (1) This function prompts user for to chose if they either want to use a default starting world or input their
# own starting world file
def startingWorldOptions(world):
    choice = -1
    inputAccepted = False

    while (inputAccepted == False):
        print("Starting World options:\n\t(1) Chose a default starting World\n\t(2) Upload a starting world")
        choice = int(input("Enter your choice: "))
        if (choice == 1):
            world, numRows, numColumns = choseStatingWorld(world)
            inputAccepted = True
        elif (choice == 2):
            world, numRows, numColumns = inputStartingWorld(world)
            inputAccepted = True
        else:
            print("\n\x1B[3mError:\x1B[0m Please choose either '1' or '2'\n")

    if deBugShowStartingWorld == True:
        print("\nStarting World:")
        for r in range(0, numRows, 1):
            print(world[r])
        print("Number of rows = %d \nNumber of Columns = %d" % (numRows, numColumns))

    return (world, numRows, numColumns)


# Function: choseStartingWorld
# @ choseStartingWorld(list)
# @ return(list, int, int)
# Features:
# (1) This function prompts user to chose one of the pre-made starting Worlds
# (2) Once chosen the 2D list 'world' and its dimensions are returned to the call function.
def choseStatingWorld(world):
    starting_world = -1
    inputAccepted = False

    while (inputAccepted == False):
        print("\nChoices for starting biospheres:\n\t"
              "(0) Return to previous Menu\n\t(1) Empty\n\t"
              "(2) Single critter\n\t(3) Single birth\n\t"
              "(4) Simple birth\n\t(5) Edge testing\n\t"
              "(6) It's a complex world\n\t(7) Even more complex world")
        startingWorldInt = int(input("Enter your choice: "))

        if (startingWorldInt == 0):
            print("\n")
            startingWorldOptions(world)

        elif (startingWorldInt in range(1, 8, 1)):
            if (startingWorldInt == 1):
                from startingPatterns import emptyWorld
                world = emptyWorld()
            elif (startingWorldInt == 2):
                from startingPatterns import singleCritter
                world = singleCritter()
            elif (startingWorldInt == 3):
                from startingPatterns import singleBirth
                world = singleBirth()
            elif (startingWorldInt == 4):
                from startingPatterns import simpleBirth
                world = simpleBirth()
            elif (startingWorldInt == 5):
                from startingPatterns import edgeCases
                world = edgeCases()
            elif (startingWorldInt == 6):
                from startingPatterns import complexCase
                world = complexCase()
            elif (startingWorldInt == 7):
                from startingPatterns import moreComplexCases
                world = moreComplexCases()

            inputAccepted = True
            numRows = len(world)
            numColumns = len(world[0])
            return (world, numRows, numColumns)

        else:
            print("\n\x1B[3mError:\x1B[0m Please choose a number between 1-7:\n")


# Function: inputStartingWorld
# @ inputStartingWorld(list)
# @ return(list, int, int)
# Features:
# (1) This function prompts user for an input file that contains a starting world.
# (2) If the file is empty or invalid an appropriate error message will be displayed.
# (3) The function copies the input file into a 2D list called 'world' and then closes the file.
# (4) The function determines the lengths of the rows and columns in the 'world' list.
# (5) The list 'world' and its dimensions are returned to the call function.
def inputStartingWorld(world):
    inputFileOK = False

    while (inputFileOK == False):

        try:
            inputFileName = input("Enter name of input file: ")
            inputFile = open(inputFileName, "r")
            print("Opening file " + inputFileName + " for reading...")

            aLine = inputFile.readline()
            if (aLine == NOTHING):
                print("ERROR: '%s' is an empty file.\n" % (inputFileName))

            elif (aLine != NOTHING):
                currentRow = 0
                while (aLine != NOTHING):
                    world.append([])
                    endLine = False
                    for ch in aLine:
                        if ch in (NOTHING, EMPTY, CRITTER) and (endLine == False):
                            world[currentRow].append(ch)
                        elif (ch == NEW_LINE) and (endLine == False):
                            endLine = True
                    currentRow = currentRow + 1
                    aLine = inputFile.readline()

                inputFileOK = True
            inputFile.close()
            print("Completed reading of file '%s'\n" % (inputFileName))

        except IOError:
            print("ERROR: File '%s' couldn't be opened.\n" % (inputFileName))

    numRows = len(world)
    numColumns = len(world[0])

    return (world, numRows, numColumns)


# Function: count
# @ count(list, int, int, int, int, int, int)
# @ return(int)
# Features:
# (1) This function counts the number of surrounding critters a position on the world map has.
def count(world, rl, rh, cl, ch, currentRow, currentColumn):
    surrounding = 0

    for r in range(rl, rh, 1):
        for c in range(cl, ch, 1):

            if world[r][c] == CRITTER:
                surrounding = surrounding + 1
            if world[r][c] == EMPTY:
                surrounding = surrounding

    if world[currentRow][currentColumn] == CRITTER:
        surrounding = surrounding - 1

    if deBugSurroundingEachPos == True:
        print("\nSurrounding world[%d][%d] = %d" % (currentRow, currentColumn, surrounding))

    return (surrounding)


# Function: copyWorld
# @ copyWorld(list, int, int)
# @ return(list)
# Features:
# (1) This function generates a deep copy of the 'world' list, creating a new list called 'newWorld'
# (2) This allows for the birth and death to be applied to the "New World" (the 'newWorld' list) while keeping the
# "Old World" (the 'world' list) unchanged; so that both worlds can be displayed simultaneously.
# (3) Debugging flag allows for the 'newWorld' list to be displayed right after it generated to ensure no issues
# occurred when copying the list.
def copyWorld(world, numRows, numColumns):
    newWorld = []
    line = 0

    for r in range(0, numRows, 1):
        newWorld.append([])
        for c in range(0, numColumns, 1):
            newWorld[line].append(world[r][c])
        line = line + 1

    if (deBugShowWorldChange == True):
        print("")
        print("\nThis is 'newWorld' which was just created by copying the (old) 'world'")
        for r in range(0, numRows, 1):
            print(newWorld[r])

    return (newWorld)


# Function: birthsAndDeaths
# @ birthsAndDeaths(list, list, list, int, int)
# @ return(list)
# Features:
# (1) This function generates the "New World" by applying the birth and death rules to the "Old World".
# (2) The birth and death rules are based on what is currently in each square (either EMPTY or CRITTER) and the number
# of surrounding CRITTERS for every given square.
# (3) The birth and death rules are given in the game description.
# (4) Debugging flag allows for the 'newWorld' list to be displayed right after the birth and death rules have been
# applied to ensure there was no issues with the birth and death calculations.
def birthsAndDeaths(newWorld, surrounding_list, world, numRows, numColumns):
    for r in range(0, numRows, 1):
        for c in range(0, numColumns, 1):
            if (world[r][c] == CRITTER) and (surrounding_list[r][c] <= 1):
                newWorld[r][c] = EMPTY
            if (world[r][c] == CRITTER) and (surrounding_list[r][c] <= 3) and (surrounding_list[r][c] >= 2):
                newWorld[r][c] = CRITTER
            if (world[r][c] == CRITTER) and (surrounding_list[r][c] >= 4):
                newWorld[r][c] = EMPTY
            if (world[r][c] == EMPTY) and (surrounding_list[r][c] == 3):
                newWorld[r][c] = CRITTER

    if (deBugShowWorldChange == True):
        print("\nThis is the \"New World\" after the birth and death rules have been applied:")
        for r in range(0, numRows, 1):
            print(newWorld[r])

    return (newWorld)


# Function: display()
# Author: James Tam
# Modified by Liam Guetg
# @ display(int, list, list, int, int)
# @ return(none)
# Features:
# (1) This function displays the 'Old world' (before birth and death rules are applied) and the "New world' (after birth
# and death rules are applied) side by side.
# (2) This function also displays the turn the user is on.
def display(turn, world, newWorld, numRows, numColumns):
    # Displays a row at a time of each list
    numberOfSpaces = (2 * numColumns) - 2
    spacesString = " " * numberOfSpaces
    print("\nTurn #%d" % (turn))
    print("%s%s%s" % ("BEFORE", spacesString, "AFTER"))
    for r in range(0, numRows, 1):
        # Row of dashes before each row of old and new list
        # (Dashes for old list)
        for i in range(0, numColumns, 1):
            print("%s" % (" -"), end="")
        print("#\t", end="")
        # (Dashes for new list)
        for i in range(0, numColumns, 1):
            print("%s" % (" -"), end="")
        print()

        # Display one row of old world list
        for c in range(0, numColumns, 1):
            # Display: A vertical bar and then element (old list)
            print("|%s" % (world[r][c]), end="")
        # Separate the lists with a number sign and a tab
        print("", end="#\t")

        # Display one row of new world list
        for c in range(0, numColumns, 1):
            # Display: A vertical bar and then element (new list)
            print("|%s" % (newWorld[r][c]), end="")
        print("|")

    # Row of dashes after end of last row (old world list)
    for i in range(0, numColumns, 1):
        print("%s" % (" -"), end="")
    print("#\t", end="")

    # Row of dashes after end of each row (new world list)
    for i in range(0, numColumns, 1):
        print("%s" % (" -"), end="")
    print()


# Function: transferWorlds
# @ transferWorlds(list, list, int, int)
# @ return(list)
# Features:
# (1) This function deep copies the "New World" (the 'newWorld' list) into the "Old World" (the 'world' list).
# (2) This turns the the "New World" into the "Old World" preparing the 'world' list for the next round of birth
# and death rules to be applied.
# (3) Debugging flag allows for the 'world' list to be displayed right after the new world function was copied into it
# to ensure there was no issues whe copying the list.
def transferWorlds(world, newWorld, numRows, numColumns):
    for r in range(0, numRows, 1):
        for c in range(0, numColumns, 1):
            world[r][c] = newWorld[r][c]

    if (deBugShowWorldChange == True):
        print("")
        print("\ntransferWorlds fnc (after each turn): "
              "This is the 'old world' which should be the same as the newWorld")
        for r in range(0, numRows, 1):
            print(world[r])

    return (world)


# Function: repeat
# @ repeat(int, boolean)
# @ return(boolean, int)
# Features:
# (1) This function prompts the user to input if they wish to continue the biosphere simulation or quit it.
# (2) This function also counts the number of turns the user has gone through in the biosphere simulation.
def repeat(turn, quitBiosphere):
    continueBiosphere = input("\nHit enter to continue ('q' to quit): ")
    if (continueBiosphere == "q"):
        quitBiosphere = True
    else:
        turn = turn + 1

    return (quitBiosphere, turn)


# Function: transferWorlds
# @ getSurroundingList(list, int, int)
# @ return(list)
# Features:
# (1) This function creates a 2D list repersenting the number of surrounding Critters each position has.
# (2) Debugging flag allows for the surrounding_list to be displayed for each turn.
def getSurroundingList(world, numRows, numColumns):
    line = 0
    currentRow = 0
    surrounding_list = []

    while currentRow < numRows:
        surrounding_list.append([])
        currentColumn = 0

        while currentColumn < numColumns:
            surrounding = 0
            if (currentRow == 1):
                rl = 0
                rh = currentRow + 2
                if (currentColumn == 0):
                    cl = 0
                    ch = currentColumn + 2
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

                elif (currentColumn != 0) and (currentColumn != (numColumns - 1)):
                    cl = currentColumn - 1
                    ch = currentColumn + 2
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

                elif (currentRow == 0) and (currentColumn == (numColumns - 1)):
                    cl = currentColumn - 1
                    ch = numColumns
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

            elif (currentRow != 1) and (currentRow != (numRows - 1)):
                rl = currentRow - 1
                rh = currentRow + 2
                if (currentColumn == 0):
                    cl = 0
                    ch = currentColumn + 2
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

                elif (currentColumn != 0) and (currentColumn != (numColumns - 1)):
                    cl = currentColumn - 1
                    ch = currentColumn + 2
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

                elif (currentColumn == numColumns - 1):
                    cl = currentColumn - 1
                    ch = numColumns
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)


            elif (currentRow == numRows - 1):
                rl = currentRow - 1
                rh = numRows
                if (currentColumn == 0):
                    cl = 0
                    ch = currentColumn + 2
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

                elif (currentColumn != numColumns - 1) and (currentColumn != 0):
                    cl = currentColumn - 1
                    ch = currentColumn + 2
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

                elif (currentColumn == numColumns - 1):
                    cl = currentColumn - 1
                    ch = numColumns
                    surrounding = count(world, rl, rh, cl, ch, currentRow, currentColumn)

            surrounding_list[line].append(surrounding)
            currentColumn = currentColumn + 1
        currentRow = currentRow + 1
        line = line + 1

        if deBugSurroundingList == True:
            print("\n'surrounding_list': the number of surrounding critters for each position")
            for r in range(0, numRows, 1):
                print(surrounding_list[r])

    return (surrounding_list)


# /Users/liamguetg/Desktop/startingPattern3.txt

# Function: start()
# @ start(none)
# @ return(none)
# Features:
# (1) This function initializes the 'Game of Life' program
def start():
    world = []
    surrounding_list = []
    numRows = -1
    numColumns = -1
    currentRow = -1
    currentColumn = -1
    turn = -1
    quitBioshpere = False

    world, numRows, numColumns = startingWorldOptions(world)

    turn = 0
    while quitBioshpere == False:
        surrounding_list = getSurroundingList(world, numRows, numColumns)
        newWorld = copyWorld(world, numRows, numColumns)
        newWorld = birthsAndDeaths(newWorld, surrounding_list, world, numRows, numColumns)
        display(turn, world, newWorld, numRows, numColumns)
        world = transferWorlds(world, newWorld, numRows, numColumns)
        quitBioshpere, turn = repeat(turn, quitBioshpere)


start()

