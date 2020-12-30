import random, string


def generate_id(character_count=8):
    all_chars = string.digits + string.ascii_lowercase
    url_id = ''

    for i in range(character_count):
        url_id = url_id + random.sample(all_chars, 1)[0]
    
    return url_id