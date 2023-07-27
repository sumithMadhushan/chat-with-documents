import spacy

# Import the Doc class
from spacy.tokens import Doc, Span


nlp = spacy.blank("en")


print("==================================================================")
print("           Data Structures (2): Doc, Span and Token               ")
print("==================================================================\n")

# It's created automatically when you process a text with the nlp object. 
# But you can also instantiate the class manually.

# The words and spaces to create the doc from
words = ["Hello", "world", "!"]
spaces = [True, False, False]

# Create a doc manually
doc = Doc(nlp.vocab, words=words, spaces=spaces) # This is same as nlp("Hello World!")

print(doc)

print("==================================================================")
print("           Give a label to token            ")
print("==================================================================\n")


# Create a span manually
span = Span(doc, 0, 2)

# Create a span with a label
span_with_label = Span(doc, 0, 2, label="GREETING")

# Add span to the doc.ents
doc.ents = [span_with_label]

print(doc)
# Iterate over the predicted entities
for ent in doc.ents:  # .ents property lets you access the named entities predicted
    # Print the entity text and its label
    print(ent.text, "-", ent.label_)



