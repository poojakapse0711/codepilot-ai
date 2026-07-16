from pathlib import Path

from app.repository.file_reader import FileReader
from app.repository.repository_loader import RepositoryLoader


class RepositoryService:
    """Service responsible for loading repository source code."""

    def __init__(self) -> None:
        self.loader = RepositoryLoader()
        self.reader = FileReader()

    def load_repository(self, repository_path: str) -> dict[Path, str]:
        """
        Load all supported source code files and their contents.
        """

        repository_files = self.loader.load_repository(repository_path)

        repository_content: dict[Path, str] = {}

        for file in repository_files:
            repository_content[file] = self.reader.read(file)

        return repository_content