from tensorflow.keras.layers import Embedding, Bidirectional, GRU, Dense, Dropout
from tensorflow.keras.models import Sequential

def GRU_model(units, emb_dim, dropout, total_words, max_len):
    """
        GRU Model
        Arguments:
            units(int): number of GRU units
            emb_dim(int): number of embedding dimention to represent a word
            dropout(float): droput ratio 
        Return
            GRU model
    """
    model = Sequential([
        Embedding(total_words, emb_dim, input_length=max_len),
        Bidirectional(GRU(units)),
        Dense(32, activation='relu'),
        Dropout(dropout),
        Dense(16, activation='softmax')
    ])
    return model