# Capstone architecture

Project code: **invoices-s05**.

## Components

- API behind a gateway (REST/GraphQL).
- Invoice service with field `amount`.
- Async queue for payment events.
- Metrics and tracing for latency and errors.

## Principles

Domain boundaries, idempotent webhooks, saga for distributed steps.
