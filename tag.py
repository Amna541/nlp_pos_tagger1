from nlp_pos_tagger.pos_tagger import pos_tag_text

text = "Write any text here.🙂"
tags = pos_tag_text(text)

for word, tag, full_tag in tags:
    print(f"Word: {word}, POS Tag: {tag}, Full POS: {full_tag}")
