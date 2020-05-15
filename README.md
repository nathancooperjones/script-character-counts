# Character Counts for Scripts

Software written for the Geena Davis Institute's Spell Check for Bias tool.

### Development
Begin by installing [Docker](https://docs.docker.com/install/) if you have not already. Once Docker is running, run development from within the Docker container:

```bash
# build the Docker image
docker build -t script_character_counts .

# run the Docker container in interactive mode.
docker run \
    -it \
    --rm \
    -v "${PWD}:/script_character_counts" \
    -p 8888:8888 \
    script_character_counts /bin/bash -c "pip install -r requirements-dev.txt && bash"
```
