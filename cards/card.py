class Card:
    def __init__(self, name, _type, cost, text):
        self.name = name
        self._type = _type
        self.cost = cost
        self.text = text
        self.base_amount = 10
        self.to_be_cleaned = True
        self.temp_phase = None
    def __str__(self):
        return self.name + ": " + self.text
    def on_pickup(self):
        pass
    def on_play(self):
        pass
    def on_trash(self):
        pass
    def score(self):
        pass