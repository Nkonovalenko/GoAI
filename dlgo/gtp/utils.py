class SGFWriter:
    
    def __init__(self, output_sgf):
        self.output_sgf = output_sgf

        self.letters = 'abcdefghijklmnopqrs'
        self.sgf = "(;GM[1]FF[4]CA[UTF-8]SZ[19]RU[Chinese]\n"

    def append(self, text):
        self.sgf = self.sgf + text

    def write_sgf(self):
        self.sgf = self.sgf + ")\n"
        with open(self.output_sgf, 'w') as f:
            f.write(self.sgf)
    