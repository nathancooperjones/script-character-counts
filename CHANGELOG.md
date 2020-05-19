# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) and this project uses [Semantic Versioning](http://semver.org/).

# [0.1.1] - 2020-5-18
### Added
 - `debug` parameter to `get_character_dialogue_for_script` function
 - Additional round of unit testing for some more fun edge-cases
### Changes
 - refactored `get_character_dialogue_for_script` to no longer require a line of non-dialogue
### Fixes
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
