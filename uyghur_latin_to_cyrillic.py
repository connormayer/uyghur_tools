import argparse

MAP_1 = {
    "A": "А",
    "a": "а",
    "E": "Ә",
    "e": "ә",
    "B": "Б",
    "b": "б",
    "P": "П",
    "p": "п",
    "T": "Т",
    "t": "т",
    "J": "Җ",
    "j": "җ",
    "X": "Х",
    "x": "х",
    "D": "Д",
    "d": "д",
    "R": "Р",
    "r": "р",
    "Z": "З",
    "z": "з",
    "S": "С",
    "s": "с",
    "F": "Ф",
    "f": "ф",
    "Q": "Қ",
    "q": "қ",
    "K": "К",
    "k": "к",
    "G": "Г",
    "g": "г",
    "L": "Л",
    "l": "л",
    "M": "М",
    "m": "м",
    "N": "Н",
    "n": "н",
    "H": "Һ",
    "h": "һ",
    "O": "О",
    "o": "о",
    "U": "У",
    "u": "у",
    "Ö": "Ө",
    "ö": "ө",
    "Ü": "Ү",
    "ü": "ү",
    "W": "В",
    "w": "в",
    "É": "Е",
    "é": "е",
    "I": "И",
    "i": "и",
    "Y": "Й",
    "y": "й"
}

MAP_2 = {
    "Ng": "Ң",
    "ng": "ң",
    "Sh": "Ш",
    "sh": "ш",
    "Gh": "Ғ",
    "gh": "ғ",
    "Zh": "Ж",
    "zh": "ж",
    "Ch": "Ч",
    "ch": "ч",
    "ya": "я",
    "Ya": "Я"
}

def convert_latin_to_cyrillic(infile, outfile):
    """
    Converts latin Uyghur script to cyrillic. Because several sounds are
    represented with two characters in latin orthography, there are potentially
    ambiguous sequences that are differentiated with apostrophes: e.g. "yengi" 
    with a velar nasal and "in'glizche" with an alveolar nasal followed by a
    velar stop. To conver these properly, we first convert all two char sounds
    (from MAP_2), then remove apostrophes, then convert all one char sounds
    (from MAP_1).
    """
    with open(infile, "r") as f:
        file = f.read()

    # Replace all two character sequences
    for key in MAP_2:
        file = file.replace(key, MAP_2[key])

    # Remove miscellaneous characters
    file = file.replace("'", "")
    file = file.replace("=", "")
    file = file.replace("’", "")

    # Replace all one character sequences
    for key in MAP_1:
        file = file.replace(key, MAP_1[key])

    with open(outfile, "w") as f:
        f.write(file)

def convert_cyrillic_to_latin(infile, outfile):
    """
    Converts cyrillic Uyghur script to Latin.
    """
    with open(infile, "r") as f:
        file = f.read()

    map_1 = {v: k for k, v in MAP_1.items()}
    map_2 = {v: k for k, v in MAP_2.items()}

    for key in map_2:
        file = file.replace(key, map_2[key])

    # Remove miscellaneous characters
    file = file.replace("'", "")
    file = file.replace("=", "")
    file = file.replace("’", "")

    # Replace all one character sequences
    for key in map_1:
        file = file.replace(key, map_1[key])

    with open(outfile, "w") as f:
        f.write(file)

    parser = argparse.ArgumentParser(
        description="Convert latin Uyghur script to cyrillic"
    )
    parser.add_argument(
        "infile", type=str, help="The file to read latin script from"
    )
    parser.add_argument(
        "outfile", type=str, help="The file to write cyrillic script to"
    )
    args = parser.parse_args()
    if args.input == "cyrillic":
        convert_cyrillic_to_latin(args.infile, args.outfile)
    elif args.input == "latin":
        convert_latin_to_cyrillic(args.infile, args.outfile)
    else:
        print("Invalid input value {}".format(args.input))
