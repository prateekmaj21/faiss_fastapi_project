import faiss
import numpy as np

# Initialize the FAISS index
dimension = 384  # Adjust based on the embedding dimension of the model used
index = faiss.IndexFlatL2(dimension)  # Using L2 distance (Euclidean)

# Save the index to a file (optional)
faiss.write_index(index, "faiss_index.bin")

# Load the index from a file (optional)
index = faiss.read_index("faiss_index.bin")
