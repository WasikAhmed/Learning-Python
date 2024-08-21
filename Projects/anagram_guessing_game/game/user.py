import json
import hashlib


class User:
    def __init__(self, username, password, wins=0, losses=0):
        self.username = username
        self.password = self._hash_password(password)
        self.wins = wins
        self.losses = losses

    @staticmethod
    def _hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        return self.password == self._hash_password(password)

    def update_stat(self, won):
        if won:
            self.wins += 1
        else:
            self.losses += 1

    def save_user(self, filepath="data/users.json"):
        users = self._load_user(filepath)
        users[self.username] = {
            "password": self.password,
            "wins": self.wins,
            "losses": self.losses
        }
        with open(filepath, 'w') as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def _load_user(filepath):
        try:
            with open(filepath, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @classmethod
    def authenticate(cls, username, password, filepath="data/users.json"):
        users = cls._load_user(filepath)
        if username in users and users[username]['password'] == cls._hash_password(password):
            return cls(username, password, users[username]['wins'], users[username]['losses'])
        else:
            return None
