# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH

# Main purpose of an extensive list: considerably improved sentence
# segmentation.
#
# If you can do this or can advise on how to do this
# Create issues first and submit your changes

abbrevs = [
    "Sen.",
    "Sr.",
    "sr.",
    "Sra.",
    "sra.",
]

_exc = {}
for orth in abbrevs:
    _exc[orth] = [{ORTH: orth}]
    uppered = orth.upper()
    capsed = orth.capitalize()
    for i in [uppered, capsed]:
        _exc[i] = [{ORTH: i}]


TOKENIZER_EXCEPTIONS = _exc
