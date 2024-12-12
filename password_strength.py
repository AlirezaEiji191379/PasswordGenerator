import argparse
from PasswordValidator.Models.PasswordStrengthEnum import *
from PasswordValidator.PasswordValidatorService import *

parser = argparse.ArgumentParser(description="validate password strength")
parser.add_argument('--password', help="password")
args = parser.parse_args()
password_strength = PasswordValidatorService().GetPasswordStrength(args.password)
if password_strength == PasswordStrengthEnum.STRONG:
    print("Strong password")
elif password_strength == PasswordStrengthEnum.WEAK:
    print("Weak password")
elif password_strength == PasswordStrengthEnum.MEDIUM:
    print("Medium password")
