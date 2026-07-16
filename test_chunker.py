from app.chunking.chunker import CodeChunker

chunker = CodeChunker()

text = "Hello World\n" * 300

chunks = chunker.split(text)

print(len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(len(chunk))