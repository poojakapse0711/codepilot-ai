from pathlib import Path

from app.chunking.chunker import CodeChunker
from app.repository.repository_service import RepositoryService


class ChunkingService:
    """Creates chunks from repository source code."""

    def __init__(self) -> None:
        self.repository_service = RepositoryService()
        self.chunker = CodeChunker()

    def chunk_repository(
        self,
        repository_path: str,
    ) -> dict[Path, list[str]]:
        """
        Load a repository and split each file into chunks.
        """

        repository = self.repository_service.load_repository(repository_path)

        chunked_repository: dict[Path, list[str]] = {}

        for file_path, content in repository.items():
            chunked_repository[file_path] = self.chunker.split(content)

        return chunked_repository