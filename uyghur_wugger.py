import argparse
import random

SOUND_DICT = {
    # Non-harmonizing consonants
    'C': [
        'b', 'p', 't', 'j', 'x', 'd', 'r', 'z', 's', 'f', 'l', 'm', 'n', 'h',
        'w', 'y', 'ng', 'sh', 'zh', 'ch'
    ],

    # Non-harmonizing consonants in onset position
    'O': [
        'b', 'p', 't', 'j', 'x', 'd', 'r', 'z', 's', 'f', 'l', 'm', 'n', 'h',
        'w', 'y', 'ng', 'sh', 'zh', 'ch'
    ]

    # Non-harmonizing vowels
    'V': [
        'i', 'é'   
    ],

    # /i/
    'I': [
        'i'
    ]

    # /é/
    'E': [
        'é'  
    ]

    # Front vowels
    'F': [
        'e', 'ö', 'ü'
    ],

    # Back vowels
    'B': [
        'a', 'o', 'u'
    ],

    # Front dorsals   
    'K': [
        'k', 'g', 
    ],

    # Back dorsals
    'Q': [
        'q', 'gh'
    ]
}

def create_wugs(template, number):
    wugs = []
    for _ in range(int(number)):
        wug = ''
        for c in template:
            wug += random.choice(SOUND_DICT[c])
        wugs.append(wug)
    return wugs

def generate_wugs(input_file, output_file):
    wugs = []
    with open(input_file, 'r') as f:
        for line in f:
            if line and not line[0] == '#':
                template, number = line.rstrip().split('\t')
                wugs.extend(create_wugs(template, number))

    with open(output_file, 'w') as f:
        for wug in wugs:
            f.write(wug + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate Uyghur wug words from a template file"
    )
    parser.add_argument(
        "infile", type=str, help="The file to read the templates from"
    )
    parser.add_argument(
        "outfile", type=str, help="The file to write wugs to"
    )
    args = parser.parse_args()
    generate_wugs(args.infile, args.outfile)
