FROM nvcr.io/nvidia/l4t-cuda:11.4.19-runtime

ARG MAJOR=11
ARG MINOR=4
ARG PATCH=1

ENV PATH /usr/local/cuda/bin${PATH:+:$PATH}
ENV LD_LIBRARY_PATH /usr/local/cuda/lib64${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}

RUN apt update && apt install -y make g++ wget

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/arm64/cuda-keyring_1.1-1_all.deb && \
    dpkg -i cuda-keyring_1.1-1_all.deb && \
    apt update && apt install -y cuda-${MAJOR}-${MINOR}

WORKDIR /usr/src/app

RUN wget --no-check-certificate https://github.com/NVIDIA/cuda-samples/archive/refs/tags/v$MAJOR.$MINOR.$PATCH.tar.gz
RUN tar -xzvf v$MAJOR.$MINOR.$PATCH.tar.gz

WORKDIR /usr/src/app/cuda-samples-$MAJOR.$MINOR.$PATCH/Samples/deviceQuery

RUN make

CMD ["./deviceQuery"]
