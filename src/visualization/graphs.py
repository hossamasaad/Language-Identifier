import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from tensorflow.math import confusion_matrix
from sklearn.preprocessing import LabelEncoder

class Graphs:

    def __init__(self, model, history) -> None:
        self.model = model
        self.history = history
        self.labels = joblib.load('/Language-Identifier/data/processed/labels.pkl')
        self.valid_padded = joblib.load('/Language-Identifier/data/processed/valid_padded.pkl')
        self.valid_labels = joblib.load('/Language-Identifier/data/processed/valid_labels.pkl')

    
    def accuracy(self, save_fig = None):
        """
        Plot accuracy graph
        Arguments:
            model: model history
        """

        plt.plot(self.history.history['accuracy'])
        plt.plot(self.history.history['val_accuracy'])
        plt.xlabel("Epochs")
        plt.ylabel('Accuracy')
        plt.legend(['accuracy', 'val_accuracy'])
        if save_fig:
            plt.savefig('/Language-Identifier/reports/figures/{}.png'.format(save_fig))
        
        plt.show()

    def loss(self, save_fig = None):
        """
        Plot loss graph
        Arguments:
            History: model history
        """
        plt.plot(self.history.history['loss'])
        plt.plot(self.history.history['val_loss'])
        plt.xlabel("Epochs")
        plt.ylabel('Loss')
        plt.legend(['loss', 'val_loss'])
        if save_fig:
            plt.savefig('/Language-Identifier/reports/figures/{}.png'.format(save_fig))
        
        plt.show()
    
    def confusion_matrix(self, save_fig=None):
        """
        Show the confusion matrix
        """
        
        y = np.argmax(self.valid_labels, axis=1)                  # real labels    

        y_pred = self.model.predict(self.valid_padded)            # predicted values
        y_pred = np.argmax(y_pred, axis=1)

        cm = confusion_matrix(y, y_pred)                          # confusion matrix

        # get list of langauges name in order
        label_encoder = LabelEncoder()
        vec = label_encoder.fit_transform(self.labels)
        dic = dict(zip(vec, self.labels))
        l = []
        for i in range(16):
            l.append(dic[i])

        # plot confusion matrix
        plt.figure(figsize=(20,20))
        sns.heatmap(cm, annot = True, fmt='g')
        loc = np.array(range(16)) +.5
        plt.xticks(loc, l)
        plt.yticks(loc, l)
        if save_fig:
            plt.savefig('/Language-Identifier/reports/figures/{}.png'.format(save_fig))
        
        plt.show()