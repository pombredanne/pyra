# Load what we actually need to run the tests
import unittest
from pyra.iindex import InvertedIndex, INF

class TestInvertedIndex(unittest.TestCase):

    def setUp(self):
        pass

    def test_trivial_corpus(self):
        corpus = "the quick brown fox jumps over the lazy dog and the brown dog runs away"
        tokens = corpus.split()
        iidx   = InvertedIndex(tokens)

        self.assertEqual(iidx.first('dog'),                                 8)
        self.assertEqual(iidx.last('dog'),                                  12)
        self.assertEqual(iidx.next('dog', 8),                               12)
        self.assertEqual(iidx.prev('dog', 12),                              8)
        self.assertEqual(iidx.first('cat'),                                 INF)
        self.assertEqual(iidx.last('cat'),                                 -INF)
        self.assertEqual(iidx.next('cat', 8),                               INF)
        self.assertEqual(iidx.prev('cat', 12),                             -INF)
        self.assertEqual(iidx.first('fox'),                                 3)
        self.assertEqual(iidx.last('fox'),                                  3)
        self.assertEqual(iidx.postings_count('dog', -INF, INF),             2)
        self.assertEqual(iidx.postings_count('dog', -INF, 9),               1)
        self.assertEqual(iidx.postings_count('dog', -INF, 8),               1)
        self.assertEqual(iidx.postings_count('dog', -INF, 7),               0)
        self.assertEqual(iidx.postings_count('dog', 7, 13),                 2)
        self.assertEqual(iidx.postings_count('dog', 8, 12),                 2)
        self.assertEqual(iidx.postings_count('dog', 12, INF),               1)
        self.assertEqual(iidx.postings_count('dog', 13, 14),                0)
        self.assertEqual(iidx.postings('dog', -INF, INF),                   [8, 12])
        self.assertEqual(iidx.postings('dog', -INF, 9),                     [8])
        self.assertEqual(iidx.postings('dog', -INF, 8),                     [8])
        self.assertEqual(iidx.postings('dog', -INF, 7),                     [])
        self.assertEqual(iidx.postings('dog', 7, 13),                       [8,12])
        self.assertEqual(iidx.postings('dog', 8, 12),                       [8,12])
        self.assertEqual(iidx.postings('dog', 12, INF),                     [12])
        self.assertEqual(iidx.postings('dog', 13, 14),                      [])
        self.assertEqual(iidx.dictionary() ^ set(tokens),                   set())
