class GotCharacter:
    """GoT Character without a house"""
    def __init__(self, first_name: str = None, is_alive: bool = True) -> None:
        self.first_name = first_name;
        self.is_alive = is_alive;

class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad things happen to good people."""
    def __init__(self, first_name: str = None, is_alive: bool = True):
        super().__init__(first_name = first_name, is_alive = is_alive);
        self.family_name = "Stark";
        self.house_words = "Winter is Coming";
    def print_house_words(self):
        print(self.house_words);
    def die(self):
        self.is_alive = False;