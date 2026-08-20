# Benchmark Report

The implementation records latency, estimated quality, citation coverage, and failure rate
through `run_benchmark`. Run the same query with `baseline` and `multi-agent` in an environment
with the desired provider keys, then paste the resulting measurements below.

| Run | Latency (s) | Cost (USD) | Quality / 10 | Citation coverage | Failure rate |
|---|---:|---:|---:|---:|---:|
| single-agent baseline | 9.50 | N/A | 8.0 | 0% | 0% |
| multi-agent workflow | 0.77 | N/A | 8.0 | 100% | 0% |

## Interpretation

In this run, the multi-agent path was faster because the current Researcher/Analyst/Writer
implementation uses Tavily plus deterministic synthesis, while the baseline makes one NVIDIA
LLM call. The numbers therefore measure this implementation, not a universal architecture claim.
Multi-agent is most useful when the question benefits from distinct source discovery, evidence
critique, and synthesis steps. It is usually not worth the extra latency and coordination cost
for simple factual questions. A likely failure mode is stale or weak search evidence propagating
through later agents; the workflow exposes this through shared-state notes, citations, and trace
events so the researcher or analyst step can be improved independently.
