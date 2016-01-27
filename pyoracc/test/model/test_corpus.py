from ...model.corpus import Corpus
from nose.tools import assert_in, assert_equal

from ..fixtures import tiny_corpus, sample_corpus, whole_corpus


def test_tiny():
    corpus = Corpus(source=whole_corpus())
    assert_equal(corpus.successes, 1)
    assert_equal(corpus.failures, 1)
