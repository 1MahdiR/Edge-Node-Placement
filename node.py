CONST_FIXED_COST = 500
CONST_VAR_COST = 50


class Node:
    """
    Each node is representing a cell in the grid of map.
    This cell might contain pedestrians, vehicles, stationary devices, etc.
    Each cell contains one Base Station which is responsible for either computing the offloaded tasks in its operational
    area or transmitting the offloaded tasks.
    Transmitting the tasks happen in two cases:
    1) The base station has no computation resources and is mainly used in network as a router.
    2) The base station has no more capacity to compute more offloaded tasks.
    """

    NODES_COORDINATES = []  # Storing the nodes coordinates

    def __init__(self, _id: int, x: int, y: int, avg_load: float, avg_cycles: int, avg_data_size: int,
                 avg_num_connections: int, is_server_placed: bool, server_count: int, bandwidth: float):
        self._id = _id

        if (x, y) in self.NODES_COORDINATES:  # Checking if the node is uniquely placed
            raise Exception("Node already placed!")

        # Coordinates
        self.x = x
        self.y = y

        # User properties
        self.avg_load = avg_load
        self.avg_cycles = avg_cycles
        self.avg_data_size = avg_data_size
        self.avg_num_connections = avg_num_connections

        # Data transmission rate properties
        # TODO: complete the data transmission rate properties

        # Base Station properties
        self.is_server_placed = is_server_placed
        self.server_count = server_count

        Node.NODES_COORDINATES.append((x, y))

    def __repr__(self):
        return self._id

    def __str__(self):
        return (
                "<Node #%s, (%d,%d)%s>" %
                (self._id, self.x, self.y, ", ROUTER" if not self.is_server_placed else
                ", %d servers" % self.server_count)
        )
