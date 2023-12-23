class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr_path = [0,0]
        path_set = set()
        path_set.add(tuple(curr_path))

        for direction in path:
            if direction == 'N':
                curr_path[1] += 1
            
            elif direction == 'S':
                curr_path[1] -= 1
            
            elif direction == 'E':
                curr_path[0] += 1
            
            elif direction == 'W':
                curr_path[0] -= 1
            
            if tuple(curr_path) in path_set:
                return True
            
            else:
                path_set.add(tuple(curr_path))
        
        return False