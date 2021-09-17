class Protagonist:
    def __init__(self, name, pronoun_list):
        self.name = name
        self.subject_pronoun = pronoun_list[0]
        self.object_pronoun = pronoun_list[1]
        self.possessive_pronoun = pronoun_list[2]