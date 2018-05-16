class node:
    key = None

    def __init__(self, key):
        self.key = key
        self._edges = set()

    @property
    def edges(self):
        return self._edges

    @edges.setter
    def edges(self, n):
        if n not in self._edges:
            edges = self._edges
            edges.add(n)
            self._edges = edges
        if self not in n.edges:
            n.edges = (self)  # adds edge to other node

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)
