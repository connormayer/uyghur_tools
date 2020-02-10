# uyghur_awazi_scraper

A simple script to scrape articles from the Uyghur Awazi news website (http://uyguravazi.kazgazeta.kz/). 

This script pulls down article titles, authors (to the extent they're available), date, and article text. These fields are stored in both the default Latin orthography for Uyghur Awazi (a sort of "pan-Turkic" orthography with a smattering of Cyrillic characters) and the more standard Uyghur Latin orthography. Note that there are a few oddities with the pan-Turkic script: in particular, "ö" renders as "š".

This folder also contains the output of a full scrape of the site run in late January, 2020. 

If you run the scraper yourself, *please* be kind in your choice of the scraping rate (specified by the `--wait_time` argument). The default is 2 seconds (+/- some random perturbation). This is on the conservative side, but if you scrape too quickly you may cause technical issues for the site, get yourself blocked, or both.

You can run `python3 uyghur_awazi_scraper.py --help` for more information about the arguments to the script.