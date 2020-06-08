zip_map = {'06770': 'Naugatuck, CT', '06403': 'Beacon Falls'}
other_zip_map = [('06770', 'Naugatuck CT',), ('06403', 'Beacon Falls')]


class HashMap(object):
    def __init__(self):
        self.hashmap = [[] for i in range(256)]

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def retrieve(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            return v
        raise KeyError


hm = HashMap()

hm.insert(other_zip_map[0][0], other_zip_map[0][1])
hm.insert(other_zip_map[1][0], other_zip_map[1][1])

print(hm.retrieve(other_zip_map[0][0]))
print(hm.retrieve(other_zip_map[1][0]))
