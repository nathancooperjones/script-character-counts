# `script_scraper` - Parser for Film and TV Scripts

[![codecov](https://codecov.io/gh/nathancooperjones/script-scraper/branch/master/graph/badge.svg?token=4YKUOBQM53)](https://codecov.io/gh/nathancooperjones/script-scraper)

A lightweight Python parser initially written for the [Geena Davis Institute's](https://seejane.org) Spell Check for Bias tool.

![The first page of the Inception script](https://nathancooperjones.com/wp-content/uploads/2020/05/2-1024x888.jpg)

### Usage
```python
>>> from script_scraper import open_pdf, script_scraper, word_and_sentence_count
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
Begin by installing [Docker](https://docs.docker.com/install/), if you have not already. Once Docker is running, run development from within the Docker container:

```bash
# build the Docker image
docker build -t script_scraper .

# run the Docker container in interactive mode
docker run \
    -it \
    --rm \
    -v "${PWD}:/script_scraper" \
    -p 8888:8888 \
    script_scraper /bin/bash

# launch JupyterLab...
jupyter lab --ip 0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''

# ... or, now in the container, run unit tests, if you'd like
pytest -v --cov-report term --cov=script_scraper
```

### Known Bugs / Issues Progress
- [ ] Dialogue that might span multiple lines with multiple characters separated with a `/` is incorrectly counted and reported as a single character.
  - Low priority, might not address in the foreseeable future.
- [X] Character names with slight misspellings are counted as separate characters.
  - Addressed in version `0.5.0`
- [X] Dialogue with multiple characters speaking at once (side-by-side type) with sub-groups of characters speaking at once separated with a `/` is incorrectly counted and reported as only two characters.
  - Addressed in version `0.4.0`
- [X] Character's with `V.O.` in name are counted as separate characters.
  - Addressed in version `0.3.0`
- [X] Dialogue with multiple characters separated with an `AND` or `&` is incorrectly counted and reported as a single character.
  - Addressed in version `0.3.0`
- [X] Characters with punctuation are sometimes counted as more than one character.
  - Addressed in version `0.3.0`
- [X] Sentence count is not the _most_ reliable yet for some character's dialogue.
  - Addressed in version `0.2.2`
- [X] Dialogue with multiple characters separated with a `/` is incorrectly counted and reported as a single character.
  - Addressed in version `0.2.0`
- [X] `non_dialogue_sentence` _might_ not be required for `get_character_dialogue_for_page`...
  - Addressed in version `0.1.1`
- [X] Sometimes, different scene descriptions are counted as characters.
  - Addressed in version `0.2.1`
- [X] When a character speaks in all caps, it is assumed to be a character name.
  - Addressed in version `0.1.1`
