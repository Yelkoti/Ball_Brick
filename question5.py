class Ball_Brick:

    def __init__(self,border_array,sizeOfMatrix):
        self.sizeOfMatrix = sizeOfMatrix
        self.inner_wall_count = self.b_elemnt = 0
        self.line_array = []
        self.ball_count = Ball_Count
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

    def data_array_convertion(self,data_array):
        for i in range(len(data_array)):
            for j in range(3):

                if data_array[i][j] in ['ds','DS','Ds','dS']:
                    data_array[i][j] = 'S'

                elif data_array[i][j] in ['de','DE','De','dE']:
                    data_array[i][j] = 'E'

                elif data_array[i][j] in ['b','B']:
                    data_array[i][j] = 'B'

                else:
                    data_array[i][j] = int(data_array[i][j])

        return data_array


    def insert_data_into_array(self,data_array):

        for i in data_array:
            self.border_array[i[0]][i[1]] = i[2]
        
    def display_output(self,sizeOfMatrix):

        for i in range(sizeOfMatrix):
            for j in range(sizeOfMatrix):
                print(self.border_array[i][j],end="")

            print()
    def check_the_result(self):
        inner_loop = outter_loop = 0
        for i in range(1,self.sizeOfMatrix-1):
            for j in range(1,self.sizeOfMatrix-1):

                if self.border_array[i][j] != ' ':
                    break
            else:
                inner_loop +=1

        else:
            outter_loop +=1

        if inner_loop == self.sizeOfMatrix-2 and outter_loop == 1:
            return 'win'
        return

    def travers_the_ball(self,direction,sizeOFMatrix):

        if direction in ['ld','Ld','LD','lD']:

            if self.mid >= 2 and self.mid <= sizeOFMatrix-2:
                self.inner_wall_count = 0
                self.border_array[sizeOFMatrix-1][self.mid-1],self.border_array[sizeOFMatrix-1][self.mid] = self.border_array[sizeOFMatrix-1][self.mid],self.border_array[sizeOFMatrix-1][self.mid-1]
                self.mid = self.mid - 1
                self.destroy_the_cells()

            else:
                self.inner_wall_count = 0
                self.inner_wall_count +=1
                self.destroy_the_cells()

                if self.inner_wall_count >= 2:
                    self.ball_count -= 1
                return

        elif direction in ['RD','rd','Rd','rD']:

            if self.mid >= 1 and self.mid < sizeOFMatrix-2:
                self.inner_wall_count = 0
                self.border_array[sizeOFMatrix-1][self.mid+1],self.border_array[sizeOFMatrix-1][self.mid] = self.border_array[sizeOFMatrix-1][self.mid],self.border_array[sizeOFMatrix-1][self.mid+1]
                self.mid = self.mid + 1
                self.destroy_the_cells()

            else:
                self.inner_wall_count = 0
                self.inner_wall_count +=1
                self.destroy_the_cells()
                
                if self.inner_wall_count >= 2:
                    self.ball_count -= 1
                return
        
        else:
            self.inner_wall_count = 0
            self.destroy_the_cells()
            
    def destroy_the_cells(self):
        for i in range(self.sizeOfMatrix-2,-1,-1):

            if self.border_array[i][self.mid] == ' ':
                continue

            elif self.border_array[i][self.mid] == 'S':
                for k in range(-1,2,1):
                    for l in range(-1,2,1):

                        if self.border_array[i+k][self.mid+l] in ['W','o','G']:
                            continue

                        else:
                            self.border_array[i+k][self.mid+l] = ' '
                return

            elif self.border_array[i][self.mid] == 'E':
                for k in range(1,self.sizeOfMatrix-1,1):
                    self.border_array[i][k] = ' '
                return

            elif self.border_array[i][self.mid] == 'W':
                self.inner_wall_count +=1
                return

            elif self.border_array[i][self.mid] == 'B':
                self.border_array[i][self.mid] = ' '
                self.b_elemnt += 1

                if self.b_elemnt%2!=0:
                    self.border_array[self.sizeOfMatrix-1][self.mid+1] = '_'

                else:
                    self.border_array[self.sizeOfMatrix-1][self.mid-1] = '_'
                return

            else:
                self.border_array[i][self.mid] -= 1
                
                if self.border_array[i][self.mid] == 0:
                    self.border_array[i][self.mid] = ' '
                return


size_of_matrix = int(input("Enter size of the NxN matrix:"))
data_array = []

while True:
    data = list(map(str,input("Enter the brick's position and the brick type:").split()))
    data_array.append(data)
    termination = input("Do you want to continue(Y or N)")

    if termination == 'n' or termination == 'N':
        break

Ball_Count = int(input("Enter ball count:"))
result_array = []

obj = Ball_Brick(result_array,size_of_matrix)
data_array = obj.data_array_convertion(data_array)
obj.insert_data_into_array(data_array)
obj.display_output(size_of_matrix)
print("Ball Count is ",Ball_Count)

while obj.ball_count!=0:
    direction = input("Enter the direction in which the ball need to traverse:")
    obj.travers_the_ball(direction,size_of_matrix)
    obj.display_output(size_of_matrix)
    result_string = obj.check_the_result()
    
    if result_string == 'win':
        print("You win HURRAY..!!")
        break

    else:
        print("Ball Count is ",obj.ball_count)

else:
    print("You LOST")