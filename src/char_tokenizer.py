class CharacterTokenizer:

    def tokenize(self, text):

        chars = []

        for char in text:

            if char != " ":
                chars.append(char)

        return chars