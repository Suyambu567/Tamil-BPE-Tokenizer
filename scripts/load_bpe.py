from src.bpe_tokenizer import BPETokenizer

bpe = BPETokenizer()

bpe.load_model(
    "models/bpe_merges.json"
)

encoded = bpe.encode(
    "நான் பள்ளிக்கு"
)

print(encoded)