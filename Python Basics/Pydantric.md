## Introduction
Pydantic is a library in Python used for data validation and settings management. It is used for defining data schemas and validating input data against those schemas. 
The library provides a way to define data schemas as Python classes, which can then be used to validate and parse data
Here are some use cases of Pydantic in Python:

  #### Data validation: 
  Pydantic is used for validating input data against a schema. It ensures that the data received by an application is valid and meets the defined criteria. For instance, 
  if you want to validate the incoming data to make sure it contains a certain field, Pydantic will help you do that.

  #### Data serialization and deserialization: 
  Pydantic can be used to serialize and deserialize data between different data formats like JSON, YAML, etc. It can also be used to map data to and from objects, and to 
  convert data types.

  #### Settings management: 
  Pydantic can be used for managing settings and configuration files. It can parse and validate configuration files, and provide a way to access and modify the settings in 
  those files.

  #### API input validation: 
  Pydantic is also used for validating input data for APIs. It ensures that the input data received by the API is valid and meets the defined criteria. This is especially 
  useful in web applications, where input validation is critical to prevent security vulnerabilities.


```
"""
Basic example showing how to read and validate data from a file using Pydantic.
"""

import json
from typing import List, Optional

import pydantic


class ISBNMissingError(Exception):
    """Custom error that is raised when both ISBN10 and ISBN13 are missing."""

    def __init__(self, title: str, message: str) -> None:
        self.title = title
        self.message = message
        super().__init__(message)


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 doesn't have the right format."""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Author(pydantic.BaseModel):
    name: str
    verified: bool


class Book(pydantic.BaseModel):
    """Represents a book with that you can read from a JSON file."""

    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    author2: Optional[Author]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_isbn_10_or_13(cls, values):
        """Make sure there is either an isbn_10 or isbn_13 value defined"""
        if "isbn_10" not in values and "isbn_13" not in values:
            raise ISBNMissingError(
                title=values["title"],
                message="Document should have either an ISBN10 or ISBN13",
            )
        return values

    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_valid(cls, value) -> None:
        """Validator to check whether ISBN10 is valid"""
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)

        if sum((10 - i) * char_to_int(x) for i, x in enumerate(chars)) % 11 != 0:
            raise ISBN10FormatError(
                value=value, message="ISBN10 digit sum should be divisible by 11."
            )
        return value

    class Config:
        """Pydantic config class"""

        allow_mutation = False
        anystr_lower = True


def main() -> None:
    """Main function."""

    # Read data from a JSON file
    with open("./data.json") as file:
        data = json.load(file)
        books: List[Book] = [Book(**item) for item in data]
        # print(books)
        print(books[0])
        # print(books[0].dict(exclude={"price"}))
        # print(books[1].copy())


if __name__ == "__main__":
    main()
```
