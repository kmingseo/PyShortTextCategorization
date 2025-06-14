# Short Text Mining in Python


## 📌 Goal

PyShortTextCategorization is a Python package that supports supervised and unsupervised short text classification. 
It utilizes intermediate representation techniques such as topic modeling and word embeddings to address the sparsity and lack of information inherent in short texts.

- Update Keras imports to tensorflow.keras to ensure compatibility and avoid conflicts in TensorFlow 2.x environments.
- Replaced prints with logging for better log management.
- Added choices in argparse to validate embedding types.
- Improved argument descriptions and inpu-t validation.
- Enhanced console input handling with whitespace stripping and clean exit.
- Used f-strings for clearer output formatting.
- Added if name == "main": guard for proper script execution.

<br/><br/>


## 📌 Requirements


- python==3.10
- numpy==1.26.4 
- scipy==1.13.1
- joblib==1.5.1 
- scikit-learn==1.6.1 
- tensorflow-cpu==2.19.0 
- keras==3.10.0 
- gensim==4.3.3 
- pandas==2.2.3 
- snowballstemmer==3.0.1 
- transformers==4.52.3 
- torch==2.7.0 
- numba==0.61.2 
- shorttext==2.1.1

<br/><br/>


## 📌 How to install & run

### Download and install the docker image

Load an image from a tar file 
```
docker load -i final_2023040014:v1.tar
```

Check loaded image
```
docker images
```

### Create and run a Docker container

Run the container
```
docker run -dit final_2023040014:v1
```

Find container
```
docker ps
```

Access the container
```
docker exec -it <CONTAINER_ID> /bin/bash
```

<br/><br/>


## 📌 How to run
(After entering the project root directory inside the container, run the following commands) 

### NOTE: 
The file test.py is a sample script provided for demonstration purposes. <br/>
It shows how to use the package for short text categorization with a pre-trained embedding file (glove.6B.100d.25k.word2vec.txt).

In the file test.py,
if you want to train the classifier with different sentences, <br/> 
simply modify the example words in each category within the data dictionary or the input sentence. <br/>
You can also add more categories. 

To test the classifier with different sentences using the CLI, simply modify the value of the --inputtext option in the command.

### 1. Run the test script
```
python test.py
```

### Expected Output
```
{'fruit': 0.6626538015879517, 'animal': 0.5442677398027801, 'color': 0.5905815856817532}

fruit
```

### 2. Run the CLI categorization tool
```
python -m shorttext.cli.categorization \
  new_model.bin \
  --wv glove.6B.100d.25k.word2vec.txt \
  --type word2vec_nonbinary \
  --inputtext "I like eating an apple"
```

### Expected Output
```
fruit : 0.6627
color : 0.5906
animal : 0.5443
```

<br/><br/>


## 📌 Project Directory Structure
```
PyShortTextCategorization/
├── .circleci/                       # Continuous Integration configuration
├── docs/                            
├── shorttext/                       # Main Python package source code
│   ├── classifiers/                 
│   ├── cli/                         # Command-line interface modules
│   │   ├── __init__.py
│   │   ├── categorization.py        # CLI for text categorization
│   │   ├── wordembedsim.py          
│   ├── data/                        
│   ├── generators/                  
│   ├── metrics/                    
│   ├── spell/                       
│   ├── stack/                       
│   ├── utils/                     
│   ├── __init__.py
│   └── smartload.py                
├── test/                            # Unit tests
├── .gitignore
├── .readthedocs.yml                 
├── LICENSE
├── MANIFEST.in                      
├── README.md                        # Project overview and usage instructions
├── glove.6B.100d.25k.word2vec.txt   # Pre-trained word embedding for testing
├── pyproject.toml                   
└── test.py                          # Sample script for testing
```


<br/><br/>


## 📌 How to Stop and Clean Up

### 1. To stop and exit
```
Ctrl + D
or
exit (typing)
```

### 2. Stop the container
```
docker stop <CONTAINER_ID>
```

### 3. Remove the container
```
docker rm <CONTAINER_ID>
```

### 4. Remove Docker image
```
docker rmi <image_name>
```

<br/><br/>

## 📌LICENSE

MIT © Viva Republica, Inc. See the LICENSE file (https://github.com/stephenhky/PyShortTextCategorization/blob/master/LICENSE) for details.
