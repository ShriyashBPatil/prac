# Simple Reactive Agent (Vacuum Cleaner World)
class SimpleAgent:
    def decide(self, environment):
        if environment == "dirty":
            return "clean"
        else:
            return "move"
environment = "dirty"
agent = SimpleAgent()
action = agent.decide(environment)
print("Agent action:", action)
