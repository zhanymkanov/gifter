import random
import string


def gen_sku() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=7))
