import re
import string


def ws_punc_tokenizer(text):
    """
    Tokenizes text by splitting on whitespace and removing punctuation.
    :param text: String to tokenize.
    :return: Array of tokens.
    """
    text = re.sub(r'(\w)-(\w)', r'\1 \2', text.lower())
    split = text.split()
    return [token.translate(str.maketrans('', '', string.punctuation.replace('-', '')))
            for token in split]


if __name__ == '__main__':
    print(f"Life is good: {ws_punc_tokenizer('Life is good')}")
    print(f"Search is my life: {ws_punc_tokenizer('Search is my life')}")