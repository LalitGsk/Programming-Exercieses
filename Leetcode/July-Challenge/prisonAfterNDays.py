'''
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation: 
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
'''

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        _dict = {}
        self.cells = cells
        for i in range(N):
            s = str(self.cells)
            if s in _dict:
                loop_len = i- _dict[s]
                left_days = (N-i)%loop_len
                return self.prisonAfterNDays(self.cells, left_days)
            else:
                _dict[s] = i
                prev = self.cells[0]
                for j in range(1,7):
                    curr, next = self.cells[j], self.cells[j+1]
                    self.cells[j] = 1 - (prev^next)
                    prev = curr
            self.cells[0], self.cells[7] = 0,0
            
        return self.cells
