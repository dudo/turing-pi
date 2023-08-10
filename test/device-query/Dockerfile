FROM ubuntu:20.04

RUN apt update && apt install -y make g++ wget curl gnupg

ARG DISTRO=ubuntu2004
ARG ARCH=cross-linux-aarch64
ARG TARGET_ARCH=aarch64
ARG JETSON=r35.4
ARG CUDA=v11.4.1

RUN \
    echo "deb [signed-by=/usr/share/keyrings/cuda-archive-keyring.gpg] https://developer.download.nvidia.com/compute/cuda/repos/$DISTRO/$ARCH/ /" | tee /etc/apt/sources.list.d/cuda.list && \
    mkdir -p /usr/share/keyrings && \
    curl -L https://developer.download.nvidia.com/compute/cuda/repos/$DISTRO/$ARCH/cuda-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/cuda-archive-keyring.gpg

RUN \
    echo "deb https://repo.download.nvidia.com/jetson/common $JETSON main" | tee -a /etc/apt/sources.list.d/jetson.list && \
    echo "deb https://repo.download.nvidia.com/jetson/t194 $JETSON main" | tee -a /etc/apt/sources.list.d/jetson.list && \
    apt-key adv --fetch-key http://repo.download.nvidia.com/jetson/jetson-ota-public.asc && \
    mkdir -p /opt/nvidia/l4t-packages/ && \
    touch /opt/nvidia/l4t-packages/.nv-l4t-disable-boot-fw-update-in-preinstall && \
    apt update && \
    apt install -y --no-install-recommends nvidia-l4t-core cuda
RUN apt install -y nvidia-gds

WORKDIR /tmp

RUN wget --no-check-certificate https://github.com/NVIDIA/cuda-samples/archive/refs/tags/$CUDA.tar.gz
RUN tar -xzvf $CUDA.tar.gz --strip-components=1

WORKDIR /tmp/Samples/deviceQuery

RUN make TARGET_ARCH=$TARGET_ARCH

CMD ["./deviceQuery"]
