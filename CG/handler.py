class handle_request:
    def handle_DDA(x1, y1, x2, y2):
        from algorithms import DDA
        algorithm = DDA.algo()
        algorithm.run(x1, y1, x2, y2)
    def handle_Bresenham(x1, y1, x2, y2):
        from algorithms import bresenhams
        algorithm = bresenhams.BresenhamAlgorithm()
        algorithm.run(x1, y1, x2, y2)
    def handle_circle(xc, yc, radius):
        from algorithms import mid_circle
        algorithms = mid_circle.MidpointCircleAlgorithm()
        algorithms.run(xc, yc, radius)
