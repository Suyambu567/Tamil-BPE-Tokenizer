import json
from collections import defaultdict

class BPETokenizer:

    def __init__(self):
        self.merges = []

    def get_vocab(self, corpus):

        vocab = {}

        for word in corpus.split():

            chars = " ".join(list(word))

            vocab[chars] = vocab.get(chars, 0) + 1

        return vocab

    def get_stats(self, vocab):

        pairs = defaultdict(int)

        for word, freq in vocab.items():

            symbols = word.split()

            for i in range(len(symbols) - 1):

                pairs[(symbols[i], symbols[i + 1])] += freq

        return pairs

    def best_pair(self, pairs):

        return max(
            pairs,
            key=pairs.get
        )

    def merge_pair(self, pair, vocab):

        merged_vocab = {}

        bigram = " ".join(pair)

        replacement = "".join(pair)

        for word in vocab:

            new_word = word.replace(
                bigram,
                replacement
            )

            merged_vocab[new_word] = vocab[word]

        return merged_vocab

    def train(self, corpus, num_merges=50):

        vocab = self.get_vocab(corpus)

        for i in range(num_merges):

            pairs = self.get_stats(vocab)

            if not pairs:
                break

            best = self.best_pair(pairs)

            self.merges.append(best)

            print(f"Merge {i+1}: {best}")

            vocab = self.merge_pair(
                best,
                vocab
            )

        return vocab
    
    def encode(self, text):

        tokens = []

        for word in text.split():

            pieces = list(word)

            changed = True

            while changed:

                changed = False

                for merge in self.merges:

                    i = 0

                    while i < len(pieces) - 1:

                        if (
                            pieces[i] == merge[0]
                            and
                            pieces[i + 1] == merge[1]
                        ):

                            pieces[i:i+2] = [
                                merge[0] + merge[1]
                            ]

                            changed = True

                        else:
                            i += 1

            tokens.extend(pieces)

        return tokens
    def decode(self, tokens):

        return " ".join(tokens)
    def save_model(self, filepath):

        with open(filepath, "w", encoding="utf-8") as f:

            json.dump(
                self.merges,
                f,
                ensure_ascii=False,
                indent=4
            )
    def load_model(self, filepath):

        with open(filepath, "r", encoding="utf-8") as f:

            self.merges = [
                tuple(x)
                for x in json.load(f)
            ]