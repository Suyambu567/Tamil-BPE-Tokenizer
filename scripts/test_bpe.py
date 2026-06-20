from src.bpe_tokenizer import BPETokenizer

corpus = """
நான் இன்று
நான் பள்ளிக்கு
"""

bpe = BPETokenizer()

final_vocab = bpe.train(
    corpus,
    num_merges=50
)

print("\nFinal Vocabulary")

for word, freq in final_vocab.items():
    print(word, "->", freq)

print("\nLearned Merge Rules")

for merge in bpe.merges:
    print(merge)

print("\nEncoded Text")

encoded = bpe.encode(
    "நான் பள்ளிக்கு"
)

print(encoded)
bpe.save_model(
    "models/bpe_merges.json"
)

print("\nModel Saved")
bpe.save_model(
    "models/bpe_merges.json"
)

print("Model Saved")