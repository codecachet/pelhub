""" read bookmaster, and put all entries on single page called "books"
reviews are in md, contained in subdirectory.
"""

from pelican import signals
from bs4 import BeautifulSoup            

def do_pretty(path, context):

    return # check PRETTIFY_WITH_BS4

    print(f'PRETTIFY: path={path}')
    with open(path, 'r') as f:
        doc = f.read()
    soup = BeautifulSoup(doc, 'html5lib')
    pdoc = soup.prettify()
    with open(path, 'w') as f:
        f.write(pdoc)


# path, context
def register():
    signals.content_written.connect(do_pretty)


    