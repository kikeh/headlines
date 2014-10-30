import sys

class Newspaper:
    
    name    = ''
    url     = ''
    pattern = ''

    def __init__(self, *args, **kwargs):
        if self.is_number(args[0]):
            try:
                self.set_attributes(self.newsDB[int(args[0])])
            except IndexError:
                print("No newspaper with id: %r" % args[0])
                sys.exit(2)
        else:
            try:
                entry = self.find_by_name(args[0])
                if entry == None:
                    raise TypeError('TypeError')
                self.set_attributes(entry)
            except TypeError:
                print("No newspaper with name: %r" % args[0])
                sys.exit(2)

    def set_attributes(self, entry):
        self.name    = entry['name']
        self.url     = entry['url']
        self.pattern = entry['pattern']
            

    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def find_by_name(self, name):
        for i in self.newsDB:
            if i['name'] == name:
                return i
        return None
            

    newsDB = ({'name': 'elmundo'  , 'url': 'http://www.elmundo.es'  , 'pattern': '<article.*?>.*?<header.*?>.*?<h1.*?>.*?<a.*?>(.*?)</a>.*?</article>'},
              {'name': '20minutos', 'url': 'http://www.20minutos.es', 'pattern': '<a.*?class="title".*?>(.*?)</a>'})
