import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("She ate the pizza in the evening")

print("==============================")
print("Predicting Part-of-speech Tags")
print("==============================\n")
print("Input Text : She ate the pizza in the evening\n")
# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text,"-", token.pos_) #.pos_ attribute, the predicted part-of-speech tag

print("")
print("Here, the model correctly predicted ""ate"" as a verb and ""pizza"" as a noun.\n")