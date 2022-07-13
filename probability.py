import spacy
import sys
from collections import defaultdict
import numpy


nlp = spacy.load('en_core_web_sm')

doc = "Apple is a great New York product."

scores = numpy.zeros((len(doc), nlp.entity.model.nr_class))
with nlp.entity.step_through(doc) as state:
    while not state.is_final:
        action = state.predict()
        next_tokens = state.queue
        scores[next_tokens[0].i] = state.scores
        state.transition(action)