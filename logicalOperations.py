import json

from kanren import Relation, facts, conde, run, eq, lall, membero, lany
from unification import var

parent = Relation()
sibling = Relation()
couple = Relation()

# facts(parent,
#         ("Cinthya", "Jose Andrés"),
#           ("Cinthya", "Juan Pablo"),
#
#           ("Mónica",  "Tomás"),
#           ("Jose Alberto",  "Tomás"),
#
#           ("Maribel", "Cinthya"),
#           ("Maribel", "Mónica"),
#           ("Maribel", "Gino Alonso"),
#
#           ("Roxana", "Jose Alberto")
#       )
#
# facts(sibling,
#       ("Jose Andrés", "Juan Pablo"),
#           ("Cinthya", "Mónica"),
#           ("Cinthya", "Gino")
#       )
#
# facts(couple,
#       ("Cinthya", "Andrés"),
#           ("Mónica", "Jose Alberto"),
#           ("Maribel", "Gino Alberto"),
#           ("Gino Alonso", "Xiomara"),
#             ("Don Juan", "Roxana")
#       )

def loadFacts():
    # open JSON file
    with open('db.json') as json_file:
        data = json.load(json_file)
        for fact in data['parent']:
            key = list(fact.keys())[0]
            value = list(fact.values())[0]
            facts(parent, (key, value))

        for fact in data['sibling']:
            key = list(fact.keys())[0]
            value = list(fact.values())[0]
            facts(sibling, (key, value))

        for fact in data['couple']:
            key = list(fact.keys())[0]
            value = list(fact.values())[0]
            facts(couple, (key, value))

loadFacts()

def grandparent(grandParent, individual):
    regularParent = var()
    grandparent_spouse = var()
    return conde(
        (
        parent(grandParent, regularParent), parent(regularParent, individual), spouse(grandParent, grandparent_spouse)),
        (parent(grandparent_spouse, regularParent), parent(regularParent, individual),
         spouse(grandparent_spouse, grandParent))
    )

def children(parentOne, child):
    parentTwo = var()
    return conde(
        (parent(parentOne, child), spouse(parentOne, parentTwo)),
        (parent(parentTwo, child), spouse(parentTwo, parentOne))
    )

def spouse(x, y):
    return lany(couple(x, y), couple(y, x))

def parents(child, mother, father):
    return conde(
        (parent(mother, child), spouse(mother, father)),
        (parent(father, child), spouse(father, mother))
    )

def siblings(person1, person2):
    parent_var = var()
    return conde([parent(parent_var, person1), parent(parent_var, person2)])


def addParent(child, pparent):
    facts(parent, (child, pparent))
    saveState()

def addSibling(personA, personB):
    facts(sibling, (personA, personB))
    saveState()

def addCouple(personA, personB):
    facts(couple, (personA, personB))

def getFacts(relation, relation_name):
    result = []
    result.append((f"Facts for {relation_name}:"))
    for fact in relation.facts:
        # Each fact is a tuple in the relation's .facts set
        result.append((f"  {fact[0]} is {relation_name} of {fact[1]}"))
    return result

#get all facts in JSON format
def saveState():
    parentFacts = []
    for fact in parent.facts:
        parentFacts.append({fact[0]: fact[1]})

    siblingFacts = []
    for fact in sibling.facts:
        siblingFacts.append({fact[0]: fact[1]})

    coupleFacts = []
    for fact in couple.facts:
        coupleFacts.append({fact[0]: fact[1]})

    data = {
        "parent": parentFacts,
        "sibling": siblingFacts,
        "couple": coupleFacts
    }

    with open('db.json', 'w') as outfile:
        json.dump(data, outfile)

saveState()

