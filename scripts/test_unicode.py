from src.unicode_handler import TamilUnicodeValidator

text = "நான் இன்று பள்ளிக்கு சென்றேன்"

result = TamilUnicodeValidator.validate_text(text)

for char, status in result:
    print(char, status)