from nltk import pos_tag, word_tokenize
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def pos_tag_text(text):
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tagged_tokens = pos_tag(tokens)
    return tagged_tokens
