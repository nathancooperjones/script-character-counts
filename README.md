# Character Counts for Scripts

A lightweight Python parser written for the [Geena Davis Institute's](https://seejane.org) Spell Check for Bias tool.

[![codecov](https://codecov.io/gh/nathancooperjones/script-scraper/branch/master/graph/badge.svg?token=4YKUOBQM53)](https://codecov.io/gh/nathancooperjones/script-scraper)

![The first page of the Inception script](https://nathancooperjones.com/wp-content/uploads/2020/05/2-1024x888.jpg)

### Usage
```python
>>> from script_scraper import (open_pdf,
...                             script_scraper,
...                             word_and_sentence_count)
>>> # open the PDF file
>>> pdf = open_pdf(path='~/Desktop/Inception.pdf')
>>> # run the analysis
>>> words_spoken = script_scraper(pdf=pdf,
...                               remove_first_line=False)
>>> # check words spoken for each character
>>> words_spoken['ATTENDANT']
['He was delirious. But he asked for', 'you by name. And...', 'Show him.']
>>> # get word and sentence count for each character
>>> word_count, sentence_count = word_and_sentence_count(words_spoken['ATTENDANT'])
>>> word_count, sentence_count
(13, 3)
```

### Development
Begin by installing [Docker](https://docs.docker.com/install/) if you have not already. Once Docker is running, run development from within the Docker container:

```bash
# build the Docker image
docker build -t script_scraper .

# run the Docker container in interactive mode.
docker run \
    -it \
    --rm \
    -v "${PWD}:/script_scraper" \
    -p 8888:8888 \
    script_scraper /bin/bash -c "pip install -r requirements-dev.txt && bash"

# now in the container, run unit tests, if you'd like
pytest -v --cov-report term --cov=script_scraper
```

### Known Bugs / Issues
- [ ] Sentence count is not the _most_ reliable yet for some character's dialogue.
- [X] `non_dialogue_sentence` _might_ not be required for `get_character_dialogue_for_page`...
- [X] Sometimes, different scene descriptions are counted as characters.
- [X] When a character speaks in all caps, it is assumed to be a character name.
- [X] When dialogue is split so two characters talk at once, that is counted as a single character.
