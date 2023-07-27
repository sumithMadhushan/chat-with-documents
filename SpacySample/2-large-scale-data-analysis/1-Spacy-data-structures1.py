import spacy

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")


nlp.vocab.strings.add("coffee") #spaCy stores all shared data in a vocabulary, the Vocab.

coffee_hash = nlp.vocab.strings["coffee"]
coffee_string = nlp.vocab.strings[coffee_hash]

print("==================================================================")
print("           Shared vocab and string store (1)")
print("==================================================================\n")


print("hash value:", coffee_hash)
print("string value:", coffee_string)

print("==================================================================")
print("           Shared vocab and string store (2)")
print("==================================================================\n")


doc = nlp("I love coffee")
print("hash value love :", nlp.vocab.strings["love"])
print("hash value coffee :", doc.vocab.strings["coffee"])
print("string value 3702023516439754181 :", nlp.vocab.strings[3702023516439754181])


print("==================================================================")
print("           Lexemes: entries in the vocabulary                     ")
print("==================================================================\n")

doc = nlp("I love coffee")
lexeme = nlp.vocab["coffee"]

# Print the lexical attributes
print(lexeme.text, lexeme.orth, lexeme.is_alpha)