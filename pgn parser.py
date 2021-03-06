import chess
import chess.pgn
import os
import sys

os.chdir("c:\\users\\dweih\\chess")

class parser():
    def __init__( self, pgn_path = 'c:\\users\\dweih\\notebook\\chess\\twogames.pgn' , out_path = 'out.txt' ):
        try:
            self.pgn = open(pgn_path)
            self.out = open(out_path, 'w')
        except:
            print 'Error: ', sys.exc_info()[0]
        
    def writeNode( self, node, next_node ):
        self.out.write(node.board().fen() + ', ' + node.board().san(next_node.move) + '\n') 

    def scan( self ):
        game = chess.pgn.read_game(self.pgn)
        while game:
            node = game
            self.out.write("New game\n")
            while not node.is_end():
                next_node = node.variation(0)
                self.writeNode(node, next_node)
                node = next_node
            self.out.flush()
            game = chess.pgn.read_game(self.pgn)

    def close(self):
        self.pgn.close()
        self.out.close()  

