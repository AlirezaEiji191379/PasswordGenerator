import argparse
from PasswordGeneration.Business.PasswordGeneratorService import PasswordGeneratorService
from PasswordGeneration.Models.Complexity import Complexity
from PasswordGeneration.Models.SecurityLevel import SecurityLevel
from PasswordGeneration.Models.PasswordGeneratorModel import PasswordGeneratorModel


def GeneratePassword(length, secLevel, complexityStr):
    securityLevel = GetSecLevel(secLevel)
    complexity = GetComplexity(complexityStr)
    passwordModel = PasswordGeneratorModel(length, securityLevel, complexity)
    return PasswordGeneratorService().GeneratePassword(passwordModel)


def GetComplexity(complexityStr: str) -> Complexity:
    if complexityStr == "low":
        return Complexity.LOW

    elif complexityStr == "medium":
        return Complexity.MEDIUM

    elif complexityStr == "high":
        return Complexity.HIGH

    else:
        raise ValueError("invalid security level")


def GetSecLevel(secLevel: str) -> SecurityLevel:
    if secLevel == "low":
        return SecurityLevel.LOW

    elif secLevel == "medium":
        return SecurityLevel.MEDIUM

    elif secLevel == "high":
        return SecurityLevel.HIGH

    else:
        raise ValueError("invalid security level")


parser = argparse.ArgumentParser(description="Generate a secure password.")
parser.add_argument('--length', type=int, default=12, help="Length of the password.")
parser.add_argument('--secLevel', choices=['low', 'medium', 'high'], default='medium',
                    help="Security level of the password.")
parser.add_argument('--complexity', choices=['low', 'medium', 'high'], default='medium',
                    help="Complexity level of the password.")
args = parser.parse_args()
password = GeneratePassword(args.length, args.secLevel, args.complexity)
print(password)
