from pathlib import Path


class FileReader:
    """Reads source code files."""

    def read(self, file_path: Path) -> str:
        """
        Read and return file contents.
        """

        try:
            return file_path.read_text(encoding="utf-8")

        except UnicodeDecodeError:
            return file_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )