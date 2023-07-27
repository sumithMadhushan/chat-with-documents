import spacy

# Load a larger pipeline with vectors
nlp = spacy.load("en_core_web_lg")


print("==================================================================")
print("                 Inspecting word vectors")
print("==================================================================")

# Process a text
doc3 = nlp("Two bananas in pyjamas")
print("Input : Two bananas in pyjamas")
# Get the vector for the token "bananas"
bananas_vector = doc3[1].vector
print("bananas_vector", bananas_vector)

print("==================================================================")
print("                  Similarity examples (1)               ")
print("==================================================================\n")

# Compare two documents
doc1 = nlp("I like fast food")
doc2 = nlp("I like pizza")

print("Input Text 1: I like fast food \nInput Text 2: I like pizza\n")
print(doc1.similarity(doc2))

print("Here, a fairly high similarity score of 0.86 is predicted for ""I like fast food"" and ""I like pizza"".\n")

print("Input : I like pizza and pasta\n")
# Compare two tokens
doc = nlp("I like pizza and pasta")
token1 = doc[2]
token2 = doc[4]
print(token1.similarity(token2))


print("According to the word vectors, the tokens ""pizza"" and ""pasta"" are kind of similar, and receive a score of 0.7.\n")


