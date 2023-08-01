# NLP POS Tagger

[![PyPI Version](https://img.shields.io/pypi/v/nlp_pos_tagger)](https://pypi.org/project/nlp_pos_tagger/)
[![License](https://img.shields.io/pypi/l/nlp_pos_tagger)](https://github.com/Amna541/nlp_pos_tagger/blob/main/LICENSE)

A simple NLP library for Part-of-Speech (POS) tagging in English text.

## Installation

You can install the library using `pip`:

```bash
pip install nlp_pos_tagger
```

## Usage

```python
from nlp_pos_tagger import pos_tag_text

text = "you can write any text here✏️🖋️."
tags = pos_tag_text(text)
print(tags)
```

## Features

- Perform Part-of-Speech (POS) tagging on English text🙌.
- Tokenization using the Natural Language Toolkit (NLTK).
- Basic preprocessing to remove non-alphabetic characters and convert to lowercase.

## Requirements

- Python 3.x
- NLTK

## License

This project is licensed under the [MIT License](https://github.com/Amna541/nlp_pos_tagger/blob/main/LICENSE).

## Contribution

Contributions are welcome! If you find any issues or want to add new features, feel free to open a pull request👍👍.

## Acknowledgments

This library was developed as a part of the NLP course project by [Amna Arooj](https://github.com/Amna541).
