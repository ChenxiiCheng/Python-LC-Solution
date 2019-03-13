'''
Question: 
  957. Prison Cells After N Days

Descrition: 
  There are 8 prison cells in a row, and each cell is either occupied or vacant.
  Each day, whether the cell is occupied or vacant changes according to the following rules:
  If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
  Otherwise, it becomes vacant.
  (Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
  We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
  Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)

Examples:

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

#Python3 Code:

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        #Solution 2
        count = 0
        N %= 14
        if N == 0:
            N = 14
        while count < N:
            newCell = [0] * 8
            for i in range(1, 7):
                if cells[i - 1] == cells[i + 1]:
                    newCell[i] = 1
                else:
                    newCell[i] = 0
            cells = newCell
            count += 1
        return cells
    
        
        #Solution 1
        #So, the state of the cells repeat every after 14 days. 
        #If N>14, we can simply do N = N%14. The only problem is when N%14 == 0, 
        #then we do not want the 0th state, but the 14th state, that is the last state.
        if N > 14:
            N = N % 14
        if N % 14 == 0:
            N = 14
        for i in range(1, N + 1):
            temp = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                if cells[i - 1] == cells[i + 1]:
                    temp[i] = 1
                else:
                    temp[i] = 0
            cells = temp
        return(cells)

        

