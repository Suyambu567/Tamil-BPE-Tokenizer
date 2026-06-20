class TamilUnicodeValidator:

    @staticmethod
    def is_tamil_char(char):

        return 0x0B80 <= ord(char) <= 0x0BFF

    @staticmethod
    def validate_text(text):

        result = []

        for char in text:

            if char == " ":
                continue

            result.append(
                (char,
                 TamilUnicodeValidator.is_tamil_char(char))
            )

        return result