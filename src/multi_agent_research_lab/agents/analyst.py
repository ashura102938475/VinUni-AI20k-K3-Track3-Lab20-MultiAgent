"""Analyst agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.state import ResearchState


class AnalystAgent(BaseAgent):
    """Turns research notes into structured insights."""

    name = "analyst"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.analysis_notes`.

        TODO(student): Extract key claims, compare viewpoints, and flag weak evidence.
        """

        notes = state.research_notes or "No research notes."
        state.analysis_notes = "Key evidence and caveats:\n" + notes
        state.add_trace_event(self.name, {"sources_reviewed": len(state.sources)})
        return state
