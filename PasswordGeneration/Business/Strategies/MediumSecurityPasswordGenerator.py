from PasswordGeneration.Business.Strategies.BaseSecurityPasswordGenerator import BaseSecurityPasswordGenerator
from PasswordGeneration.Business.Utils.PasswordUtility import HasDuplicateCharacter
from PasswordGeneration.Business.Utils.PasswordUtility import GetPasswordCharacters
from PasswordGeneration.Models.Complexity import Complexity
import secrets


class MediumSecurityPasswordGenerator(BaseSecurityPasswordGenerator):
    def GeneratePassword(self, length: int, complexity: Complexity) -> str:
        if length < 10:
            raise ValueError("medium secure passwords length must be greater than 10")
        passwordCharset = GetPasswordCharacters(complexity)
        while True:
            password = ''.join(secrets.choice(passwordCharset) for _ in range(length))
            if not HasDuplicateCharacter(password):
                return password
