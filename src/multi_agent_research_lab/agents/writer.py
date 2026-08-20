"""Writer agent skeleton."""

from multi_agent_research_lab.agents.base import BaseAgent
from multi_agent_research_lab.core.state import ResearchState


class WriterAgent(BaseAgent):
    """Produces final answer from research and analysis notes."""

    name = "writer"

    def run(self, state: ResearchState) -> ResearchState:
        """Populate `state.final_answer`.

        TODO(student): Synthesize a clear response with citations or source references.
        """

        citations = " ".join(f"[{i + 1}]" for i, _ in enumerate(state.sources))
        state.final_answer = (
            f"Question: {state.request.query}\n\n"
            f"{state.analysis_notes or state.research_notes or ''}\n\n"
            f"Sources: {citations}"
        )
        state.add_trace_event(self.name, {"citations": len(state.sources)})
        return state
