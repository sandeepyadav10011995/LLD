

class IntegerValidator:
    @staticmethod
    def isInteger(input_value: str) -> bool:
        try:
            string_int = int(input_value)
            print(string_int)
            return True
        except ValueError:
            return False
