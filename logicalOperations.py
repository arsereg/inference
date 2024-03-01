from kanren import Relation, facts, conde, run, eq, lall, membero, lany
from unification import var

parent = Relation()
sibling = Relation()
couple = Relation()

facts(parent,
        ("Cinthya", "Jose Andrés"),
          ("Cinthya", "Juan Pablo"),

          ("Mónica",  "Tomás"),
          ("Jose Alberto",  "Tomás"),

          ("Maribel", "Cinthya"),
          ("Maribel", "Mónica"),
          ("Maribel", "Gino Alonso"),

          ("Roxana", "Jose Alberto")
      )

facts(sibling,
      ("Jose Andrés", "Juan Pablo"),
          ("Cinthya", "Mónica"),
          ("Cinthya", "Gino")
      )

facts(couple,
      ("Cinthya", "Andrés"),
          ("Mónica", "Jose Alberto"),
          ("Maribel", "Gino Alberto"),
          ("Gino Alonso", "Xiomara"),
            ("Don Juan", "Roxana")
      )

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

def addSibling(personA, personB):
    facts(sibling, (personA, personB))

def addCouple(personA, personB):
    facts(couple, (personA, personB))