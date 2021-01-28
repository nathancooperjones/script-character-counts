FROM python:3.9

RUN apt-get update && apt-get install -y \
  tmux \
  vim \
  libpq-dev \
  gcc \
  locales \
  build-essential \
  libpoppler-cpp-dev \
  pkg-config \
  python-dev

# Enables us to use tmux. the language encoding in this container is not quite right.
RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "LANG=en_US.UTF-8" > /etc/locale.conf
RUN locale-gen en_US.UTF-8

USER root
WORKDIR /script_scraper/

# copy requirement files over
COPY setup.py README.md requirements-dev.txt ./
COPY script_scraper/_version.py ./script_scraper/

# install libraries
RUN pip install -U pip
RUN pip install -r requirements-dev.txt
RUN pip install -e .

# copy the rest of the files to the container
COPY . .
