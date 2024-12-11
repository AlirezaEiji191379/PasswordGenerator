from PasswordGeneration.Models.Complexity import Complexity
from PasswordGeneration.Models.SecurityLevel import SecurityLevel


class PasswordGeneratorModel:
    def __init__(self, length, securityLevel, complexity):
        self.length = length
        self.securityLevel = SecurityLevel(securityLevel)
        self.complexity = Complexity(complexity)
