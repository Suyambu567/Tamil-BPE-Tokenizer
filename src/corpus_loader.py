class CorpusLoader:

    def load(self, filepath):

        with open(filepath, "r", encoding="utf-8") as f:

            text = f.read()

        return text