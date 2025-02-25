from config.base_station import *

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
    NODES = []

    def __init__(self, _id: int, x: int, y: int, avg_load: float, avg_cycles: int, avg_data_size: int,
                 avg_num_connections: int, is_server_placed: bool, server_count: int, bandwidth: float,
                 num_access_points: int):
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

        # Wireless transmission properties
        # TODO: complete the data transmission rate properties
        self.bandwidth = bandwidth
        self.num_access_points = num_access_points

        # Base Station properties
        self.is_server_placed = is_server_placed
        self.server_count = server_count

        Node.NODES_COORDINATES.append((x, y))
        Node.NODES.append(self)

    def calculate_cost(self):
        return (FIXED_PLACEMENT_COST + VAR_PLACEMENT_COST * self.server_count +
                VAR_ACCESS_POINT_COST * self.num_access_points)

    def __repr__(self):
        return "<Node #%d>" % self._id

    def __str__(self):
        return (
                "<Node #%d, (%d,%d)%s>" %
                (self._id, self.x, self.y, ", ROUTER" if not self.is_server_placed else
                ", %d servers" % self.server_count)
        )
