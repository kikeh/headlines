import urllib2
import re
from Filter import Filter
from Headline import Headline
from Newspaper import Newspaper
import sys, getopt

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def choose_newspaper(newspaper):
    return Newspaper(newspaper)

def main(argv):

    nheads  = 0
    news_id = 0

    try:
        opts, args = getopt.getopt(argv,"n:p:",["num-headlines=", "newspaper="])
    except getopt.GetoptError:
        print('usage: headlines.py -n <num_headlines> -p <newspaper>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-n", "--num-headlines"):
            nheads = arg
        elif opt in ("-p", "--newspaper"):
            news_id = arg
        else:
            print('usage: headlines.py -n <num_headlines> -p <newspaper>')
            sys.exit(2)

    news = choose_newspaper(news_id)
    response = urllib2.urlopen(news.url)
    page_source = response.read()
    headlines = re.findall(news.pattern, page_source, re.DOTALL)
    
    heads = []
    for title in headlines:
        heads.append(Headline(title))

    filt = Filter(heads)
    filt.filter_all()

    if is_number(nheads):
        filt.print_title_summary(int(nheads))
    else:
        print("Invalid nheads")

if __name__ == "__main__":
   main(sys.argv[1:])
