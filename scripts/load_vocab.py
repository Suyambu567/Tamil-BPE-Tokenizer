from src.vocabulary import Vocabulary

vocab = Vocabulary()

vocab.load("data/vocab/vocab.json")

print(vocab.word_to_id)

print(vocab.decode([0,1,2,3]))
from src.bpe_tokenizer import BPETokenizer

bpe = BPETokenizer()

bpe.load_model(
    "models/bpe_merges.json"
)

encoded = bpe.encode(
    "நான் பள்ளிக்கு"
)

print(encoded)