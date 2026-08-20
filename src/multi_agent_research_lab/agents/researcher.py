"""Researcher agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.state import ResearchState
from multi_agent_research_lab.services.search_client import SearchClient


class ResearcherAgent(BaseAgent):
    """Collects sources and creates concise research notes."""

    name = "researcher"

    def __init__(self, search_client: SearchClient | None = None) -> None:
        self.search_client = search_client or SearchClient()

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.sources` and `state.research_notes`.

        TODO(student): Implement search, source filtering, citation capture, and notes.
        """

        state.sources = self.search_client.search(state.request.query, state.request.max_sources)
        state.research_notes = "\n".join(
            f"[{i + 1}] {source.title}: {source.snippet}"
            for i, source in enumerate(state.sources)
        )
        state.add_trace_event(self.name, {"sources": len(state.sources)})
        return state
