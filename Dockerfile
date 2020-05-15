FROM python:3.7

RUN apt-get update && apt-get install -y \
  tmux \
  vim \
  libpq-dev \
  gcc \
  locales

# Enables us to use tmux. the language encoding in this container is not quite right.
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8

USER root
WORKDIR /script_character_counts/

# copy requirement files over
COPY setup.py README.md requirements.txt .
COPY script_character_counts/_version.py ./script_character_counts/

# install libraries
RUN pip install -U pip
RUN pip install -r requirements.txt

# copy the rest of the files to the container
COPY . .
