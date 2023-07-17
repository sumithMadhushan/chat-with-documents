import spacy
import tensorflow as tf
from transformers import (
    pipeline,
    TFDistilBertForSequenceClassification,
    DistilBertTokenizer,
    TFDistilBertForQuestionAnswering
)


def answer_question(text, question):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    nlp_question = nlp(question)
    sentences = [sent.text for sent in doc.sents]
    context = " ".join(sentences)

    # Use the pre-trained question answering model from Hugging Face - this is a Natural Language Processing
    nlp_qa_model = pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad",
        revision="626af31",
    )

    answer = nlp_qa_model(question=question, context=context)

    return answer["answer"]

def pre_trained_answer_question(context, question):
    model_name = 'distilbert-base-cased-distilled-squad'
    model = TFDistilBertForQuestionAnswering.from_pretrained(model_name)
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
   

    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="tf")
    input_ids = inputs["input_ids"].numpy()[0]
    attention_mask = inputs["attention_mask"].numpy()[0]

    outputs = model(input_ids=tf.constant([input_ids]), attention_mask=tf.constant([attention_mask]))
    answer_start = tf.argmax(outputs.start_logits, axis=1).numpy()[0]
    answer_end = (tf.argmax(outputs.end_logits, axis=1) + 1).numpy()[0]
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return answer

def summarizer(text):
    nlp_summariz_model = pipeline("summarization", model="facebook/bart-large-cnn")
    result = nlp_summariz_model(text, max_length=130, min_length=30, do_sample=False)
    return result


def text_classification(text):
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    model = TFDistilBertForSequenceClassification.from_pretrained(model_name)
    tokenizer = DistilBertTokenizer.from_pretrained(model_name)
    encoded_input = tokenizer(text, truncation=True, padding=True, return_tensors="tf")
    outputs = model(
        encoded_input.input_ids, attention_mask=encoded_input.attention_mask
    )
    predictions = tf.nn.softmax(outputs.logits, axis=1)

    predicted_label = tf.argmax(predictions, axis=1).numpy()[0]

    class_mapping = {0: "Negative", 1: "Positive"}
    predicted_class = class_mapping[predicted_label]
    return predicted_class


# Sample text input
text = (
    "Harry Potter and the Philosopher's Stone is a fantasy novel written by J.K. Rowling. The story follows Harry Potter, "
    "a young wizard who discovers his magical abilities and begins attending Hogwarts School of Witchcraft and Wizardry. "
    "He becomes friends with Ron Weasley and Hermione Granger and together they face various challenges."
)

# Answer a question about the text
question = "Who is the author of Harry Potter and the Philosopher's Stone?"
answer = answer_question(text, question)
print("Answer:", answer)
