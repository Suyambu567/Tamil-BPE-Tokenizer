class TamilTokenizer:

    def tokenize(self, text):
        return text.split()

if __name__ == "__main__":
    tokenizer = TamilTokenizer()

    text = "நான் இன்று பள்ளிக்கு சென்றேன்"

    print(tokenizer.tokenize(text))