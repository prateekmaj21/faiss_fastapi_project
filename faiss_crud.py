import faiss
import numpy as np

class FAISSCRUD:
    def __init__(self, dimension=384, index_file="faiss_index.bin"):
        self.dimension = dimension
        self.index_file = index_file
        self.index = faiss.IndexFlatL2(dimension)
        self.id_to_embedding = {}
        self.next_id = 0
        
        # Load the index if it exists
        try:
            self.index = faiss.read_index(index_file)
        except:
            pass

    def create(self, embedding):
        self.index.add(np.array([embedding], dtype=np.float32))
        self.id_to_embedding[self.next_id] = embedding
        self.next_id += 1
        self.save_index()
        return self.next_id - 1

    def read(self, idx):
        return self.id_to_embedding.get(idx, None)

    def update(self, idx, new_embedding):
        if idx in self.id_to_embedding:
            self.index.remove_ids(np.array([idx]))
            #self.index.add_with_ids(np.array([new_embedding], dtype=np.float32), np.array([idx]))
            self.id_to_embedding[idx] = new_embedding
            self.save_index()
            return True
        return False

    def delete(self, idx):
        if idx in self.id_to_embedding:
            self.index.remove_ids(np.array([idx]))
            del self.id_to_embedding[idx]
            self.save_index()
            return True
        return False

    def save_index(self):
        faiss.write_index(self.index, self.index_file)
