"""Optional critic agent skeleton for bonus work."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.state import ResearchState


class CriticAgent(BaseAgent):
    """Optional fact-checking and safety-review agent."""

    name = "critic"

    def run(self, state: ResearchState) -> ResearchState:
        """Validate final answer and append findings.

        TODO(student): Add fact-check, citation coverage, or hallucination checks.
        """

        answer = state.final_answer or ""
        cited = sum(f"[{i}]" in answer for i in range(1, len(state.sources) + 1))
        coverage = cited / len(state.sources) if state.sources else 0.0
        if not answer:
            state.errors.append("critic: final answer is empty")
        elif state.sources and coverage < 1.0:
            state.errors.append(f"critic: citation coverage {coverage:.0%}")
        state.add_trace_event(self.name, {"citation_coverage": coverage})
        return state
