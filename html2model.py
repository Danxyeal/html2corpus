from bs4 import BeautifulSoup

def tag_lines(html_string):
    # html_no_lines = ''.join([char for char in html_string if not char == '\n'])
    # html_tag_lines = ''.join([c for char in sentence])
    no_newlines = html_string.replace('\n','')
    newline_tags = []
    for c in no_newlines:
        if c == '<':
            newline_tags.append('\n<')
        else:
            newline_tags.append(c)
    return ''.join(newline_tags)[1:]

def soup_lines(lines):
    for text in lines:
        return (BeautifulSoup(text, 'html.parser') for text in lines)
    
def unwrap_format_tags(soup):
    format_tags = ['b', 'div', 'strong', 'i', 'em', 'mark', 'span', 'sup']
    for tag in soup.find_all(format_tags):
        tag.unwrap()
    return soup


def discard_script_style_and_link_tags(soup):
    for s in soup.find_all('script'):
        s.extract()
    for s in soup.find_all('style'):
        s.extract()
    for s in soup.find_all('link'):
        s.extract()
    return soup

def get_body_main(tag, selector, html_input='index.html', use_id=True, is_string=False):
    if not is_string:
        with open(html_input, 'r') as input_file:
            html_string = input_file.read()
    html_string = tag_lines(html_string)
    soup = BeautifulSoup(html_string, 'html.parser')
    return {
        'main_tag': tag,
        'main_div_id': selector,
        'soup_main': soup.find(tag, id=selector),
        'clean_soup': discard_script_style_and_link_tags(soup),
        'raw_html': html_string.replace('\n', ''),
        'body_text': soup.get_text(),
        'page_title': soup.find('title').text,
    }

def remove_chars(sentence,chars):
    return ''.join([c for c in sentence if c not in chars])

def replace_chars(text, c):
    return text.replace(c, ' ')

def read_tags(soup):
    for tag in soup.find_all():
        return tag.name

def read_attrs(soup):
    attrs = {'class': '', 'id': '', 'name': ''}
    for tag in soup.find_all():
        attrs['class'] = tag.attrs.get('class')
        attrs['id'] = tag.attrs.get('id')
        attrs['name'] = tag.attrs.get('name')
    return attrs

def if_not_none(item, attribute):
    if item:
        ia = item.get(attribute)
        return ia if not ia == '' else None
    return None

def prepare_data(tags, attrs, text):
    for i in range(0, len(tags)):
        tags[i] = tags[i] if tags[i] else None
        text[i] = text[i].strip() if text[i].strip() else None
    tag_id = [if_not_none(a, 'id') for a in attrs]
    tag_class = [if_not_none(a, 'class') for a in attrs]
    tag_name = [if_not_none(a, 'name') for a in attrs]
    return {
        'LABEL': '',
        'TXT': text,
        'TAG': tags,
        'ID': tag_id,
        'CLASS': tag_class,
        'NAME': tag_name,
        'TXT': text,
    }

#read_text = lambda soup: [tag.text for tag in soup.find_all()]

def get_data(html_lines):
    lines = [line.replace('\t','') for line in html_lines]
    tags = [read_tags(soup) for soup in soup_lines(html_lines)]
    attrs = [read_attrs(soup) for soup in soup_lines(lines)]
    text = [soup.text for soup in soup_lines(lines)]
    return prepare_data(tags, attrs, text)
