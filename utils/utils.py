def token_reader():
    token_file = open('../token.txt', 'r')
    lines = token_file.readlines()

    return lines[0]