from PasswordGeneration.Business.Strategies.HighSecurityPasswordGenerator import HighSecurityPasswordGenerator
from PasswordGeneration.Business.Strategies.LowSecurityPasswordGenerator import LowSecurityPasswordGenerator
from PasswordGeneration.Business.Strategies.MediumSecurityPasswordGenerator import MediumSecurityPasswordGenerator
from PasswordGeneration.Models.SecurityLevel import SecurityLevel
from PasswordGeneration.Models.PasswordGeneratorModel import PasswordGeneratorModel


class PasswordGeneratorService:
    def GeneratePassword(self, passwordGeneratorModel: PasswordGeneratorModel):
        length = passwordGeneratorModel.length
        complexity = passwordGeneratorModel.complexity
        securityLevel = passwordGeneratorModel.securityLevel
        if securityLevel == SecurityLevel.LOW:
            return LowSecurityPasswordGenerator().GeneratePassword(length, complexity)

        elif securityLevel == SecurityLevel.MEDIUM:
            return MediumSecurityPasswordGenerator().GeneratePassword(length, complexity)

        elif securityLevel == SecurityLevel.HIGH:
            return HighSecurityPasswordGenerator().GeneratePassword(length, complexity)

        else:
            raise ValueError("invalid security level")
