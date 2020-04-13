from data_structures.linked_list import LinkedList


class HashTable:
    fill_factor = 75
    initial_capacity = 100
    count = 0
    nodes_array = []

    def __init__(self, initial_capacity):
        self.initial_capacity = initial_capacity
        self.nodes_array.clear()
        for i in range(0, self.initial_capacity):
            self.nodes_array.append(LinkedList())

    def get_hashed_index(self, key):
        return hash(key) % len(self.nodes_array)

    def add(self, key, value):
        if self.count + 1 >= (self.initial_capacity * self.fill_factor / 100):
            raise Exception('Table is full. Auto extending of hash table is not yet implemented!')

        self.nodes_array[self.get_hashed_index(key)].add_end(value)  # TODO: add key/value pair into list
        self.count = self.count + 1

    def remove(self, key):
        self.nodes_array[self.get_hashed_index(key)].remove_end()  # TODO: remove by key
        self.count = self.count - 1

    def get(self, key):
        item = self.nodes_array[self.get_hashed_index(key)]
        return item.head.value if item.head is not None else None  # TODO: get by key

    def dump_table_content(self):
        for index, node in enumerate(self.nodes_array):
            print(f'index={index}, value={node.head.value}') if node.head is not None else print(
                f'index={index}, value=None')
