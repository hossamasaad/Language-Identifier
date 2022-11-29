from tensorflow.keras.layers import Embedding, GlobalMaxPooling1D, Conv1D, Dense, Dropout
from tensorflow.keras.models import Sequential

def CONV_model(units, emb_dim, dropout, total_words, max_len):
    """
        Try using a convelution layer instead of RNN
        Arguments:
            units(int): number of Conv units
            emb_dim(int): number of embedding dimention to represent a word
            dropout(float): droput ratio 
        Return
            CONV model
    """
    model = Sequential([
        Embedding(total_words, emb_dim, input_length=max_len),
        Conv1D(units, 5, activation='relu'),
        GlobalMaxPooling1D(),
        Dense(32, activation='relu'),
        Dropout(dropout),
        Dense(16, activation='softmax')
    ])
    return model