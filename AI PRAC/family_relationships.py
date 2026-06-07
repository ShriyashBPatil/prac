# Knowledge Base for Family Relationship Reasoning
# Knowledge Base (Facts)
facts = {
    ("parent", "John", "Mary"),
    ("parent", "Mary", "Sam"),
    ("parent", "John", "Alex"),
    ("male", "John"),
    ("male", "Sam"),
    ("male", "Alex"),
    ("female", "Mary")
}
# Basic Relations
def parent(x, y):
    return ("parent", x, y) in facts
def male(x):
    return ("male", x) in facts
def female(x):
    return ("female", x) in facts
# Derived Relations
def father(x, y):
    return parent(x, y) and male(x)
def mother(x, y):
    return parent(x, y) and female(x)
def grandparent(x, z):
    for rel in facts:
        if rel[0] == "parent":
            y = rel[2]
            if parent(x, y) and parent(y, z):
                return True
    return False
def sibling(x, y):
    if x == y:
        return False
    for rel in facts:
        if rel[0] == "parent":
            p = rel[1]
            if parent(p, x) and parent(p, y):
                return True
    return False
def brother(x, y):
    return sibling(x, y) and male(x)
def sister(x, y):
    return sibling(x, y) and female(x)
# Testing
print("Father(John, Mary):", father("John", "Mary"))
print("Mother(Mary, Sam):", mother("Mary", "Sam"))
print("Grandparent(John, Sam):", grandparent("John", "Sam"))
print("Sibling(Sam, Alex):", sibling("Sam", "Alex"))
print("Brother(Alex, Sam):", brother("Alex", "Sam"))
print("Sister(Mary, Alex):", sister("Mary", "Alex"))
