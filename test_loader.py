from app.loaders.repository_loader import RepositoryLoader

loader = RepositoryLoader()

files = loader.load_repository(".")

for file in files:
    print(file)