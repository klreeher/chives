from django.db import models


class Users:
    def __init__(self, username, email):

        self.username = username
        self.email = email
        self.displayName = username
