from gensim.models import KeyedVectors
from shorttext.classifiers import SumEmbeddedVecClassifier

# load the word embedding model
model = KeyedVectors.load_word2vec_format('glove.6B.100d.25k.word2vec.txt', binary=False)

classifier = SumEmbeddedVecClassifier(model)

data = {
    'fruit': ['apple', 'banana', 'orange'],
    'animal': ['cat', 'dog', 'rabbit'],
    'color': ['red', 'blue', 'green']
}

classifier.train(data)

# get similarity scores for each category
result = classifier.score('I like eating an apple')
print(result)
# print the highest score
print(max(result, key=result.get))

# save the trained classifier
classifier.save_compact_model("new_model.bin")
