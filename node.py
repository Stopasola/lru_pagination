class Node:
    def __init__(self, data, reference_bit):
        self.data = data
        self.reference_bit = reference_bit
        self.next = self
