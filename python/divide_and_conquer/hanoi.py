"""
Credit to https://gist.github.com/Brobin/9080107.
"""

class Tower:

    def __init__(self):
        self.counter = 0
"""
Runtime: O(2^N)
"""
    def hanoi(self, n, a, c, b):
        if n == 1:
            self.counter += 1
            print('{0}->{1}'.format(a, b))
        else:
            self.hanoi(n - 1, a, b, c)
            self.hanoi(1, a, c, b)
            self.hanoi(n - 1, b, c, a)


tower = Tower()
tower.hanoi(15, "source", "spare", "target")
print(tower.counter)