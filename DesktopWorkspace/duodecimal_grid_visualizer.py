# AROHA Framework: Duodecimal Grid Visualizer
import math

class DuodecimalGridVisualizer:
    def __init__(self, radius=12):
        self.radius = radius
        print(f"[Grid Visualizer] Initialized matrix radius: {self.radius}")

    def render_node_matrix(self):
        nodes = []
        for i in range(1, 13):
            angle = i * (360 / 12)
            rad = math.radians(angle)
            x = round(self.radius * math.cos(rad), 2)
            y = round(self.radius * math.sin(rad), 2)
            nodes.append({"node": i, "coord": (x, y)})
        return nodes

if __name__ == "__main__":
    viz = DuodecimalGridVisualizer()
    for n in viz.render_node_matrix():
        print(f"  Node {n['node']:2d} -> Coordinates: {n['coord']}")