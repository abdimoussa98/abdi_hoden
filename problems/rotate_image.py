class RotateImage(object):
    def rotateLayer(self, matrix, top, bottom, left, right ): 
        for i in range(right - left):
            # move bottom-left to top-left
            temp = matrix[top][left + i] #store the top-left in temp, so we only have 1 temp var
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom-right to bottom-left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top-right to bottom-right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top-left to top-right
            matrix[top + i][right] = temp

    def rotate(self, matrix):
        size = len(matrix)

        left = 0
        right = size - 1
        top = 0
        bottom = size - 1

        while(top < bottom and left < right):
            self.rotateLayer(matrix, top, bottom, left, right)
            top += 1
            bottom -= 1
            left += 1
            right -= 1
