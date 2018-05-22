import argparse
import csv

def process_scraper_output(infile, outfile):
    words = set()
    with open(infile, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            words.add(row['text_latin'])

    words_list = sorted(words, key=len)
    with open(outfile, 'w') as f:
        for word in words_list:
            f.write(word + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Takes the output of the Uyghur scraper and "
                    "returns unique words sorted ascending by length",
    )
    parser.add_argument(
        "infile", type=str, help="The file to read scraper output from"
    )
    parser.add_argument(
        "outfile", type=str, help="The file to write sorted words to"
    )
    args = parser.parse_args()
    process_scraper_output(args.infile, args.outfile)
