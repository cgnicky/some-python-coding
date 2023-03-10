class MyHashMap:

    def __init__(self):
        # Prime number for less collision
        self.size = 2069
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        bucket, idx = self.get_idx(key)
        if idx < 0:
            bucket.append((key, value))
        else:
            bucket[idx] = (key, value)
        
    def get(self, key: int) -> int:
        bucket, idx = self.get_idx(key)
        if idx < 0:
            return -1
        else:
            return bucket[idx][1]

    def remove(self, key: int) -> None:
        bucket, idx = self.get_idx(key)
        if idx < 0:
            return
        else:
            bucket.remove(bucket[idx])
    
    def _hash_key(self, key):
        return key % self.size
    
    def get_idx(self, key):
        # Using hashing function to get the index position in buckets array
        hashed_key = self._hash_key(key)
        bucket = self.buckets[hashed_key]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        
        return bucket, -1
