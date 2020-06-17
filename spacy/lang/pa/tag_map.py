# coding: utf8
from __future__ import unicode_literals

from ...symbols import POS, PUNCT, SYM, ADJ, CCONJ, NUM, DET, ADV, ADP, X, VERB
from ...symbols import NOUN, PROPN, PART, INTJ, SPACE, PRON

# WARNING. This is currently the English TAG_MAP
# and needs to be fixed for Papiamento.
#
# If you can do this or can advise on how to do this
# Create issues first and submit your changes


TAG_MAP = {
    ".": {POS: PUNCT, "PunctType": "peri"},
    ",": {POS: PUNCT, "PunctType": "comm"},
    "-LRB-": {POS: PUNCT, "PunctType": "brck", "PunctSide": "ini"},
    "-RRB-": {POS: PUNCT, "PunctType": "brck", "PunctSide": "fin"},
    "``": {POS: PUNCT, "PunctType": "quot", "PunctSide": "ini"},
    '""': {POS: PUNCT, "PunctType": "quot", "PunctSide": "fin"},
    "''": {POS: PUNCT, "PunctType": "quot", "PunctSide": "fin"},
    ":": {POS: PUNCT},
    "$": {POS: SYM},
    "#": {POS: SYM},
    "AFX": {POS: ADJ, "Hyph": "yes"},
    "CC": {POS: CCONJ, "ConjType": "comp"},
    "CD": {POS: NUM, "NumType": "card"},
    "DT": {POS: DET},
    "EX": {POS: PRON, "AdvType": "ex"},
    "FW": {POS: X, "Foreign": "yes"},
    "HYPH": {POS: PUNCT, "PunctType": "dash"},
    "IN": {POS: ADP},
    "JJ": {POS: ADJ, "Degree": "pos"},
    "JJR": {POS: ADJ, "Degree": "comp"},
    "JJS": {POS: ADJ, "Degree": "sup"},
    "LS": {POS: X, "NumType": "ord"},
    "MD": {POS: VERB, "VerbType": "mod"},
    "NIL": {POS: X},
    "NN": {POS: NOUN, "Number": "sing"},
    "NNP": {POS: PROPN, "NounType": "prop", "Number": "sing"},
    "NNPS": {POS: PROPN, "NounType": "prop", "Number": "plur"},
    "NNS": {POS: NOUN, "Number": "plur"},
    "PDT": {POS: DET},
    "POS": {POS: PART, "Poss": "yes"},
    "PRP": {POS: PRON, "PronType": "prs"},
    "PRP$": {POS: DET, "PronType": "prs", "Poss": "yes"},
    "RB": {POS: ADV, "Degree": "pos"},
    "RBR": {POS: ADV, "Degree": "comp"},
    "RBS": {POS: ADV, "Degree": "sup"},
    "RP": {POS: ADP},
    "SP": {POS: SPACE},
    "SYM": {POS: SYM},
    "TO": {POS: PART, "PartType": "inf", "VerbForm": "inf"},
    "UH": {POS: INTJ},
    "VB": {POS: VERB, "VerbForm": "inf"},
    "VBD": {POS: VERB, "VerbForm": "fin", "Tense": "past"},
    "VBG": {POS: VERB, "VerbForm": "part", "Tense": "pres", "Aspect": "prog"},
    "VBN": {POS: VERB, "VerbForm": "part", "Tense": "past", "Aspect": "perf"},
    "VBP": {POS: VERB, "VerbForm": "fin", "Tense": "pres"},
    "VBZ": {
        POS: VERB,
        "VerbForm": "fin",
        "Tense": "pres",
        "Number": "sing",
        "Person": "three",
    },
    "WDT": {POS: DET},
    "WP": {POS: PRON},
    "WP$": {POS: DET, "Poss": "yes"},
    "WRB": {POS: ADV},
    "ADD": {POS: X},
    "NFP": {POS: PUNCT},
    "GW": {POS: X},
    "XX": {POS: X},
    "BES": {POS: VERB},
    "HVS": {POS: VERB},
    "_SP": {POS: SPACE},
}