# coding: utf8
from __future__ import unicode_literals

from ...attrs import LIKE_NUM


_num_words = [
    "sero",
    "un",
    "dos",
    "tres",
    "kuatro","kuater",
    "sinko","sinku",
    "seis",
    "shete",
    "ocho",
    "nuebe",
    "dies","djes",
    "diesun","djesun",
    "diesdos","djesdos",
    "diestres","djestres",
    "dieskuater","dieskuater",
    "djesinko","djesinku",
    "dieseis","djeseis",
    "dieshete","djeshete",
    "disocho","djesocho",
    "diesnuebe","djesnuebe",
    "binti",
    "trinta",
    "kuarenta",
    "sinkuenta",
    "sesenta",
    "setenta",
    "ochenta",
    "nobenta",
    "shen",
    "mil",
    "mion",
]


_ordinal_words = [
    "promé",
]


def like_num(text):
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text.lower() in _num_words:
        return True
    if text.lower() in _ordinal_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
