class TestModels:

    def test_conv_model(self, conv_model):
        assert conv_model.layers[0].name[:9] == 'embedding'
        assert conv_model.layers[1].filters  == 64
        assert str(conv_model.layers[3].activation)[10:14] == 'relu'
    
    def test_gru_model(self, gru_model):
        assert gru_model.layers[0].name[:9]  == 'embedding'
        assert gru_model.layers[1].name[:13] == 'bidirectional'
        assert gru_model.layers[3].rate == 0.3
    
    def test_lstm_model(self, lstm_model):
        assert lstm_model.layers[0].name[:9]  == 'embedding'
        assert lstm_model.layers[1].name[:13] == 'bidirectional'
        assert lstm_model.layers[3].rate == 0.3