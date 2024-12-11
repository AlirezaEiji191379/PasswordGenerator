import secrets
from PasswordGeneration.Business.Strategies.BaseSecurityPasswordGenerator import BaseSecurityPasswordGenerator
from PasswordGeneration.Business.Utils.PasswordUtility import *
from PasswordGeneration.Models.Complexity import Complexity


class HighSecurityPasswordGenerator(BaseSecurityPasswordGenerator):
    def GeneratePassword(self, length: int, complexity: Complexity) -> str:
        if length < 16:
            raise ValueError("high secure passwords length must be greater than 16")
        passwordCharset = GetPasswordCharacters(complexity)
        first_char = secrets.choice(string.ascii_letters)
        while True:
            password = first_char + ''.join(secrets.choice(passwordCharset) for _ in range(length))
            if not HasDuplicateCharacter(password) and not HasSequentialChars(password):
                return password
