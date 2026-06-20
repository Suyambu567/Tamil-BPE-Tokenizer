from src.tokenizers import TamilTokenizer
from src.frequency_counter import FrequencyCounter

text = """
நான் இன்று பள்ளிக்கு சென்றேன்
நான் வீட்டிற்கு வந்தேன்
"""

tokenizer = TamilTokenizer()

tokens = tokenizer.tokenize(text)

counter = FrequencyCounter()

freq = counter.count_words(tokens)

print(freq)