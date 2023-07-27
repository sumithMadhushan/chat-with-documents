# Named entities are "real world objects" that are assigned a name
# For example, a person, an organization or a country

# ents - named entity recognition model

import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Process a text
doc = nlp("Apple is looking at buying U.K. startup for $1 billion in December 2023")


print("Apple is looking at buying U.K. startup for $1 billion in December 2023\n")

# Iterate over the predicted entities
for ent in doc.ents:  # .ents property lets you access the named entities predicted
    # Print the entity text and its label
    print(ent.text, "-", ent.label_)
print("")
print("")
print("=============================================")

# Get quick definitions of the most common tags and labels.
print("Definitions of the most common tags and labels")
print("=============================================\n")
print("")

print("ORG Definition - ", spacy.explain("ORG"))
print("GPE Definition - ", spacy.explain("GPE"))
print("NNP Definition - ", spacy.explain("NNP"))
print("dobj Definition - ", spacy.explain("dobj"))
print("")