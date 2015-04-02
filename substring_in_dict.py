import enchant

d = enchant.Dict("en_US")
print(d.check("Hello"))
print(d.check("helo"))
print(d.suggest("Helo"))

#------------------------------------------------------------
from nltk.corpus import wordnet

