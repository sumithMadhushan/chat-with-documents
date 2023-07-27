import spacy

# Import the Matcher
from spacy.matcher import Matcher

# Load a pipeline and create the nlp object
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab
# The matcher is initialized with the shared vocabulary, nlp.vocab
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher
# The matcher.add method lets you add a pattern.
# The first argument is a unique ID to identify which pattern was matched. 
# The second argument is a list of patterns.

pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Process some text
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc
matches = matcher(doc)

print("=====================================================")
print("      Rule-based matching - Using the Matcher (1)    ")
print("=====================================================\n")


# Iterate over the matches
for match_id, start, end in matches:
    # Get the matched span
    matched_span = doc[start:end]
    print(matched_span.text)


# match_id: hash value of the pattern name
# start: start index of matched span
# end: end index of matched span

print("\n=====================================================")
print("             Matching lexical attributes (DIGIT)       ")
print("=====================================================\n")


pattern2 = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]

matcher.add("Is Digit Pattern", [pattern2])
doc2 = nlp("2018 FIFA World Cup: France won!")

matches2 = matcher(doc2)

# Iterate over the matches
for match_id, start, end in matches2:
    # Get the matched span
    matched_span = doc2[start:end]
    print(matched_span.text)

print("")


print("\n=====================================================")
print("             Using operators and quantifiers       ")
print("=====================================================\n")

print("  Example                         Description ")
print("-----------------------------------------------")
print("  "'{"OP": "!"}'"                 Negation: match 0 times             ")
print("  "'{"OP": "?"}'"                 Optional: match 0 or 1 times        ")
print("  "'{"OP": "+"}'"                 Match 1 or more times               ")
print("  "'{"OP": "*"}'"                 Match 0 or more times        \n")

pattern3 = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
    {"POS": "NOUN"}
]

matcher.add("Operator Pattern", [pattern3])
doc3 = nlp("I bought a smartphone. Now I'm buying startup apps.")

matches3 = matcher(doc3)

# Iterate over the matches
for match_id, start, end in matches3:
    # Get the matched span
    matched_span = doc3[start:end]
    print(matched_span.text)

print("")