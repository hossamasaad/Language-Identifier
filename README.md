# Language Identifier
![GitHub repo size](https://img.shields.io/github/repo-size/hossamasaad/Language-Identifier)
![GitHub contributors](https://img.shields.io/github/contributors/hossamasaad/Language-Identifier)
![GitHub stars](https://img.shields.io/github/stars/hossamasaad/Language-Identifier?style=social)
![GitHub forks](https://img.shields.io/github/forks/hossamasaad/Language-Identifier?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hossamasaad10?style=social)

The goal of this project is to create a model that is able to predict a given sentence language through text processing,  including tokenizing and representation of sentences as vectors and applying concepts such as RNN, LSTM and GRU to create the classifier that can detect the language among 16 languages.

## Dataset
[Language Detection](https://www.kaggle.com/basilb2s/language-detection) It's a small language detection dataset. This dataset consists of text details for 16 different languages
<br />
<img src="https://github.com/hossamasaad/Language-Identifier/blob/main/reports/figures/langauges_count.png" width="490"> <img src="https://github.com/hossamasaad/Language-Identifier/blob/main/reports/figures/lanuages_pie.png" width="340">


## Project Structure
```
.
├── LICENSE
├── requirements.txt
├── README.md
├── data
│   ├── processed
│   │   ├── labels.pkl
│   │   ├── train_labels.pkl
│   │   ├── train_padded.pkl
│   │   ├── valid_labels.pkl
│   │   └── valid_padded.pkl
│   └── raw
│       └── Language Detection.csv
├── models
│   ├── meta.tsv
│   ├── vecs.tsv
│   ├── best_conv.pkl
│   ├── best_gru.pkl
│   ├── best_lstm.pkl
│   ├── conv_history.pkl
│   ├── gru_history.pkl
│   └── lstm_history.pkl
├── notebooks
│   └── Language Identifier.ipynb
├── reports
│   └── figures
│       ├── conv1d_accuracy.png
│       ├── conv1d_loss.png
│       ├── conv_accuracy.png
│       ├── conv_confusion_matrix.png
│       ├── conv_loss.png
│       ├── gru_accuracy.png
│       ├── gru_confusion_matrix.png
│       ├── gru_loss.png
│       ├── langauges_count.png
│       ├── lanuages_pie.png
│       ├── lstm_accuracy.png
│       ├── lstm_confusion_matrix.png
│       └── lstm_loss.png
├── src
│   ├── __init__.py
│   ├── features
│   ├── data
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   └── explore.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── gru.py
│   │   ├── lstm.py
│   │   ├── conv1d.py
│   │   └── gridsearch.py
│   └── visualization
│       ├── __init__.py
│       ├── graphs.py
│       └── visualize.py
└── tests
```

## Model Archtichtures


## Results
- All models achieved high accuracy even when using one convolution layer instead of LSTM or GRU, But GRU achieved highest accuracy 99.6% training accuracy 96.5% validation accuracy.
- Using LSTM achieved high accuracy about 96.87% validation accuracy  
- Using fewer embedding dimensions makes the model reach high accuracy faster but in Embedding Projector alot of words grouped with other languages.

### 32 Embedding dimensions examples

![image](https://user-images.githubusercontent.com/40635600/154850829-83a647c9-cb9f-4309-a70f-30b56f2aa672.png)
![image](https://user-images.githubusercontent.com/40635600/154850851-52c50dba-9e70-43ce-94fb-71d0b78e587f.png)

### 3 Embedding dimensions examples

![image](https://user-images.githubusercontent.com/40635600/154851278-204897f7-b175-49ad-bc5a-1de80b4c0118.png)
![image](https://user-images.githubusercontent.com/40635600/154851317-3983482c-8d54-41b2-8240-ab300c5c75f9.png)

### LSTM Accuracy and Loss
<img src="https://github.com/hossamasaad/Language-Identifier/blob/main/reports/figures/lstm_accuracy.png" width="400"> <img src="https://github.com/hossamasaad/Language-Identifier/blob/main/reports/figures/lstm_loss.png" width="400">



### LSTM Confusion matrix
![image](https://github.com/hossamasaad/Language-Identifier/blob/main/reports/figures/lstm_confusion_matrix.png)


## Contributing to Langauge Identifier

To contribute to Langauge Identifier, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).



## Tools
- Python
- Tensorflow
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
- seaborn
- pytest
