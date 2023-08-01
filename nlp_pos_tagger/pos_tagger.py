from nltk import pos_tag, word_tokenize
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_full_pos_tag(tag):
    tag_dict = {
        'CC': 'Coordinating conjunction',
        'CD': 'Cardinal number',
        'DT': 'Determiner',
        'EX': 'Existential there',
        'FW': 'Foreign word',
        'IN': 'Preposition or subordinating conjunction',
        'JJ': 'Adjective',
        'JJR': 'Adjective, comparative',
        'JJS': 'Adjective, superlative',
        'LS': 'List item marker',
        'MD': 'Modal',
        'NN': 'Noun, singular or mass',
        'NNS': 'Noun, plural',
        'NNP': 'Proper noun, singular',
        'NNPS': 'Proper noun, plural',
        'PDT': 'Predeterminer',
        'POS': 'Possessive ending',
        'PRP': 'Personal pronoun',
        'PRP$': 'Possessive pronoun',
        'RB': 'Adverb',
        'RBR': 'Adverb, comparative',
        'RBS': 'Adverb, superlative',
        'RP': 'Particle',
        'SYM': 'Symbol',
        'TO': 'to',
        'UH': 'Interjection',
        'VB': 'Verb, base form',
        'VBD': 'Verb, past tense',
        'VBG': 'Verb, gerund or present participle',
        'VBN': 'Verb, past participle',
        'VBP': 'Verb, non-3rd person singular present',
        'VBZ': 'Verb, 3rd person singular present',
        'WDT': 'Wh-determiner',
        'WP': 'Wh-pronoun',
        'WP$': 'Possessive wh-pronoun',
        'WRB': 'Wh-adverb'
    }

    return tag_dict.get(tag, 'Other')

def pos_tag_text(text):
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)

    tagged_tokens_with_full_pos = []

    for token, tag in tagged_tokens:
        if token.isnumeric():
            full_tag = 'Numeral'
        elif tag == 'PRP':
            full_tag = 'Personal pronoun'
        elif token.isalpha() and token.istitle():
            full_tag = 'Proper noun, singular'
        else:
            full_tag = get_full_pos_tag(tag)
        
        tagged_tokens_with_full_pos.append((token, tag, full_tag))

    return tagged_tokens_with_full_pos
