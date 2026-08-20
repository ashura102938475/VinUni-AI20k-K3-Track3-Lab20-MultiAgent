"""Skeleton guard test.

NOTE(student): Test này chỉ xác nhận skeleton còn nguyên TODO. Sau khi bạn implement
SupervisorAgent, test này SẼ FAIL - đó là điều bình thường. Hãy xóa hoặc thay thế nó
bằng unit test thật cho routing policy của bạn.
"""

from multi_agent_research_lab.agents import SupervisorAgent
from multi_agent_research_lab.core.schemas import ResearchQuery, SourceDocument
from multi_agent_research_lab.core.state import ResearchState


def test_supervisor_routes_missing_sources_to_researcher() -> None:
    state = ResearchState(request=ResearchQuery(query="Explain multi-agent systems"))
    SupervisorAgent().run(state)
    assert state.route_history == ["researcher"]


def test_supervisor_routes_complete_state_to_done() -> None:
    state = ResearchState(
        request=ResearchQuery(query="Explain multi-agent systems"),
        sources=[SourceDocument(title="source", snippet="evidence")],
        research_notes="notes",
        analysis_notes="analysis",
    )
    SupervisorAgent().run(state)
    assert state.route_history == ["writer"]
