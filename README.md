# Turing Pi 2 Kubernetes Cluster

Flux driven bare metal kubernetes cluster living on the edge.

![IMG_1022](https://user-images.githubusercontent.com/2963800/256379395-9535575e-c533-4981-aa85-0f44d37322ea.jpg)

## Getting Started

### Turing Pi

A compact AI & edge computing cluster.

```mermaid
mindmap
  root(clusters/local)
    apps
      home
        homebridge
        zigbee2MQTT
      sample
        graphql federated gateway
    charts
      cert manager
      cilium
      external secrets
      grafana lgtm
      metrics server
      nvidia device plugin
      postgres operator
      redpanda operator
    manifests
      GatewayClass
      Gateway
      RuntimeClass
    notifications
      slack error
      slack info
      webhook receiver
    secrets
```

#### Build

- [Densium APU](https://densium.net/products/densium-apu?Frontpanel=Dark+Walnut&Exterior=Black) 4L
- [Noctua NF-A14 ULN](https://noctua.at/en/products/fan/nf-a14-uln) 140mm
- [Pico PSU](https://turingpi.com/product/pico-psu/) 160w
- 3x [Turing RK1](https://turingpi.com/product/turing-rk1) 8 cores /  32 GB / 6 TOPS
- 1x [Nvidia Jetson Orin NX](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/#tech-specs) 8 cores /  16 GB / 100 TOPS
- 4x [Samsung 970 EVO Plus NVMe M.2 SSD](https://www.samsung.com/us/computing/memory-storage/solid-state-drives/ssd-970-evo-plus-nvme-m-2-250gb-mz-v7s250b-am/) 250GB

32 cores / 112 GB / 118 TOPS

1TB storage

<https://turingpi.com/>

### Kubernetes (via k0s)

An open-source system for automating deployment, scaling, and management of containerized applications.

<https://k0sproject.io/>

### Flux

Used to **pull** repository changes into kubernetes clusters.

<https://fluxcd.io>

### Brew

The Missing Package Manager for macOS (or Linux).

<https://brew.sh>

This repo includes a collection of dependencies to install:

```sh
brew bundle
```

## Usage

### Flux CLI

#### Bootstrap

When spinning up an env for the first time (you should never really need to do this, unless locally):

```sh
flux bootstrap github \
  --components-extra=image-reflector-controller,image-automation-controller \
  --owner=dudo \
  --repository=turing-pi \
  --private=false \
  --personal=true \
  --path=clusters/overlays/local
```

#### Useful Commands

```sh
flux suspend image update my-service
flux resume image update my-service

kubectl logs -n flux-system deploy/image-automation-controller

flux get all -A
kubectl get GitRepository -n flux-system
kubectl get Kustomization -n flux-system
kubectl get HelmRelease -n ingress-nginx
```

### Environment Variables

env are stored within `.env` files within their appropriate folder. These are then converted into configMaps via kustomize.

```yaml
configMapGenerator:
  - name: my-thing-config
    envs:
      - .env
```

Use the config map, per usual.

```yaml
envFrom:
  - configMapRef:
      name: my-thing-config
```

### Pertinent Sections

- [Apps](./apps)
- [Charts](./charts)
- [Clusters](./clusters)
- [Manifests](./manifests)
- [Notifications](./notifications)
- [Secrets](./secrets)
