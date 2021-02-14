#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of
    html validation by checking whether
    every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''
    tags = _extract_tags(html)
    opentags = []
    if html == '':
        return True
    elif tags == []:
        return False
    else:
        for tag in tags:
            if '/' not in tag:
                opentags.append(tag)
            else:
                if len(opentags) == 0:
                    return False
                strippedcloseTag = tag[2:-1]
                strippedopenTag = opentags[-1][1:-1]
                if strippedopentag == strippedclosetag:
                    opentags.pop()
        if len(opentags) == 0:
            return True
        else:
            return False
    # HINT:
    # use the _extract_tags function below to generate a list
    # of html tags without any extra text;
    # then process these html tags using the balanced
    # parentheses algorithm from the class/book
    # the main difference between your code and
    # the code from class will
    # be that you will have to keep track
    # of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def _extract_tags(html):
    '''
    This is a helper function for validate_html.
    By convention in Python, helper functions that are not meant
    to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags
    contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    final_list = []
    tags = ''
    x = False
    for i in html:
        if i == '<':
            x = True
            tags += i
        elif i == '>':
            x = False
            tags += i
            final_list += [tags]
            tags = ''
        else:
            if x is True:
                tags += i
    return final_list
