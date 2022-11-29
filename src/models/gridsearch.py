class GridSearch:
    def __init__(self, model, grid, total_words, max_len) -> None:
        self.model = model
        self.grid = grid
        self.total_words = total_words
        self.max_len = max_len
        self._best = None

    def fit(self, X_train, y_train, X_valid, y_valid, epochs=10):
        
        for units in self.grid['units']:
            for emb in self.grid['emb_dim']:
                for dropout in self.grid['dropout']:
                    model = self.model(units, emb, dropout, self.total_words, self.max_len)
                    model.summary()
                    print("Start training model....")
                    
                    model.compile(
                        loss='categorical_crossentropy',
                        optimizer='adam',
                        metrics=['accuracy'],
                    )

                    history = model.fit(
                        X_train,
                        y_train,
                        epochs=epochs,
                        validation_data=(X_valid, y_valid),
                        verbose = 1
                    )

                    if history.history['val_accuracy'][-1] > self._best.history['val_accuracy'][-1]:
                        self._best = history
                    
                    print("Training Finished")
                    print("accuracy     :{} ".format(history.history['accuracy'    ][-1]))
                    print("val_accuracy :{} ".format(history.history['val_accuracy'][-1]))
                    print("loss         :{} ".format(history.history['loss'        ][-1]))
                    print("val_loss     :{} ".format(history.history['val_loss'    ][-1]))
        
    def get_best(self):
        return self._best