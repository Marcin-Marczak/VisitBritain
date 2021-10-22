from faker import Faker
fake = Faker("en")


def unique_random_word():
    return fake.word()
