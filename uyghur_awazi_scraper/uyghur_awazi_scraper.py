import argparse
import csv
import random
import requests 
import time

from bs4 import BeautifulSoup 

HEADERS = [
    "category", "author", "url", "text", "title", "author_latin", "keywords",
    "text_latin", "title_latin", "date"
]

URL_TEMPLATE = "http://uyguravazi.kazgazeta.kz/?p={}"

DEFAULT_START = 1
# Newest article as of 13/01/2020
DEFAULT_END = 41966

DEFAULT_OUTFILE = "kazgazeta_corpus_scrape.csv"

# Amount of time to wait between requests, in seconds
DEFAULT_WAIT_TIME = 2

MAP_1 = {
    "Ä": "E",
    "ä": "e",
    "V": "W",
    "v": "w",
    "Ç": "Ch",
    "ç": "ch",
    "Ş": "Sh",
    "ş": "sh",
    "Š": "Ö",
    "š": "ö",
    "Җ": "J",
    "җ": "j",
    "ŋ": "ng",
    "Ğ": "Gh",
    "ğ": "gh",
    "I": "I",
    "ı": "i",
    "İ": "I",
    "°": "'"
}

MAP_2 = {
    "E": "É",
    "e": "é",
    "J": "Zh",
    "j": "zh"
}

def convert_turkish_to_latin_str(in_str):
    if not in_str:
        return ""

    for key in MAP_2:
        in_str = in_str.replace(key, MAP_2[key])

    # Remove miscellaneous characters
    in_str = in_str.replace("'", "")
    in_str = in_str.replace("=", "")
    in_str = in_str.replace("’", "")

    # Replace all one character sequences
    for key in MAP_1:
        in_str = in_str.replace(key, MAP_1[key])

    return in_str

def scrape_corpus(outfile, start, end, truncate_outfile, wait_time):
    if truncate_outfile:
        print("Truncating outfile...")
        with open(outfile, 'w', encoding="utf-8") as f:
            f.write(','.join(HEADERS) + "\n")

    with open(outfile, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        if truncate_outfile:
            writer.writerow(HEADERS)

        for i in range(start, end + 1):
            article_url = URL_TEMPLATE.format(str(i))
            print("Processing {}...".format(article_url))

            page = requests.get(article_url)

            if page.status_code == 200:
                soup = BeautifulSoup(page.text, "html.parser")
                soup.prettify().encode('ascii', 'replace')

                main_content = soup.find('div', attrs={'class': 'td-ss-main-content'})
                post_title = soup.find('h1', attrs={'class': 'entry-title'})
                post_content = soup.find('div', attrs={'class': 'td-post-content'})
                post_date = soup.find('span', attrs={'class': 'td-post-date'})
                post_author = soup.find('div', attrs={'class': 'td-post-author-name'})

                date = post_date.text.strip() if post_date else ""
                author = post_author.text.strip() if post_author else ""
                text = post_content.text.strip() if post_content else ""
                title = post_title.text.strip() if post_title else ""

                author_latin = convert_turkish_to_latin_str(author)
                text_latin = convert_turkish_to_latin_str(text)
                title_latin = convert_turkish_to_latin_str(title)

                with open(outfile, 'a', encoding="utf-8") as f:
                    writer.writerow([
                        "", 
                        author, 
                        article_url, 
                        text, 
                        title, 
                        author_latin,
                        "",
                        text_latin,
                        title_latin,
                        date
                    ])
            else:
                print("Error: Response code {} for url {}".format(page.status_code, article_url))

            time.sleep(wait_time + random.random())

if __name__ == "__main__":
    """
    Scrape article titles and text from http://uyguravazi.kazgazeta.kz/.
    """
    parser = argparse.ArgumentParser(
        description="Scrape article titles and text from http://uyguravazi.kazgazeta.kz/."
    )
    parser.add_argument(
        'outfile', type=str, help='The file to save results to.'
    )
    parser.add_argument(
        '--start', type=int, default=DEFAULT_START,
	help="The starting index of the articles to scrape."
    )
    parser.add_argument(
        '--end', type=int, default=DEFAULT_END,
	help="The ending index of the articles to scrape."
    )
    parser.add_argument(
        '--truncate_outfile', action="store_true", default=False,
        help="If this flag is specified, the outfile will be truncated before "
             "the script runs."
    )
    parser.add_argument(
        '--wait_time', type=int, default=DEFAULT_WAIT_TIME,
        help="The amount of time to wait between requests."
    )

    args = parser.parse_args()
    results = scrape_corpus(
        args.outfile, args.start, args.end, args.truncate_outfile, args.wait_time
    )
