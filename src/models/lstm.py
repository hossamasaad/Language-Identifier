from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential

# LSTM model
def LSTM_model(units, emb_dim, dropout, total_words, max_len):
    """
        LSTM Model
        Arguments:
            units(int): number of LSTM units
            emb_dim(int): number of embedding dimention to represent a word
            dropout(float): droput ratio 
        Return
            LSTM model
    """
    model = Sequential([
        Embedding(total_words, emb_dim, input_length=max_len),
        Bidirectional(LSTM(units)),
        Dense(32, activation='relu'),
        Dropout(dropout),
        Dense(16, activation='softmax')
    ])
    return model