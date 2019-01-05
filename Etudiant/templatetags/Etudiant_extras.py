from random import randint
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django import template
from django.template.base import VariableDoesNotExist

register = template.Library()


@register.filter(is_safe=True)
def citation(text):
    res = "&laquo; {} &raquo;".format(escape(text))
    return mark_safe(res)


@register.filter(is_safe=True, nema='smart_trunc')
def smart_truncat(text, nb_char):
    # Verifion si l nb_char est un entier et existe
    try:
        nb_char= int(nb_char)
    except ValueError:
        return text

    if len(text)<= nb_char:
        return text

    text= text[:nb_char+1]

    if text[-1:]!= ' ':
        mots= text.split('  ')[:-1]
        text= ' '.join(mots)
    else:
        return text[:-1]

    return text+'...'


@register.tag
def random(parser, token):
    try:
        mon_tag, begin, end = token.split_contents('')
    except (VariableDoesNotExist, ValueError):
        msg = """le tag %s prend exactement
        deux para""" % token.split_contents('')[0]
        raise template.TemplateSyntaxError(msg)

    try:
        begin, end = int(begin), int(end)
    except ValueError:
        msg = """les argument du tag %s doit oblig
        etre des entiers""" % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    return RandomNode(begin, end)


class RandomNode(template.Node):

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def render(self, context):
        return str(randint(self.begin, self.end))


@register.simple_tag(name='random2', takes_context=True)
def random_simple(context, begin, end):
    try:
        # do something with context here if let's hv to something
        return randint(int(begin), int(end))
    except ValueError:
        raise template.TemplateSyntaxError("""les argumts doivnt etre des
                                           des entier""")
