from spellchecker import SpellChecker
from PyDictionary import PyDictionary

spell = SpellChecker()
dictionary=PyDictionary()

misspelled = spell.unknown(['HEE'])
for word in misspelled:
	print(spell.correction(word))
	print(spell.candidates(word))
#print(dictionary.meaning("HELP"))
