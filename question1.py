class Ball_Brick:

    def __init__(self,border_array,sizeOfMatrix):
        self.line_array = []
        self.border_array = border_array

        for i in range(sizeOfMatrix):
            self.line_array = []

            for j in range(sizeOfMatrix):

                if i == 0 or j == 0 or i == sizeOfMatrix-1 or j == sizeOfMatrix-1:
                    self.line_array.append('W')

                else:
                    self.line_array.append(' ')

            self.border_array.append(self.line_array)
        
        self.mid = sizeOfMatrix//2
        
        for i in range(sizeOfMatrix):

            if i > 0 and i <sizeOfMatrix-1:

                if i == self.mid:
                    self.border_array[sizeOfMatrix-1][i] = 'o'

                else:
                    self.border_array[sizeOfMatrix-1][i] = 'G'

    def insert_data_into_array(self,data_array):
        for i in data_array:
            self.border_array[i[0]][i[1]] = i[2]
        
    def display_output(self,sizeOfMatrix):
        for i in range(sizeOfMatrix):
            for j in range(sizeOfMatrix):
                print(self.border_array[i][j],end="")
            print()

size_of_matrix = int(input("Enter size of the NxN matrix:"))
data_array = []

while True:
    data = list(map(int,input("Enter the brick's position and the brick type:").split()))
    data_array.append(data)
    termination = input("Do you want to continue(Y or N)")

    if termination == 'n' or termination == 'N':
        break

Ball_Count = int(input("Enter ball count:"))
result_array = []
obj = Ball_Brick(result_array,size_of_matrix)
obj.insert_data_into_array(data_array)
obj.display_output(size_of_matrix)
print("Ball Count is ",Ball_Count)