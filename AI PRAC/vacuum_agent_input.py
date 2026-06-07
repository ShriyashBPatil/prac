# Vacuum Cleaner Agent Using User Input
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Suck"
    location = location.upper()
    if location == "A":
        return "Move Right to B"
    elif location == "B":
        return "Move Right to C"
    elif location == "C":
        return "Move Left to B"
    else:
        return "Invalid Location"
# User Input
location = input("Enter Location (A/B/C): ")
status = input("Enter Status (clean/dirty): ")
# Agent Action
print("Action:", vacuum_agent(location, status))
