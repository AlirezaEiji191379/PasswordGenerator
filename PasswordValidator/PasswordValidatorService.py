import string
from PasswordGeneration.Business.Utils.PasswordUtility import HasDuplicateCharacter, HasSequentialChars
from PasswordValidator.Models.PasswordStrengthEnum import PasswordStrengthEnum
import re


class PasswordValidatorService:
    def GetPasswordStrength(self, password: str) -> PasswordStrengthEnum:
        result_score = 0
        result_score = result_score + self.__GetLengthScore(password)
        result_score = result_score + self.__GetCharsetScore(password)
        result_score = result_score + self.__GetUnpredictabilityScore(password)
        print(result_score)
        if result_score >= 80:
            return PasswordStrengthEnum.STRONG
        elif result_score > 50:
            return PasswordStrengthEnum.MEDIUM
        else:
            return PasswordStrengthEnum.WEAK

    @staticmethod
    def __GetUnpredictabilityScore(password):
        predictabilityScore = 30
        if HasDuplicateCharacter(password):
            return 10
        if HasSequentialChars(password):
            return 20
        return predictabilityScore

    @staticmethod
    def __GetCharsetScore(password):
        variety_score = 0
        if re.search(r"[a-z]", password):
            variety_score += 1
        if re.search(r"[A-Z]", password):
            variety_score += 1
        if re.search(r"\d", password):
            variety_score += 1
        if any(char in string.punctuation for char in password):
            variety_score += 1
        return (variety_score / 4) * 30

    @staticmethod
    def __GetLengthScore(password):
        length_score = len(password) / 12
        return min(length_score, 1) * 40
