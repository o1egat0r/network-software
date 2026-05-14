# Security audit (bookings-s05)

Project code: **bookings-s05**.

Scope: Dockerfile and CI. Base image python:3.11-slim. Recommendation: run container as non-root USER in the final stage. No secrets found in compose examples. For production enable image signing and admission policy (OPA/Gatekeeper).
