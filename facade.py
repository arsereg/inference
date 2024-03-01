import numbers

from kanren import Relation, facts, conde, run, eq, lall, membero, lany
from unification import var

import logicalOperations

def find_siblings_of(individual):
    siblingList = var()
    siblings_result = run(0, siblingList, logicalOperations.siblings(siblingList, individual))
    filtered_result = [s for s in siblings_result if s != individual]
    return filtered_result

def find_parents_of(individual):
    mother = var()
    father = var()
    return run(1, (mother, father), logicalOperations.parents(individual, mother, father))

def find_children_of(individual):
    child = var()
    return run(0, child, logicalOperations.children(individual, child))

def find_grandparents_of(individual):
    grandparent = var()
    return run(0, grandparent, logicalOperations.grandparent(grandparent, individual))

def find_couples_of(individual):
    partner = var()
    return run(0, partner, logicalOperations.spouse(individual, partner))

def addParent(mother, father, child):
    logicalOperations.addParent(mother, child)
    logicalOperations.addParent(father, child)

def addSibling(sibling1, sibling2):
    logicalOperations.addSibling(sibling1, sibling2)

def addCouple(individual1, individual2):
    logicalOperations.addCouple(individual1, individual2)


def getFacts(relation, relation_name):
    return logicalOperations.getFacts(relation, relation_name)
