from src.tokenizers import TamilTokenizer
from src.vocabulary import Vocabulary

text = "நான் இன்று பள்ளிக்கு சென்றேன்"

tokenizer = TamilTokenizer()

tokens = tokenizer.tokenize(text)

vocab = Vocabulary()

vocab.build_vocab(tokens)

vocab.save("data/vocab/vocab.json")

print("Vocabulary Saved")