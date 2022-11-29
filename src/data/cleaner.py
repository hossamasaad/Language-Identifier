import re

class Cleaner:

    def __init__(self) -> None:
        pass

    def clear_sentences(self, sentences):
        """
        Clear symbols, numbers and single letters from sentences
        Arguments:
            sentences(series, list): sentences to clear
        Return:
            new_sentences(list): cleared sentences
        """
        new_sentences = []
        for sentence in sentences:
            # removing symbols and numbers
            sentence = re.sub(r'[!@#.$(),"%^*?:;~`0-9]', ' ', sentence)
            sentence = re.sub(r'[[]]', ' ', sentence)

            # removing single letters
            sentence = ' '.join( [w for w in sentence.split() if len(w)>1] )

            # conver to lower case
            sentence = sentence.lower()

            # append to new texts
            new_sentences.append(sentence)
        
        return new_sentences