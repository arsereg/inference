from facade import *
from logicalOperations import sibling, parent, couple


def printMenu():
    menuOptions = {
        "1": "Create",
        "2": "View",
        "3": "Status",
        "4": "Exit"
    }
    for key, value in menuOptions.items():
        print(f"{key}: {value}")

    userSelection = input("Enter a number: ")
    if userSelection == "1":
        createMenu()
    elif userSelection == "2":
        viewMenu()
    elif userSelection == "3":
        statusMenu()
    elif userSelection == "4":
        return False
    else:
        print("Invalid selection")
    return userSelection


def createParentChild():
    print("Parent-child relationship creation:")
    father = input("Enter the father's name: ")
    mother = input("Enter the mother's name: ")
    child = input("Enter the child's name: ")
    addParent(mother, father, child)
    print(f"Added {father} and {mother} as parents of {child}")


def createSibling():
    print("Sibling relationship creation:")
    siblingOne = input("Enter the first sibling's name: ")
    siblingTwo = input("Enter the second sibling's name: ")
    addSibling(siblingOne, siblingTwo)
    pass


def createCouple():
    print("Couple relationship creation:")
    personOne = input("Enter the first person's name: ")
    personTwo = input("Enter the second person's name: ")
    addCouple(personOne, personTwo)
    pass


def createMenu():
    menuOptions = {
        "1": "Create a parent-child relationship",
        "2": "Create a sibling relationship",
        "3": "Create a couple relationship",
        "4": "Exit"
    }
    for key, value in menuOptions.items():
        print(f"{key}: {value}")

    userSelection = input("Enter a number: ")
    if userSelection == "1":
        createParentChild()
    elif userSelection == "2":
        createSibling()
    elif userSelection == "3":
        createCouple()
    elif userSelection == "4":
        return False
    else:
        print("Invalid selection")


def findSiblings():
    getFacts(sibling, "sibling")
    for fact in sibling.facts:
        print(f"{fact[0]} is a sibling of {fact[1]}")


def findParents():
    getFacts(parent, "parent")
    for fact in parent.facts:
        print(f"{fact[0]} is a parent of {fact[1]}")

def findCouples():
    getFacts(couple, "couple")
    for fact in couple.facts:
        print(f"{fact[0]} is a partner of {fact[1]}")


def statusMenu():
    menuOptions = {
        "1": "View siblings",
        "2": "View parents",
        "3": "View couples",
        "4": "Exit"
    }
    for key, value in menuOptions.items():
        print(f"{key}: {value}")

    userSelection = input("Enter a number: ")
    if userSelection == "1":
        findSiblings()
    elif userSelection == "2":
        findParents()
    elif userSelection == "3":
        findCouples()
    elif userSelection == "4":
        return False


def findSiblingsForIndividual():
    person = input("Enter the name of the individual: ")
    siblings = find_siblings_of(person)
    print(f"Siblings of {person}: {siblings}")


def findParentsForIndividual():
    person = input("Enter the name of the individual: ")
    parents = find_parents_of(person)
    print(f"Parents of {person}: {parents}")
    pass


def findChildrenForIndividual():
    person = input("Enter the name of the individual: ")
    children = find_children_of(person)
    print(f"Children of {person}: {children}")

def findGrandparentsForIndividual():
    person = input("Enter the name of the individual: ")
    grandparents = find_grandparents_of(person)
    print(f"Grandparents of {person}: {grandparents}")


def findCouplesForIndividual():
    person = input("Enter the name of the individual: ")
    couples = find_couples_of(person)
    print(f"Couples of {person}: {couples}")


def viewMenu():
    menuOptions = {
        "1": "View siblings for an individual",
        "2": "View parents for an individual",
        "3": "View children for an individual",
        "4": "View grandparents for an individual",
        "5": "View couple for an individual",
        "6": "Exit"
    }
    for key, value in menuOptions.items():
        print(f"{key}: {value}")

    userSelection = input("Enter a number: ")
    if userSelection == "1":
        findSiblingsForIndividual()
    elif userSelection == "2":
        findParentsForIndividual()
    elif userSelection == "3":
        findChildrenForIndividual()
    elif userSelection == "4":
        findGrandparentsForIndividual()
    elif userSelection == "5":
        findCouplesForIndividual()
    elif userSelection == "6":
        return False




def selectMenu():
    print("Select an option:")
    return printMenu()

if __name__ == '__main__':
    applicationStarted = True
    while applicationStarted:
        applicationStarted = selectMenu()



