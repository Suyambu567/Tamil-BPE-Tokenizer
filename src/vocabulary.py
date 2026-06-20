import json

class Vocabulary:

    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}

    def build_vocab(self, tokens):

        for word in tokens:

            if word not in self.word_to_id:

                idx = len(self.word_to_id)

                self.word_to_id[word] = idx
                self.id_to_word[idx] = word

    def encode(self, tokens):

        return [
            self.word_to_id[word]
            for word in tokens
        ]

    def decode(self, ids):

        return [
            self.id_to_word[idx]
            for idx in ids
        ]

    def save(self, filepath):

        with open(filepath, "w", encoding="utf-8") as f:

            json.dump(
                self.word_to_id,
                f,
                ensure_ascii=False,
                indent=4
            )

    def load(self, filepath):

        with open(filepath, "r", encoding="utf-8") as f:

            self.word_to_id = json.load(f)

        self.id_to_word = {
            int(v): k
            for k, v in self.word_to_id.items()
        }