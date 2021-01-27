# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project uses [Semantic Versioning](http://semver.org/).

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
 - duplicated punctuation is not counted as separate lines

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
 - Codecov badge to `README`
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
 - Dockerfile setup

# [0.0.0] - 2020-5-15
### Added
 - Initial repo setup
