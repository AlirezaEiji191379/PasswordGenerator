from PasswordGeneration.Business.Strategies.BaseSecurityPasswordGenerator import BaseSecurityPasswordGenerator
from PasswordGeneration.Business.Utils.PasswordUtility import GetPasswordCharacters
from PasswordGeneration.Models.Complexity import Complexity
import secrets


class LowSecurityPasswordGenerator(BaseSecurityPasswordGenerator):
    def GeneratePassword(self, length: int, complexity: Complexity) -> str:
        if length < 6:
            raise ValueError("low secure passwords length must be greater than 6")
        passwordCharset = GetPasswordCharacters(complexity)
        return ''.join(secrets.choice(passwordCharset) for _ in range(length))
