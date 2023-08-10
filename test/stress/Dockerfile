# Start with an Ubuntu base image
FROM ubuntu:20.04

# Set environment variables for non-interactive installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    autoconf \
    bc \
    build-essential \
    g++-8 \
    gcc-8 \
    clang-8 \
    lld-8 \
    gettext-base \
    gfortran-8 \
    iputils-ping \
    libbz2-dev \
    libc++-dev \
    libcgal-dev \
    libffi-dev \
    libfreetype6-dev \
    libhdf5-dev \
    libjpeg-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libpng-dev \
    libreadline-dev \
    libssl-dev \
    libsqlite3-dev \
    libxml2-dev \
    libxslt-dev \
    locales \
    moreutils \
    openssl \
    python-openssl \
    rsync \
    scons \
    python3-pip \
    libopenblas-dev \
    curl \
    wget \
    stress

# Install Python packages
RUN pip3 install --upgrade pip && \
    pip3 install tensorflow && \
    pip3 install torch

# Copy the provided Python script into the Docker image
COPY test.py /test.py

# Set command to run the script on container startup
CMD ["python3", "/test.py"]
