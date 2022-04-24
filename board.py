class tic_tac_toe:
    def __init__(self):
        
        # self.Board = [[' ',' ',' '],
        #  [' ',' ',' '],
        #  [' ',' ',' ']]
        self.Board={'1':' ', '2':' ', '3':' ', '4':' ', '5':' ', '6':' ','7':' ','8':' ','9':' '}
        self.avail_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def printBoard (self):
        print (self.Board['1'], ' | ', self.Board['2'], ' | ', self.Board['3'])
        print ('-------------')
        print (self.Board['4'], ' | ', self.Board['5'], ' | ', self.Board['6'])
        print ('-------------')
        print (self.Board['7'], ' | ', self.Board['8'], ' | ', self.Board['9'])
        print ()

    def play(self, move, player):       
        
        if move in self.avail_moves:
        
            if player == 1:

                self.Board[str(move)] = '0'                
                self.avail_moves.remove(move)
                
                
            elif player == 2:

                self.Board[str(move)] = 'X'
                self.avail_moves.remove(move)
        
            #tick_tack_toe.print_board(self)
            
        else: 
           
            print('Enter a valid move')
            #tick_tack_toe.print_board(self)
            
        return self.Board, self.avail_moves
    def check_winner(self):
    
        for i in ['X', 'O']:

            for s in [(1, 2, 3), (1, 4, 7), (7, 8, 9), (3, 6, 9), (1, 5, 9), (3, 5, 7), (2, 5, 8), (4, 5, 6)]:

                if self.Board[str(s[0])] == i and self.Board[str(s[1])] == i and self.Board[str(s[2])] == i:
                    
                    
                    return i

                else:

                    pass
if __name__ == "__main__":
    
    tic_tac_toe()
    
    