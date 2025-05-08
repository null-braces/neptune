class ContextManager:
    def __init__(self, max_turns=10):
        self.history = []
        self.max_turns = max_turns

    def add_turn(self, user_input, assistant_response):
        self.history.append({"user": user_input, "assistant": assistant_response})
        if len(self.history) > self.max_turns:
            self.history = self.history[-self.max_turns:]

    def get_context(self):
        return self.history

    def reset(self):
        self.history = []
