from src.char_tokenizer import CharacterTokenizer

tokenizer = CharacterTokenizer()

text = "நான்"

tokens = tokenizer.tokenize(text)

print(tokens)