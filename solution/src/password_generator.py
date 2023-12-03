import random
import string
import nltk
from abc import ABC, abstractmethod
from typing import List, Optional

nltk.download('words')

class PasswordGenerator(ABC):
    """Base class for generating passwords."""
    
    @abstractmethod
    def generate(self) -> str:
        """Subclasses should override this method to generate password."""
        pass


class PinCodeGenerator(PasswordGenerator):
    """Class to generate a numeric pin code"""

    def __init__(self, length: int = 4) -> str:
        self.length: int = length

    def generate(self) -> str:
        """Generate a numeric pin code."""
        #string.digits -> '0123456789'
        return ''.join([random.choice(string.digits) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """Class to generate random password"""
    def __init__(self, length: int=8, include_numbers: bool = False, include_symbols: bool = False) -> str:
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters +=string.punctuation

    def generate(self) -> str:
        """Generate a password from specified characters."""
        return ''.join([random.choice(self.characters) for _ in range(self.length)])


class MemorablePasswordGenerator(PasswordGenerator):
    """Class to generate a memorable password"""
    def __init__(
        self,
        num_of_word: int = 5,
        seperator: str = '-',
        capitalization: bool = False,
        vocabulary: Optional[List[str]] = None) -> str:

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        
        self.num_of_words: int = num_of_word
        self.seperator: str = seperator
        self.capitalization: bool = capitalization
        self.vocabulary: List[str] = vocabulary
   
    def generate(self) -> str:
        """Generate a password from a list of vocabulary words."""

        password_words = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalization:
            password_words = [word.upper() for word in password_words]
        
        return self.seperator.join(password_words)
       