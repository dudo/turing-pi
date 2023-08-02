# Secrets

<https://github.com/external-secrets/external-secrets>

Secrets are stored within TODO Secret manager. We use the External Secrets Operator to create standard k8s secrets. Two critical secrets are:

- git-auth

  Flux uses this to pull repo changes from GitHub.

- registry-auth

  Flux watches for changes to image tags, and pulls them in (from ghcr.io)

Anything else you need **secret**, add an `ExternalSecret` resource that points to the secret within TODO.
