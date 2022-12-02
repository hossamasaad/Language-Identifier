import pytest

class Testcleaner:

    def test_clear_sentences(self, clear_sentences):
        sentence = ["Two boys, playing with a ball", "Hello from the OTHER side!!!!!"]
        cleared = ["two boys playing with ball", "hello from the other side"]
        assert cleared == clear_sentences(sentence)

class TestExplorer:

    def test_get_longest_length(self, explorer):
        assert explorer.get_longest_length() == 6
    
    def test_get_sentences_and_labels(self, explorer):
        sentences, labels = explorer.get_sentences_and_labels()
        assert len(sentences) == 3
        assert sentences[0] == 'hello world'
        assert labels[0] == 'English'