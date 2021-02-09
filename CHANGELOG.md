# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project uses [Semantic Versioning](http://semver.org/).

# [0.5.1] - 2021-2-8
### Fixed
 - checking character name for `' AND '` instead of `'AND'`

# [0.5.0] - 2021-1-31
### Added
 - `combine_similar_names` function to `utils.py` to account for potential typos in character names left in script
 - type hints to _all_ functions and helper functions
 - `python-Levenshtein` to requirements in `setup.py`
### Changed
 - `script_scraper` utilities moved from `utils.py` -> `script_scraper.py`
 - `tests/test_word_and_sentence_count.py` -> `tests/test_utils.py`

# [0.4.2] - 2021-1-27
### Added
 - `python@3.9` tests to GitHub workflows
### Fixed
 - added back support for `python@3.6`
### Removed
 - `pip-tools`, as requirements will not generalize to multiple versions of Python

# [0.4.1] - 2021-1-27
### Added
 - library dependency management with `pip-tools`
### Changed
 - updated `README.md` known issues and bugs section

# [0.4.0] - 2021-1-26
### Added
 - support for dialogue with multiple characters speaking at once (side-by-side type) with sub-groups of characters speaking at once separated with a `/` being incorrectly counted and reported as more than just two characters
 - `Jupyterlab` libraries for displaying progress bars
### Changed
 - test organization
 - `Dockerfile` now installs `requirements-dev.txt`
 - base image for `Dockerfile` has been upgraded to `python@3.9`
 - `script_scraper` now uses `tqdm.auto` for progress bars rather than just `tqdm`
### Fixed
 - `README` typos

# [0.3.0] - 2021-1-26
### Added
 - support for multiple characters speaking at once, denoted with the `/` character
 - support for multiple characters speaking at once, denoted with `AND`
### Changed
 - character name punctuation is removed entirely
### Fixed
 - no print output when `verbose=True`
 - `V.O.` is now correctly filtered out of character's names

# [0.2.2] - 2021-1-11
### Fixed
 - duplicated punctuation is not counted as separate lines in `word_and_sentence_count`

# [0.2.1] - 2020-12-4
### Added
 - `start_page_number` argument to `script_scraper`
### Fixed
 - number of spaces for a dialogue line now must be less than 35, compared to the previous 31
 - `tokenizers/punkt` only downloaded once
 - acts are not counted as characters

# [0.2.0] - 2020-12-4
### Added
 - support for two characters speaking at once
 - more rigorous testing
 - `Codecov` badge to `README`
### Changed
 - removed complexity of scanning each page twice to detect `all_dialogue`
 - reorganized utility functions into `utils.py`
 - renamed files and functions
### Fixed
 - reduced number of false characters caught, such as stage direction, descriptions, etc.

# [0.1.1] - 2020-5-18
### Added
 - `debug` parameter to `get_character_dialogue_for_script` function
 - Additional round of unit testing for some more fun edge-cases
### Changes
 - refactored `get_character_dialogue_for_script` to no longer require a line of non-dialogue
### Fixed
 - different scene descriptions are no longer counted as characters for most cases
 - when a character speaks in all caps, it is no longer assumed to be a character name

# [0.1.0] - 2020-5-17
### Added
 - Logic to record character word counts in `script_analysis.py`
 - Example notebook showing workflow in `nbs/script_analysis.ipynb`
 - Updated `README` instructions
 - First round of unit testing
### Changes
 - renamed repo from `script_character_counts` to `script_scraper`

# [0.0.1] - 2020-5-15
### Added
 - `Dockerfile` setup

# [0.0.0] - 2020-5-15
### Added
 - Initial repo setup
