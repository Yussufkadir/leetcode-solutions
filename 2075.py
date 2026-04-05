def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows 
        result = []

        for j in range(cols):
            x, y = 0, j                   
            while x < rows and y < cols:
                result.append(encodedText[x * cols + y])  
                x += 1                  
                y += 1                     

        return ''.join(result).rstrip()