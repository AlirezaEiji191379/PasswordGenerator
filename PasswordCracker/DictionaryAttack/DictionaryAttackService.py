import hashlib
import time


class DictionaryAttackService:
    def __init__(self, passwordsFilePath):
        self.passFilePath = passwordsFilePath

    def Attack(self, inputPasswordHash):
        passwords_list = []
        with open(self.passFilePath, 'r') as file:
            for line in file:
                passwords_list.append(line.strip())
        start_time = time.time()
        for password in passwords_list:
            hashedPassword = hashlib.sha256(password.encode()).hexdigest()
            if hashedPassword == inputPasswordHash:
                print("password is " + str(password))
                elapsed_time = time.time() - start_time
                print(f"Method runtime: {elapsed_time:.6f} seconds")
                return password
        print("password not found")
        elapsed_time = time.time() - start_time
        print(f"Method runtime: {elapsed_time:.6f} seconds")
        return None
