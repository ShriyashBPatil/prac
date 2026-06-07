# Forward Chaining and Backward Chaining
# Rules: Conditions -> Conclusion
rules = [
    (["A", "B"], "C"),
    (["C"], "D"),
    (["D"], "E")
]
# Initial Facts
facts = {"A", "B"}
# Forward Chaining
def forward_chaining(facts):
    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(c in facts for c in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    print("Inferred:", conclusion)
                    changed = True
    return facts
# Backward Chaining
def backward_chaining(goal):
    if goal in facts:
        return True
    for conditions, conclusion in rules:
        if conclusion == goal:
            return all(
                backward_chaining(c)
                for c in conditions
            )
    return False
# Main Program
print("Initial Facts:", facts)
print("\n--- Forward Chaining ---")
final_facts = forward_chaining(set(facts))
print("Final Facts:", final_facts)
print("\n--- Backward Chaining ---")
goal = "E"
if backward_chaining(goal):
    print("Goal", goal, "is PROVED")
else:
    print("Goal", goal, "is NOT PROVED")
