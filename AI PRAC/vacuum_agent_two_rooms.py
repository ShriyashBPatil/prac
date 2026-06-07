# Vacuum Cleaner Agent for Two Rooms
def vacuum_agent(location, status):
    if status.lower() == "dirty":
        return "Suck"
    if location == "A":
        return "Move Right"
    else:
        return "Move Left"
# Test Cases
for location in ["A", "B"]:
    for status in ["clean", "dirty"]:
        print(
            f"Location: {location}, Status: {status}, Action: {vacuum_agent(location, status)}"
        )
