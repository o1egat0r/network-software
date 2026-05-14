# Performance analysis (products-s05)

## Latency

Measured **latency** p95 for product catalog reads on the test bench: **45 ms** at 200 RPS. At 500 RPS latency grew to **120 ms**; the database became the bottleneck.

## Conclusions

For **products-s05**, cache hot lists and scale read replicas.
