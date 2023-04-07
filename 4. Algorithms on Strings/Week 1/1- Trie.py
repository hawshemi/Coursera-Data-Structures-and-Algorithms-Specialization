import sys
from collections import deque


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


class TrieNode:
    def __init__(self, parent, value, node_id):
        self.parent = parent
        self.value = value
        self.node_id = node_id

        self.children = dict()

    def add_child(self, value, node_id):
        self.children[value] = TrieNode(self, value, node_id)


class Trie:
    def __init__(self, patterns):
        self.patterns = patterns

        self.tree = TrieNode(None, None, 0)
        self._construct_trie(self.patterns)

    def _construct_trie(self, patterns):
        node_id = 1

        for pattern in patterns:
            cur = self.tree
            for c in pattern:
                if c not in cur.children:
                    cur.add_child(c, node_id)
                    node_id += 1

                cur = cur.children[c]

    def print_adj_list(self):
        q = deque([self.tree])

        while q:
            cur = q.popleft()

            if cur.value is not None:
                print("{}->{}:{}".format(cur.parent.node_id, cur.node_id, cur.value))

            for node in cur.children.values():
                q.append(node)


def run_test():
    patterns = (
        "ATAGA",
        "ATC",
        "GAT",
    )
    tree = Trie(patterns)
    tree.print_adj_list()


def run_algo():
    patterns = sys.stdin.read().split()[1:]
    tree = Trie(patterns)
    tree.print_adj_list()


if __name__ == "__main__":
    # run_test()
    run_algo()