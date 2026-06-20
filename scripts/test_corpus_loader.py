from src.corpus_loader import CorpusLoader

loader = CorpusLoader()

text = loader.load("data/raw/corpus.txt")

print(text)