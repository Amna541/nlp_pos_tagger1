from nlp_pos_tagger.pos_tagger import pos_tag_text

text = "MY name is Amna Arooj. I work in Disrutive AI as an internee."
tags = pos_tag_text(text)
print(tags)
