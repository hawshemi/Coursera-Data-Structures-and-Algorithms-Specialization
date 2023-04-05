# python3

class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        if self.ranks[src_parent] < self.ranks[dst_parent]:
            src_parent, dst_parent = dst_parent, src_parent
        self.parents[dst_parent] = src_parent
        self.row_counts[src_parent] += self.row_counts[dst_parent]
        self.max_row_count = max(self.max_row_count, self.row_counts[src_parent])
        if self.ranks[src_parent] == self.ranks[dst_parent]:
            self.ranks[src_parent] += 1
        return True

    def get_parent(self, table):
        # find parent and compress path
        if self.parents[table] != table:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
