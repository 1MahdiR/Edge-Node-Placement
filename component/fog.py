
class Fog:
    def __init__(self, _id: int, is_server_placed: bool, server_count: int):
        self._id = _id
        self.is_server_placed = is_server_placed
        self.server_count = server_count

    def __repr__(self):
        return "<Fog #%d>" % self._id

    def __str__(self):
        return (
                "<Fog #%d%s>" %
                (self._id, ", ROUTER" if not self.is_server_placed else
                ", %d servers" % self.server_count)
        )