class PasswordManager:
    def __init__(self) -> None:
        self.old_passwords = []

    def get_password(self):
        return self.old_passwords[-1]

    def set_password(self, new_password):

        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
        return

    def is_correct(self, attempt):
        return attempt == self.get_password()
