""" read bookmaster, and put all entries on single page called "books"
reviews are in md, contained in subdirectory.
"""

from pelican import signals
from pelican.readers import Readers
from pelican.contents import Page
#from pelican.readers import MarkdownReader
#from pelican.generators import TemplatePagesGenerator
from pelican.generators import Generator
from pelican.writers import Writer

import pprint
from pathlib import Path, PurePath


class BookEntry(object):
    pass


class BooksGenerator(Generator):

    def __init__(self, context, settings, path, theme, output_path, 
        readers_cache_name='', **kwargs):

        super().__init__(context, settings, path, theme, output_path, readers_cache_name)

        self.output_path = output_path
        self.context = context
        self.settings = settings

        #print('settings=', self.settings)
        pp = pprint.PrettyPrinter()
        #pp.pprint(self.settings)
        
        #self.settings['READERS'] = {'md' : MarkdownReader}
        #pp.pprint(self.settings)


        self.path = path
        self.books_home = PurePath(
            settings['PATH'], settings['BOOKS_PAGES_HOME'])
        self.books_list = PurePath(self.books_home, 'books_list')
        self.readers = Readers(self.settings, readers_cache_name)

        
        print('books_home=', self.books_home)
        # get list of book md files
        p = Path(self.books_list)

        self.entries = []

        for f in p.iterdir():
            print('f=', f)
            entry = self.generate_entry(f)
            self.entries.append(entry)

        self.context['book_list'] = self.entries

        #template = get_template()
        #writer = Writer()
        #writer.write_file(name, template, context)

    #def generate_output(self, writer):
    #    # path = os.path.join(self.output_path, 'sitemap.{0}'.format(self.format))
    #    print('writer here, writer=', writer, dir(writer))
    #    print('pages=', self.context['pages'])
    #
    #    self.generate_output(writer)



        #writer.write_file('books', template, self.context, relative_urls=False,
        #           paginated=None, template_name=None, override_output=False,
        #           url=None, **kwargs)

    def generate_entry(self, md_file):
        entry = self.readers.read_file(
            base_path=self.path, path=md_file, content_class=Page,
            context=self.context)
            #preread_signal=signals.article_generator_preread,
            #preread_sender=self,
            #context_signal=signals.article_generator_context,
            #context_sender=self)
        
        i = 15
        print('*****entry=', entry, dir(entry))
        print(f'**** meta={entry.metadata}')
        i = 25
        return entry
    

               
                
            

def get_generators(generators):
    # define a new generator here if you need to
    
    return BooksGenerator

def register():
    signals.get_generators.connect(get_generators)


    