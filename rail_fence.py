def encrypt_rail_fence(plain_text, rails):
    fence = [['\n'] * len(plain_text) for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(plain_text)):
        fence[rail][i] = plain_text[i]
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    cipher_text = [char for rail in fence for char in rail if char != '\n']
    return cipher_text


def decrypt_rail_fence(cipher_text, rails):
    fence = [['\n'] * len(cipher_text) for _ in range(rails)]
    rail = 0
    direction = 1

    for i in range(len(cipher_text)):
        fence[rail][i] = '*'
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    index = 0
    for rail in fence:
        for i in range(len(rail)):
            if rail[i] == '*' and index < len(cipher_text):
                rail[i] = cipher_text[index]
                index += 1

    plain_text = []
    rail = 0
    direction = 1

    for _ in range(len(cipher_text)):
        plain_text.append(fence[rail][_])
        rail += direction

        if rail == rails - 1 or rail == 0:
            direction *= -1

    return plain_text

