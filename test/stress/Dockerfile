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
    wget

ENV REPO_URL https://developer.download.nvidia.cn/compute/redist/jp/

RUN \
    JETPACK_VERSION=$(curl -s $REPO_URL | grep -oP 'v\K[0-9]+(?=/)' | sed 's/./&\./g' | rev | cut -c2- | rev | sort -V | sed 's/\.//g' | tail -n 1) && \
    TENSORFLOW_REPO_URL=${REPO_URL}v${JETPACK_VERSION}/tensorflow/ && \
    TENSORFLOW_INSTALL=$TENSORFLOW_REPO_URL$(curl -s $TENSORFLOW_REPO_URL | grep -oP 'tensorflow-.*?\.whl' | sort -V | tail -n 1) && \
    TORCH_REPO_URL=${REPO_URL}v${JETPACK_VERSION}/pytorch/ && \
    TORCH_INSTALL=$TORCH_REPO_URL$(curl -s $TORCH_REPO_URL | grep -oP 'torch-.*?\.whl' | sort -V | tail -n 1) && \
    pip3 install --upgrade --no-cache $TENSORFLOW_INSTALL && \
    pip3 install --upgrade --no-cache $TORCH_INSTALL

COPY test.py /test.py

CMD ["python3", "/test.py"]
