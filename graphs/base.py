"""Module serves as a Abstration for Graph Class
Author: Rajan Subramanian
Date: July 21, 2020
"""

class GraphBase:
    """Abstract Base Class representing Graph Structure"""

    class VertexBase:
        """Abstraction representing vertex of a graph"""

        def get_value(self):
            """return value associated with this vertex"""
            return self._value

        def __repr__(self):
            return """Vertex({!r})""".format(self._value)

    class EdgeBase:
        """Abstration represent Edge of a graph"""

        def __repr__(self):
            insert = (self._start, self._end, self._value)
            return """Edge(({!r}, {!r}): {:.2f}""".format(*insert)
        
        def endpoint(self):
            """return (u,v) as a tuple for vertices u and v"""
            return (self._start, self._end)
        
        def opposite(self, u):
            """return vertex opposite of u on this edge"""
            return self._end if u is self._start else self._start
        
        def get_value(self):
            """return value associated with this edge"""
            return self._value 
        
        def get_items(self):
            """returns edge attributes as a tuple
            Helpful for visualizing nodes and their edge weights"""
            return (self._start._value, self._end._value, self._value)