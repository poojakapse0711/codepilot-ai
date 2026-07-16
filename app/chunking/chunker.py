from langchain_text_splitters import RecursiveCharacterTextSplitter


class CodeChunker:
    """Splits source code into chunks."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ) -> None:
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, text: str) -> list[str]:
        """Split source code into chunks."""

        return self.splitter.split_text(text)