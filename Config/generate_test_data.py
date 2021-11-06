import random
from faker import Faker
fake = Faker("en")


def unique_random_word():
    return fake.word()


def first_name():
    return fake.first_name_male()


def last_name():
    return fake.last_name_male()


def name_prefix():
    prefixes = ["Mr", "Mrs", "Miss", "Ms", "Master", "Fr", "Rev", "Dr"]
    return random.choice(prefixes)
