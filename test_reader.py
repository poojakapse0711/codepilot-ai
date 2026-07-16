from app.repository.repository_loader import RepositoryLoader
from app.repository.file_reader import FileReader

loader = RepositoryLoader()
reader = FileReader()

files = loader.load_repository(".")

print(f"Found {len(files)} files\n")

content = reader.read(files[0])

print(files[0])
print("-" * 50)
print(content[:500])