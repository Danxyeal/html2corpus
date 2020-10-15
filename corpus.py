import pandas as pd
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

class RetrievalInterface(ABC):
    @abstractmethod
    def retrieve_product():
        pass


class Corpus:
    def __init__(self, product_dictionary):
        self.full = product_dictionary
        self.data_frames = []
        self.html_string = self.full['html_string']

    def straighten_html(self):
        html_no_lines = ''.join([char for char in html_string if not char == '\n'])
        html_tag_lines = ''.join([c for char in sentence])

            '''

def get_body_main(tag:str, id:str, html_input='index.html', is_string=False):
    product_dictionary = {
        'main_tag': tag,
        'main_div_id': id,
    }
    html_string = ''
    if not is_string:
        with open(html_input, 'r') as input_file:
            html_string = input_file.read()
        #html_input = BeautifulSoup(open(html_input, encoding="utf8").read(), 'html.parser')
    html_string = tag_lines(html_string)
    soup = BeautifulSoup(html_string, 'html.parser')
    soup = discard_script_and_style(soup)
    title = soup.find('title').text
    soup = soup.find(tag, id=id)
    product_dictionary.update({'html_body_string':str(soup)})
    product_dictionary.update({'html_lines': str(soup).splitlines()})
    product_dictionary.update({'body_text':soup.get_text()})
    product_dictionary.update({'page_title':title})
    return product_dictionary
    '''
