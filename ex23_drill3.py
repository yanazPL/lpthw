import sys
script, encoding, error = sys.argv


def main(file, encoding, errors):
    piece = file.read()

    if piece:
        print_character(piece, encoding, errors)
        return main(file, encoding, errors)


def print_character(piece, encoding, errors):
    print (piece.decode(encoding, errors))

languages = open("languages.txt", "rb")

main(languages, encoding, error)