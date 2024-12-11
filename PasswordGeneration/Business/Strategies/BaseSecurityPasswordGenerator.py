from PasswordGeneration.Models.Complexity import Complexity


class BaseSecurityPasswordGenerator:
    def __init__(self):
        pass

    def GeneratePassword(self, length: int, complexity: Complexity) -> str:
        pass
