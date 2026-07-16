from app.repository.repository_service import RepositoryService

service = RepositoryService()

repository = service.load_repository(".")

print(f"Files Loaded: {len(repository)}\n")

for path, content in repository.items():
    print(path)
    print(content[:100])
    print("-" * 50)