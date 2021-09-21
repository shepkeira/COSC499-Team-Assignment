class Protagonist:
    def __init__(self, name, pronoun_list):
        self.name = name
        self.subject_pronoun = pronoun_list[0]
        self.object_pronoun = pronoun_list[1]
        self.possessive_pronoun = pronoun_list[2]
        self.completed_adventures = []
    # this function takes in an adventure name
    # adventure names are added to a list to show which adventures are avalible at a given time
    def add_adventure(self, adventure_name):
        if adventure_name not in self.completed_adventures:
            self.completed_adventures.append(adventure_name)