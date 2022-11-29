class GridSearch:

    def __init__(self, model, grid, total_words, max_len) -> None:
        """
        Construct a grid search
        Args:
            model: model archticture
            grid : grid paramteres to try
            total_Words: just total words
            max_len : maximum sentence length
        """

        self.model = model
        self.grid = grid
        self.total_words = total_words
        self.max_len = max_len
        self.best_history = None
        self.best_model = None


    def fit(self, X_train, y_train, X_valid, y_valid, epochs=10):
        """
        Start fitting diffrent models using grid hyperparamters
        Args:
            X_train: training sentences
            y_train: training labels
            X_valid: validation sentences
            y_valid: validation labels
            epochs : number of epochs 
        """
        for units in self.grid['units']:
            for emb in self.grid['emb_dim']:
                for dropout in self.grid['dropout']:
                    model = self.model(units, emb, dropout, self.total_words, self.max_len)
                    model.summary()
                    print("Start training model(units={}, embedding dimensions={}, dropout={})....".format(units, emb, dropout))
                    
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
                    print(type(model))
                    
                    if self.best_history is None:
                        self.best_history = history
                        self.best_model = model

                    if history.history['val_accuracy'][-1] > self.best_history.history['val_accuracy'][-1]:
                        self.best_history = history
                        self.best_model = model
                    
                    print("Training Finished")
                    print("accuracy     :{} ".format(history.history['accuracy'    ][-1]))
                    print("val_accuracy :{} ".format(history.history['val_accuracy'][-1]))
                    print("loss         :{} ".format(history.history['loss'        ][-1]))
                    print("val_loss     :{} ".format(history.history['val_loss'    ][-1]))
        
    def get_best(self):
        """
        Get the best model
        Returns:
            best_model: the best model
        """
        return self.best_model