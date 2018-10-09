# uyghur_tools
Miscellaneous scripts for processing Uyghur data

* `uyghur_latin_to_cyrillic.py`: Converts text files containing latin Uyghur orthography to cyrillic orthography.

    usage: `python3 uyghur_latin_to_cyrillic.py <input_file> <output_file>`

* `uyghur_wugger.py`: Generates Uyghur wug words following a template file.

    usage: `python3 uyghur_wugger.py <template file> <outpfut file>`

    ## Template File Format
    Each line is a tab-separated pair: 
    
        <form template> <number>

    The form template field specifies the general segmental properties of the words. There are currently 9 segment types:

        C: Non-harmonizing consonants
        V: Non-harmonizing vowels
        F: Front vowels
        B: Back vowels
        K: Front dorsals
        Q: Back dorsals
        O: Legal word-initial non-harmonizing consonants
        I: /i/
        E: /é/

    These can be used in any combination. For example, CFQ would generate three-segment words that start with a non-harmonizing consonant, followed by a front vowel, followed by a back dorsal.

    The number field specifies how many tokens of each template are created.

    The actual segments that go into each segment type slot are chosen uniformly at random from that class of segments. See the source code for details. See `wug_templates.txt` for an example of the template file.

* `uyghur_regexes.txt`: Some example regexes for use in a Uyghur corpus searcher
