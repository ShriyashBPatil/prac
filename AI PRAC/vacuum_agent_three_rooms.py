# Vacuum Cleaner Agent for Three Rooms
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Suck"
    location = location.upper()
    if location == "A":
        return "Move Right"
    elif location == "B":
        return "Move Right"
    elif location == "C":
        return "Move Left"
    else:
        return "Invalid Location"
# Test Cases
for location in ["A", "B", "C"]:
    for status in ["clean", "dirty"]:
        print(
            f"Location: {location}, Status: {status}, Action: {vacuum_agent(location, status)}"
        )
