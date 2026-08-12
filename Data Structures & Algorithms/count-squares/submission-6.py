class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.left_diag = defaultdict(set)
        self.right_diag = defaultdict(set)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        self.left_diag[point[1]+point[0]].add(tuple(point))
        self.right_diag[point[1]-point[0]].add(tuple(point))
        

    def count(self, point: List[int]) -> int:
        output = 0

        for p in self.left_diag[point[1] + point[0]]:
            if p == tuple(point):
                continue

            p1 = tuple(p)
            p2 = tuple([point[0], p[1]])
            p3 = tuple([p[0], point[1]])
            if self.points[p3] * self.points[p1] * self.points[p2] > 0:
                print(p1, p2, p3,self.points[p3] * self.points[p1] * self.points[p2])
            
            output += self.points[p3] * self.points[p1] * self.points[p2]

        for p in self.right_diag[point[1] - point[0]]:

            if p == tuple(point):
                continue

            p1 = tuple(p)
            p2 = tuple([point[0], p[1]])
            p3 = tuple([p[0], point[1]])

            if self.points[p3] * self.points[p1] * self.points[p2] > 0:
                print(p1, p2, p3,self.points[p3] * self.points[p1] * self.points[p2])
            
            output += self.points[p3] * self.points[p1] * self.points[p2]


        return output
        
