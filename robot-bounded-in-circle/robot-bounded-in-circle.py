class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #basically check to see if eventually the robot will come back to the original position.
        #a cycle will exist at most 4 instruction cycles. just keeping track of coordinates will
        #do the trick.
        
        #Time: O(4 x N) = O(N) where N is the number of instructions
        #Space: O(1)
        
        #default case
        move_x = True
        move_y = False
        x, y = 0, 0
        constant = 1
        for _ in range(4):
            for command in instructions:
                if command == 'G':
                    x = x + constant if move_x else x
                    y = y + constant if move_y else y
                else:
                    temp_x = not move_x #get new positions
                    temp_y = not move_y

                    if (move_x and temp_y and command == 'R') or (move_y and temp_x and command == 'L'):
                        constant *= -1
                    move_x = temp_x
                    move_y = temp_y
                
            if x == 0 and y == 0:
                return True
        
        return False