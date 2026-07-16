from app.chunking.chunking_service import ChunkingService

service = ChunkingService()

repository = service.chunk_repository(".")

print(f"Files: {len(repository)}")

for file_path, chunks in repository.items():
    print(file_path)
    print(f"Chunks: {len(chunks)}")
    print("-" * 50)