# coding: utf8
from __future__ import unicode_literals

# In order to achieve parity with some of the better-supported
# languages, e.g., English, French, and German, this list should be
# extended
# Tokens whose status as a stop word is not entirely clear should be
# rejected by deferring to their counterparts in the stop words lists for English
# and French. Similarly, those lists can be used to identify and fill in gaps so
# that -- in principle -- each token contained in the English stop words list
# should have a Papiamento counterpart here.


STOP_WORDS = set(
    """
y di cu a é el qu su
""".split()
)

contractions = ["'é", "'i"]
STOP_WORDS.update(contractions)
