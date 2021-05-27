class SGFWriter:
    
    def __init__(self, output_sgf):
        self.output_sgf = output_sgf

        self.letters = 'abcdefghijklmnopqrs'
        self.sgf = "(;GM[1]FF[4]CA[UTF-8]SZ[19]RU[Chinese]\n"