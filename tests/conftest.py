import os
import sys
import pytest
import pandas as pd

sys.path.append(os.path.realpath('..'))
from src import Cleaner, Explorer, CONV_model, LSTM_model, GRU_model, GridSearch

@pytest.fixture
def clear_sentences():
    c = Cleaner()
    return c.clear_sentences

@pytest.fixture
def explorer():
    data = pd.read_csv("test_data.csv")
    explorer = Explorer(data)
    return explorer

@pytest.fixture
def conv_model():
    return CONV_model(64, 64, 0.3, 50, 6)

@pytest.fixture
def gru_model():
    return GRU_model(64, 64, 0.3, 50, 6)

@pytest.fixture
def lstm_model():
    return LSTM_model(64, 64, 0.3, 50, 6)