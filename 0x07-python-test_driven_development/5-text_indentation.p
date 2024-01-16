#!/usr/bin/python3

"""a function that prints a text with 2 new lines after
each of these characters: ., ? and :"""


def text_indentation(text):
    """if text is not a string raise an error"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    result = text.replace(':',':'+'\n'*2)
    result = result.replace('?','?'+'\n'*2)
    result = result.replace('.','.'+'\n'*2)
    return print(result)
text_indentation("""a function that prints a text with 2 new lines after
each of these characters: ., ? and :""")