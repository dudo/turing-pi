# Continuous Deployment

Flux driven kubernetes.

## Getting Started

### kubernetes

An open-source system for automating deployment, scaling, and management of containerized applications.

<https://kubernetes.io/>

### flux

Used to **pull** repository changes into kubernetes clusters.

<https://fluxcd.io/docs/guides/repository-structure/#repo-per-app>

### brew

The Missing Package Manager for macOS (or Linux).

<https://brew.sh>

```sh
brew bundle

export GITHUB_TOKEN=<your-token>
```

### kubectl

Kubernetes command line tool.

<https://docs.docker.com/get-started/orchestration>
<https://kubernetes.io/docs/reference/kubectl/>

## Usage

### Flux

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
- [Clusters](./clusters)
- [Charts](./charts)
- [Notifications](./notifications)
- [Secrets](./secrets)
