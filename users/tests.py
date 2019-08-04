from django.test import TestCase
from .models import Users


def test_createUser():

    newUser = Users(username="Bobette", email="bobette@reeher-palmer.net")

    assert newUser.username
    assert newUser.username == "Bobette"
    assert newUser.email
    assert newUser.email == "bobette@reeher-palmer.net"


def test_emptyusers():

    emptyUser = Users("", "")

    assert emptyUser.displayName != ""
    assert emptyUser.username != ""
    assert emptyUser.email != ""

