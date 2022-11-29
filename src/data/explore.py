import random

class Explorer:

    def __init__(self, data) -> None:
        self.data = data
        self.sentences, self.labels = self._split_data() 
    
    
    def _split_data(self):
        """
        Split data to sentences and labels

        Args:
            Data (dataframe): data to split
        Returns
            Tuple (sentences, labels)
        """
        return self.data['Text'], self.data['Language']


    def show_sentences(self, n):
        """
        get some random sentence from data
        Args:
            sentences(series, list): all sentences
            labels(series, list): language in which sentences were written
            n(int): number of sentences to print 
        """
        indecies_list = random.sample(range(0, len(self.sentences)), n)

        for idx in indecies_list:
            print('Text:', self.sentences[idx])
            print('Langauge:', self.labels[idx])
            print('--------------------------------------------------------------------------------')


    def get_longest_length(self):
        """
        Get longest length of list of sentence
        Args:
            sentences (list): Sentences to get longest one length
        Return
            longest_len (int): Longest sentence length 
        """
        longest_len = 0
        for text in self.sentences:
            longest_len = max(longest_len, len(text.split()))
        return longest_len
    

    def get_sentences_and_labels(self):
        """
        Return sentences and labels

        Returns:
            Sentences, Labels
        """
        return self.sentences, self.labels