# Language Identifier

## What is this ?
The goal of this project is to create a model that is able to predict a given sentence language through text processing,  including tokenizing and representation of sentences as vectors and applying concepts such as RNN, LSTM and GRU to create the classifier that can detect the language among 17 languages.

## Dataset
[Language Detection](https://www.kaggle.com/basilb2s/language-detection) It's a small language detection dataset. This dataset consists of text details for 17 different languages

## Results
- All models achieved high accuracy even when using one convolution layer instead of LSTM or GRU, But GRU achieved highest accuracy 99% training accuracy 94% validation accuracy.
- Using convlution layer achieved high accuracy about 95% validation accuracy  
- Using fewer embedding dimensions makes the model reach high accuracy faster but in Embedding Projector alot of words grouped with other languages.


### 32 Embedding dimensions examples

![image](https://user-images.githubusercontent.com/40635600/154850829-83a647c9-cb9f-4309-a70f-30b56f2aa672.png)
![image](https://user-images.githubusercontent.com/40635600/154850851-52c50dba-9e70-43ce-94fb-71d0b78e587f.png)

### 3 Embedding dimensions examples

![image](https://user-images.githubusercontent.com/40635600/154851278-204897f7-b175-49ad-bc5a-1de80b4c0118.png)
![image](https://user-images.githubusercontent.com/40635600/154851317-3983482c-8d54-41b2-8240-ab300c5c75f9.png)

### GRU Accuracy and Loss
![image](https://user-images.githubusercontent.com/40635600/154859735-b9300311-36d6-4111-aeab-ed85f4bb2c6c.png) ![image](https://user-images.githubusercontent.com/40635600/154859778-71eaa682-e989-47c7-9559-f893f3fd7136.png)


### GRU Confusion matrix
![image](https://user-images.githubusercontent.com/40635600/154859743-0e2b42d9-d673-47ab-824f-c2952582663c.png)


## Libraries
- Tensorflow
- Scikit-learn
- NumPy
- Pandas
- Matplotlib
