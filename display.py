import spacy
from spacy import displacy

f = open('dhruv_news.txt', 'r')
content = f.readlines()
example_document = ''

count = 0
for line in content:
    count += 1
    if count > 100:
        break
    else:
      example_document+=line
count = 1



nlp = spacy.load("en_core_web_sm")
doc = nlp(example_document)
displacy.render(doc, style='ent', jupyter=False)
html =  displacy.render(doc, style='ent', page=True)
print("HTML markup: ", html)
with open("./2.html", 'w+', encoding="utf-8") as fp:
    fp.write(html)
    fp.close()
