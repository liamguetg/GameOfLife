SIZE = 10
debugOn = False

#Game of Life simulation Starting Patterms

"""
  @emptyWorld()
  @Arguments: None
  @An empty world (no critters).
  @Return value: A reference to a 2D list, the starting world.
"""
def emptyWorld():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)


"""
  @singleCritter()
  @Arguments: None
  @World with 1 critter.
  @Return value: A reference to a 2D list, the starting world.
"""
def singleCritter():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

"""
  @singleBirth()
  @Arguments: None
  @World with 3 neighbouring critters that will result in 1 birth.
  @Return value: A reference to a 2D list, the starting world.
"""
def singleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " ","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

"""
  @simpleBirth()
  @Arguments: None
  @World with critters placed to result in a number of births.
  @Return value: A reference to a 2D list, the starting world.
"""
def simpleBirth():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", "*","*", " ", " ", " ", " ", " ", " "],
     [" ","*", " ","*", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

"""
  @edgeCases()
  @Arguments: None
  @World with critters placed at the edges and corners.
  @Return value: A reference to a 2D list, the starting world.
"""
def edgeCases():
    world = []
    world = [
     ["*"," ", "*"," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", "*"],
     [" "," ", " "," ", " ", " ", " ", " ", "*", " "],
     ["*","*", " "," ", " ", " ", " ", " ", " ", "*"]
    ]
    return(world)


"""
  @complexCases()
  @Arguments: None
  @world that will have births, deaths and edge cases.
  @Return value: A reference to a 2D list, the starting world.
"""
def complexCase():
    world = []
    world = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        [" ", "*", " ", " ", " ", " ", " ", " ", "*", " ", " "],
        [" ", " ", " ", "*", " ", " ", " ", " ", " ", " ", "*"],
        [" ", "*", " ", " ", " ", "*", " ", " ", "*", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", "*", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "*", "*", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "*", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    ]
    return (world)

"""
  @moreComplexCases()
  @Arguments: None
  @world that will have births, deaths and edge cases and results in a pattern that does not die out.
  @Return value: A reference to a 2D list, the starting world.
"""
def moreComplexCases():
    world = []
    world = [
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", "*", " ", " ", " ", " ", " "],
     [" ","*", " "," ", " ", "*", " ", " ", " ", " "],
     [" "," ", " ","*", "*", "*", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     [" "," ", " "," ", " ", " ", " ", " ", " ", " "],
     ["*"," ", " "," ", " ", " ", " ", " ", " ", " "]
    ]
    return(world)

