class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]

        if original_color == color:
            return image
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        rows, cols = len(image), len(image[0])

        stack = [(sr, sc)]

        while stack:
            x,y = stack.pop()
            image[x][y] = color
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == original_color:
                    stack.append((nx, ny))

        return image