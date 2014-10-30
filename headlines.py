import urllib2
import re
from Filter import Filter
from Headline import Headline
import sys, getopt

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main(argv):

    nheads = 0

    try:
        opts, args = getopt.getopt(argv,"n:",["num="])
    except getopt.GetoptError:
        print('usage: headlines.py -n <numheads>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-n", "--num"):
            nheads = arg
    
    response = urllib2.urlopen("http://www.20minutos.es")
    page_source = response.read()
    pattern = '<a.*?class="title".*?>(.*?)</a>'
    headlines = re.findall(pattern, page_source)
    
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
