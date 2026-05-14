# Security checklist

- Secrets from vault or CI variables only, never committed.
- Pin dependencies; run pip audit / SCA regularly.
- TLS on the edge; optional mTLS inside the mesh.
- Least-privilege service accounts in Kubernetes.
