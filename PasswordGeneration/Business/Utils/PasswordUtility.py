from PasswordGeneration.Models.Complexity import Complexity
import string


def GetPasswordCharacters(complexity: Complexity):
    if complexity == Complexity.LOW:
        return string.ascii_lowercase + string.digits

    elif complexity == Complexity.MEDIUM:
        return string.ascii_letters + string.digits

    elif complexity == complexity.HIGH:
        return string.ascii_letters + string.digits + string.punctuation

    else:
        raise ValueError("invalid complexity level!")


def HasDuplicateCharacter(generatedPassword):
    return len(generatedPassword) != len(set(generatedPassword))


def HasSequentialChars(password):
    for i in range(len(password) - 2):
        if ord(password[i + 1]) == ord(password[i]) + 1 and ord(password[i + 2]) == ord(password[i]) + 2:
            return True
    return False
