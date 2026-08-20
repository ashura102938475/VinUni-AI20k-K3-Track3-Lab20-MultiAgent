"""Benchmark skeleton for single-agent vs multi-agent."""

from collections.abc import Callable
from time import perf_counter

from multi_agent_research_lab.core.schemas import BenchmarkMetrics
from multi_agent_research_lab.core.state import ResearchState

Runner = Callable[[str], ResearchState]


def run_benchmark(
    run_name: str, query: str, runner: Runner
) -> tuple[ResearchState, BenchmarkMetrics]:
    """Measure latency and return a placeholder metric object.

    TODO(student): Add quality scoring, estimated token cost, citation coverage, and error rate.
    """

    started = perf_counter()
    state = runner(query)
    latency = perf_counter() - started
    answer = state.final_answer or ""
    citations = sum(
        1
        for index, source in enumerate(state.sources, start=1)
        if (source.url and source.url in answer) or f"[{index}]" in answer
    )
    metrics = BenchmarkMetrics(
        run_name=run_name, latency_seconds=latency,
        estimated_cost_usd=state.estimated_cost_usd,
        quality_score=8.0 if state.final_answer else 0.0,
        citation_coverage=citations / len(state.sources) if state.sources else 0.0,
        failure_rate=1.0 if state.errors else 0.0,
        notes="completed" if state.final_answer else "failed",
    )
    return state, metrics
