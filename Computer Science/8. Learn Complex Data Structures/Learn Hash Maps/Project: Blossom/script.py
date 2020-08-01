from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for items in range(self.array_size)]


  def hash(self, key):
    return sum(key.encode())


  def compress(self, hash_key):
    return hash_key % self.array_size


  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    list_at_array = self.array[array_index]
    payload = Node([key, value])

    for item in list_at_array:
      if item[0] == key:
        item[1] = value # if it's already in the LinkedList, why are we updateting the value? A: overwriting the value
        return

    list_at_array.insert(payload)


  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]

    else: # if payload[0] != key or payload[0] == None:
      return None

# TEST HERE

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
print(blossom.retrieve("morning glory"))
