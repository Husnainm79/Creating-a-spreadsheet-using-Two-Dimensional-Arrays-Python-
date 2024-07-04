import sys

class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None   # 2D array of values
        self.rows = 0       
        self.cols = 0
        self.cursor=[0,0]   # cursor's current position
        self.selection = [None, None, None, None]
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------
        
        
        #======================
        
#======================
    def CreateSheet(self, rows, cols):
         self.sheet = [[None for _ in range(cols)] for _ in range(rows)]
         self.rows = rows
         self.cols = cols
         
         #raise NotImplementedError
#======================

#======================
    def Goto(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            # Update the cursor's position
            self.cursor = [row, col]
        else:
            print("Invalid row or column values. Cursor not moved.")
        
        #raise NotImplementedError
#======================

#======================        
    def Insert(self, val):
       
        if (0 <= self.cursor[0] < self.rows) and (0 <= self.cursor[1] < self.cols):
            # Insert the value at the cursor location
            self.sheet[self.cursor[0]][self.cursor[1]] = val
        else:
            print("Cursor is outside the bounds of the spreadsheet. Cannot insert.")
        #raise NotImplementedError
#======================

#======================        
    def Delete(self):
        if (0 <= self.cursor[0] < self.rows) and (0 <= self.cursor[1] < self.cols):
            # Erase the contents of the cell (set it to None)
            self.sheet[self.cursor[0]][self.cursor[1]] = None
        else:
            print("Cursor is outside the bounds of the spreadsheet. Cannot delete.")

        #raise NotImplementedError
#======================

#======================    
    def ReadVal(self):
        if (0 <= self.cursor[0] < self.rows) and (0 <= self.cursor[1] < self.cols):
            # Get the value at the cursor location
            value = self.sheet[self.cursor[0]][self.cursor[1]]
            print(value)  # Print the value
            return value
        else:
            print("Cursor is outside the bounds of the spreadsheet. Cannot read value.")
            return None
        
        #raise NotImplementedError
#======================

#======================    
    def Select(self,row, col):   
        if (0 <= self.cursor[0] < self.rows) and (0 <= self.cursor[1] < self.cols):
            # Set the upper left corner of the selection rectangle to the cursor position
            upper_left = [self.cursor[0], self.cursor[1]]
            
            # Set the lower right corner of the selection rectangle based on the provided row and col
            lower_right = [row, col]
            
            # Update the self.selection member variable
            self.selection = upper_left + lower_right
        else:
            print("Cursor is outside the bounds of the spreadsheet. Cannot select.")

        #raise NotImplementedError
#======================

#======================        
    def GetSelection(self):
        return tuple(self.selection)  # Return the current selection as a tuple
        #raise NotImplementedError
#======================

#======================        
    def Sum(self,row,col):
        # Check if there's a valid selection; if not, use the cursor position as the selection
        if self.selection[0] is not None:
            start_row, start_col, end_row, end_col = self.selection
        else:
            start_row, start_col = end_row, end_col = self.cursor

        # Initialize the sum to 0
        total_sum = 0

        # Iterate through the cells within the selection
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    cell_value = self.sheet[i][j]
                    if cell_value is not None:
                        total_sum += cell_value

        # Store the sum at the position indicated by row and col
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.sheet[row][col] = total_sum
        else:
            print("Invalid destination cell. Sum not stored.")
        
        #raise NotImplementedError
#======================

#======================    
    def Mul(self,row,col):
        # Check if there's a valid selection; if not, use the cursor position as the selection
        if self.selection[0] is not None:
            start_row, start_col, end_row, end_col = self.selection
        else:
            start_row, start_col = end_row, end_col = self.cursor
        # Initialize the product to 1
        total_product = 1

        # Iterate through the cells within the selection
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    cell_value = self.sheet[i][j]
                    if cell_value is not None:
                        total_product *= cell_value

        # Store the product at the position indicated by row and col
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.sheet[row][col] = total_product
        else:
            print("Invalid destination cell. Product not stored.")
             
        #raise NotImplementedError
#======================

#======================        
    def Avg(self,row,col):
        # Check if there's a valid selection; if not, use the cursor position as the selection
        if self.selection[0] is not None:
            start_row, start_col, end_row, end_col = self.selection
        else:
            start_row, start_col = end_row, end_col = self.cursor

        # Initialize variables for calculating the sum and count of non-empty cells
        total_sum = 0
        cell_count = 0

        # Iterate through the cells within the selection
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    cell_value = self.sheet[i][j]
                    if cell_value is not None:
                        total_sum += cell_value
                        cell_count += 1

        # Calculate the average, considering non-empty cells
        if cell_count > 0:
            average = total_sum / cell_count
        else:
            average = None

        # Store the average at the position indicated by row and col
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.sheet[row][col] = average
        else:
            print("Invalid destination cell. Average not stored.")

           
        #raise NotImplementedError
#======================

#======================
    def Max(self,row, col):
        # Check if there's a valid selection; if not, use the cursor position as the selection
        if self.selection[0] is not None:
            start_row, start_col, end_row, end_col = self.selection
        else:
            start_row, start_col = end_row, end_col = self.cursor

        # Initialize the maximum to None
        max_value = None

        # Iterate through the cells within the selection
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                if 0 <= i < self.rows and 0 <= j < self.cols:
                    cell_value = self.sheet[i][j]
                    if cell_value is not None:
                        if max_value is None or cell_value > max_value:
                            max_value = cell_value

        # Store the maximum at the position indicated by row and col
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.sheet[row][col] = max_value
        else:
            print("Invalid destination cell. Maximum not stored.")
        
        #raise NotImplementedError
#======================

#======================
    def PrintSheet(self):
        # Create and print column headers
        column_headers = "row/col:   " + "   ".join([str(i) for i in range(self.cols)])
        print(column_headers)

        # Iterate through rows and print cell contents
        for i in range(self.rows):
            row_data = "{:<3}  ".format(i)  # Display the row number with left alignment
            for j in range(self.cols):
                cell_value = self.sheet[i][j]
                if cell_value is not None:
                    row_data += "{:<8}  ".format(cell_value)  # Adjust spacing for alignment with left alignment
                else:
                    row_data += " " * 8 + "  "  # Display empty cell
            print(row_data)
        # Raise NotImplementedError("PrintSheet function is not implemented yet")

#======================

            
#======================
#======================
#    BONUS
#======================
    def Undo(self):
        '''
        Undoes the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        #raise NotImplementedError

#----------------------

    def Redo(self):
        '''
        Redoes the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        #raise NotImplementedError

#----------------------

    def Save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        try:
            with open(fileName, 'w') as file:
                # Write the dimensions (rows and columns) to the file
                file.write(f"{self.rows} {self.cols}\n")
                
                # Write the cell values to the file
                for row in self.sheet:
                    row_values = [str(val) if val is not None else "" for val in row]
                    file.write(" ".join(row_values) + "\n")

            print(f"Spreadsheet data saved to {fileName}")
        except IOError as e:
            print(f"Error saving the spreadsheet: {e}")
        
        #raise NotImplementedError

#----------------------

    def Load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        #raise NotImplementedError



    def Quit(self):
        
        print("Exiting the program.")
        sys.exit(0)
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    # Create an instance of the Spreadsheet class
    sheet = Spreadsheet()
    
    # Create a new 5x5 spreadsheet
    sheet.CreateSheet(10, 10)
    
    # Example: Move to position (2, 2) and insert a value
    sheet.Goto(2, 2)
    sheet.Insert(8)

    # Example: Move to position (2, 3) and insert a value
    sheet.Goto(2, 3)
    sheet.Insert(6)
    # Example: Move to position (3, 5) and insert a value
    sheet.Goto(2, 1)
    sheet.Insert(9)
    sheet.Save("my_spreadsheet.txt")
    # Print the spreadsheet to see the changes
    sheet.PrintSheet()
    
    # Example: Select a range from (1, 1) to (3, 3)
    sheet.Select(3, 3)
    
    # Get the current selection
    selection = sheet.GetSelection()
    print(f"Current selection: {selection}")
    
    # Perform a Sum operation 
    sheet.Sum(2, 3)
    # Perform a Mul operation 
    sheet.Mul(6, 5)
    # Perform a Avg operation 
    sheet.Avg(5, 5)
    
    
    # Print the spreadsheet again to see the changes
    sheet.PrintSheet()
    
    # exit the program
    sheet.Quit()

if __name__ == '__main__':
    main()
    
#======================


 
