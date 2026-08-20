"""Search client abstraction for ResearcherAgent."""

from multi_agent_research_lab.core.config import get_settings
from multi_agent_research_lab.core.schemas import SourceDocument


class SearchClient:
    """Provider-agnostic search client skeleton."""

    def search(self, query: str, max_results: int = 5) -> list[SourceDocument]:
        """Search for documents relevant to a query.

        TODO(student): Implement with Tavily, Bing, SerpAPI, internal docs, or a local mock.
        """

        settings = get_settings()
        if settings.tavily_api_key:
            from tavily import TavilyClient
            results = TavilyClient(settings.tavily_api_key).search(
                query, max_results=max_results
            )["results"]
            return [
                SourceDocument(
                    title=result["title"],
                    url=result.get("url"),
                    snippet=result.get("content", ""),
                )
                for result in results
            ]
        return [
            SourceDocument(
                title=f"Local research result {i + 1}",
                url=None,
                snippet=f"Evidence related to: {query}",
            )
            for i in range(max_results)
        ]
