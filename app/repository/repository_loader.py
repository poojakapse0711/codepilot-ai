from pathlib import Path


class RepositoryLoader:
    """Loads source code files from a repository."""

    SUPPORTED_EXTENSIONS = {
        ".py",
        ".java",
        ".js",
        ".ts",
        ".jsx",
        ".tsx",
    }

    def load_repository(self, repository_path: str) -> list[Path]:
        """
        Scan a repository and return supported source code files.
        """

        repository = Path(repository_path)

        if not repository.exists():
            raise FileNotFoundError(
                f"Repository does not exist: {repository_path}"
            )

        files = []

        for file in repository.rglob("*"):
            if (
                file.is_file()
                and file.suffix.lower() in self.SUPPORTED_EXTENSIONS
            ):
                files.append(file)

        return files