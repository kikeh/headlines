from __future__ import division
from Headline import *
from WordsList import *
import re

class Filter:

    POSITIVE = 1
    NEGATIVE = -1

    good_list = ["paz","buen","feli[c|z]","esperanz"]
    bad_list  = ["guerr","fall","grav","viru","falt","exces","enferm", "problem","verg.en","pol.mic", "desahuci", "v.ctim",".bola","contag","emergenc","cr.tic","lament","crisis","suspend","muert","miedo"]

    goods = WordsList(good_list, POSITIVE)
    bads  = WordsList(bad_list,  NEGATIVE)

    total_good_words = 0
    total_bad_words  = 0
    
    def __init__(self,content):
        self.content = content

    def update_headline_words_status(self, alist, headline, total):
        if alist.nature == self.POSITIVE:
            headline.good_words = total
        else:
            headline.bad_words  = total

    def filter_headline(self, headline, alist):
        total = 0
        for element in alist.list_of_words:
            pattern = ".*?%s.*?" % element
            result = re.findall(pattern,headline.title.lower())
            total += len(result)
        self.update_headline_words_status(alist, headline, total)
        
    def filter_content(self):
        for headline in self.content:
            self.filter_headline(headline, self.goods)
            self.filter_headline(headline, self.bads)
            headline.update_nature_status()
            #headline.printInfo()
            
    def calculate_totals(self):
        for headline in self.content:
            self.total_good_words += headline.good_words
            self.total_bad_words += headline.bad_words

    def get_total_good_headlines(self):
        total = 0
        for headline in self.content:
            if headline.nature == 1:
                total = total + 1
        return total

    def get_total_bad_headlines(self):
        total = 0
        for headline in self.content:
            if headline.nature == -1:
                total = total + 1
        return total
            
    def calculate_percentage(self):
        total = self.total_good_words + self.total_bad_words
        if self.total_good_words > self.total_bad_words:
            return self.total_good_words / total
        else:
            return self.total_bad_words  / total

    def calculate_result(self):
        if self.total_good_words > self.total_bad_words:
            return "positive"
        elif self.total_bad_words == self.total_good_words:
            return "moderate"
        else:
            return "negative"
    
    def print_result(self):
        percentage    = self.calculate_percentage()
        filter_result = self.calculate_result()
        print("Matches: ")
        print("  %d out of %d matches are good") % (self.total_good_words, self.total_good_words + self.total_bad_words)
        print("  %d out of %d matches are bad")  % (self.total_bad_words, self.total_good_words + self.total_bad_words)
        print("Headlines: ")
        print("  Good    : %d")  % self.get_total_good_headlines()
        print("  Bad     : %d")  % self.get_total_bad_headlines()
        print("  Moderate: %d")  % len(self.content)
        print("Headlines are %.2f%% %s.") % (percentage*100, filter_result)

    def filter_all(self):
        self.filter_content()
        self.calculate_totals()
        self.print_result()

    def print_title_summary(self,n):
        c = 1
        for head in self.content:
            #head.title = head.title.decode('ISO-8859-1') 
            if c == n+1:
                break;
            if len(head.title) <= 100:
                print("[%d] %s") % (c,head.title)
            else:
                print("[%d] %s [...]") % (c,head.title[0:94])
            c = c + 1
