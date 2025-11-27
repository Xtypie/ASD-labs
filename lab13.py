from typing import Any


class HashTab:
    def __init__(self, cap=100, load_factor=0.75):
        self.items_count = 0
        self.load_factor = load_factor
        self.cap = cap
        self.table = [None] * cap

    def hash_func(self, key, size=None) -> int:
        if not size: size = self.cap

        return int(hash(key)) % size

    def __rehash(self) -> list[None]:

        self.cap *= 2
        new_table = [None] * self.cap
        for key in self.table:
            if not key: continue
            self.__insert(key, new_table)

        return new_table

    def __insert(self, key, table) -> bool:

        index = self.hash_func(key, size=len(table))
        while table[index] != None:
            if table[index] == key: return False
            index = (index + 1) % len(table)
        table[index] = key

        return True

    def insert(self, key) -> None:

        was_inserted = self.__insert(key, self.table)
        if not was_inserted: return
        self.items_count += 1
        load_factor = self.items_count / len(self.table)
        if (load_factor > self.load_factor):
            self.table = self.__rehash()
            self.load_factor = load_factor

    def search(self, key):

        index = self.hash_func(key)
        while (self.table[index] != None):
            if (self.table[index] == key): return index
            index = (index + 1) % len(self.table)

        return -1

    def delete(self, key) -> None:

        index = self.search(key)
        if index > -1:
            self.table[index] = None
            self.items_count -= 1

    def __str__(self):
        result = []
        for i in range(self.cap):
            if self.table[i] is not None:
                result.append(f"[{i}]: {self.table[i]}")
        return "\n".join(result)


if __name__ == "__main__":
    hashtab = HashTab(cap = 5, load_factor = 0.75)

    txt = [ 'hello', 'bbbb', 'cccc', 'hy', 'bye', 'go', 'hash']

    for el in txt:
        hashtab.insert(el)

    print(hashtab)

