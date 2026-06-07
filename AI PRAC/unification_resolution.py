
def unify(x, y, subst=None):
    if subst is None:
        subst = {}
    if x == y:
        return subst
    if isinstance(x, str) and x.islower():
        subst[x] = y
        return subst
    if isinstance(y, str) and y.islower():
        subst[y] = x
        return subst
    if isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y):
            return None
        for a, b in zip(x, y):
            subst = unify(a, b, subst)
            if subst is None:
                return None
        return subst
    return None
# Apply Substitution
def apply_subst(exp, subst):
    if isinstance(exp, list):
        return [apply_subst(i, subst) for i in exp]
    return subst.get(exp, exp)
# RESOLUTION
def resolve(c1, c2):
    result = []
    for l1 in c1:
        for l2 in c2:
            subst = None
            if l1[0] == "not" and l2[0] != "not":
                subst = unify(l1[1], l2)
            elif l2[0] == "not" and l1[0] != "not":
                subst = unify(l2[1], l1)
            if subst is not None:
                clause = []
                for lit in c1 + c2:
                    if lit != l1 and lit != l2:
                        clause.append(apply_subst(lit, subst))
                result.append(clause)
    return result
# Resolution Process
def resolution(kb):
    while True:
        new_clauses = []
        for i in range(len(kb)):
            for j in range(i + 1, len(kb)):
                for clause in resolve(kb[i], kb[j]):
                    if clause == []:
                        print("Contradiction Found")
                        return True
                    if clause not in kb and clause not in new_clauses:
                        new_clauses.append(clause)
        if not new_clauses:
            return False
        kb.extend(new_clauses)

# Knowledge Base
c1 = [['not', ['P', 'x']], ['Q', 'x']]
c2 = [['P', 'A']]
c3 = [['not', ['Q', 'A']]]
kb = [c1, c2, c3]
# Run Resolution
resolution(kb)
