import re

class Headline:

    good_words = 0
    bad_words = 0
    
    nature = 0
    title  = "title"

    def __init__ (self,title):
        self.title = title

    def set_nature(self,nature):
        if nature >= -1 and nature <= 1:
            self.nature = nature

    def get_nature(self):
        if self.nature == -1:
            return "negative"
        elif self.nature == 0:
            return "moderate"
        else:
            return "positive"

    def update_nature_status(self):
        if self.good_words > self.bad_words:
            self.nature = 1
        elif self.bad_words > self.good_words:
            self.nature = -1

    def print_info(self):
        print("Title   : %s") % self.title
        print("Good  : %d") % self.good_words
        print("Bad   : %d") % self.bad_words
        print("Nature: %s") % self.get_nature()
