from databasedb.binary_tree import BinaryTree
from databasedb.physical import Storage

class DatabaseDB(object):

    def __init__(self, f):
        self._storage = Storage(f)
        self._tree: BinaryTree = BinaryTree(self._storage)

    def _assert_not_closed(self) -> None:
        if self._storage.closed:
            raise ValueError('Database closed.')

    def close(self) -> None:
        self._storage.close()

    def commit(self) -> None:
        self._assert_not_closed()
        self._tree.commit()

    def __getitem__(self, key: str) -> str:
        self._assert_not_closed()
        return self._tree.get(key)

    def __setitem__(self, key, value):
        self._assert_not_closed()
        return self._tree.set(key, value)

    def __delitem__(self, key):
        self._assert_not_closed()
        return self._tree.pop(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def __len__(self):
        return len(self._tree)