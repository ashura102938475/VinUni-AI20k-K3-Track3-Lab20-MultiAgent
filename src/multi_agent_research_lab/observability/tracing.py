"""Tracing hooks.

This file intentionally avoids binding to one provider. Students can plug in LangSmith,
Langfuse, OpenTelemetry, or simple JSON traces.
"""

from collections.abc import Iterator
from contextlib import contextmanager
from time import perf_counter
from typing import Any

from multi_agent_research_lab.core.config import get_settings


@contextmanager
def trace_span(name: str, attributes: dict[str, Any] | None = None) -> Iterator[dict[str, Any]]:
    """Minimal span context used by the skeleton.

    TODO(student): Replace or augment with LangSmith/Langfuse provider spans.
    """

    started = perf_counter()
    span: dict[str, Any] = {"name": name, "attributes": attributes or {}, "duration_seconds": None}
    observation = None
    settings = get_settings()
    if settings.langfuse_public_key and settings.langfuse_secret_key:
        try:
            from langfuse import get_client

            observation = get_client().start_as_current_observation(
                as_type="span", name=name, metadata=attributes or {}
            )
        except ImportError:
            span["langfuse"] = "install langfuse to enable remote tracing"
    try:
        yield span
    finally:
        span["duration_seconds"] = perf_counter() - started
        if observation is not None:
            observation.update(metadata={"duration_seconds": span["duration_seconds"]})
            observation.end()
