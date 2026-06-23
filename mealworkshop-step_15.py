# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: MealWorkshop
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}
    
    def dispatch(self, text):
        cleaned = text.strip().lower()
        if not cleaned or cleaned.startswith('#') or cleaned.startswith('!'):
            return None
        parts = cleaned.split(maxsplit=1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ''
        handler = self.handlers.get(command)
        if not handler:
            print(f"Unknown command: {command}")
            return None
        try:
            result = handler(args)
            if result is not None:
                print(result)
            return result
        except Exception as e:
            print(f"Error executing '{command}': {e}")
            return None

    def register(self, command, handler):
        self.handlers[command.lower()] = handler
