from src.data_map import Data_map 
from src.create_map import Create_map
class Manager:

    def __init__(self):
        self.views()
    

    def views(self):
        row, column = Data_map().welcome()
        print(row, column)
        Create_map(row, column).maker()