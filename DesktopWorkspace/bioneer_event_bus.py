# Project Bioneer: Local Asynchronous Event Bus

class BioneerEventBus:
    def __init__(self):
        self.subscribers = []

    def register(self, callback_func):
        self.subscribers.append(callback_func)
        print(f"[Event Bus] Subscriber registered. Total active: {len(self.subscribers)}")

    def dispatch(self, event_name, payload):
        print(f"[Event Bus] Dispatching event: '{event_name}'")
        for sub in self.subscribers:
            sub(event_name, payload)

if __name__ == "__main__":
    bus = BioneerEventBus()
    bus.register(lambda e, p: print(f"  -> Handler received [{e}]: {p}"))
    bus.dispatch("SYSTEM_BOOT", "All local modules synchronized.")