#! /bin/env python3

# --------

from enum import StrEnum
from secrets import randbelow

# --------

class Piece(StrEnum):
    PAWN = "p",
    KING = "K",
    QUEEN = "Q",
    BISHOP = "B",
    KNIGHT = "N",
    ROOK = "R",

    def whiteSymbolNo(self):
        match self:
            case Piece.KING:
                return 0x2654
            case Piece.QUEEN:
                return 0x2655
            case Piece.ROOK:
                return 0x2656
            case Piece.BISHOP:
                return 0x2657
            case Piece.KNIGHT:
                return 0x2658
            case Piece.PAWN:
                return 0x2659
            case _:
                raise LookupError(f"No symbol for {self}")

    def blackSymbolNo(self):
        return self.whiteSymbolNo() + 0x6

    def symbolNo(self, white=True):
        return self.whiteSymbolNo() if white else self.blackSymbolNo()

    # TODO: Think of mechanism to invert colors again on dark-mode terminals
    def symbol(self, white=True):
        return chr(self.symbolNo(white))

# --------

def positionNoToPieceArray(positionNo):

    pieceArray = [None] * 8

    kingTableIndex, bishopTableIndex = divmod(positionNo, 16)

    whiteDarkSquareBishopIndex, whiteLightSquareBishopIndex = divmod(bishopTableIndex, 4)
    pieceArray[whiteDarkSquareBishopIndex * 2] = Piece("B")
    pieceArray[whiteLightSquareBishopIndex * 2 + 1] = Piece("B")

    kingTable = [

        "QNNRKR",
        "NQNRKR",
        "NNQRKR",
        "NNRQKR",
        "NNRKQR",
        "NNRKRQ",
        "QNRNKR",
        "NQRNKR",
        "NRQNKR",
        "NRNQKR",
        "NRNKQR",
        "NRNKRQ",

        "QNRKNR",
        "NQRKNR",
        "NRQKNR",
        "NRKQNR",
        "NRKNQR",
        "NRKNRQ",
        "QNRKRN",
        "NQRKRN",
        "NRQKRN",
        "NRKQRN",
        "NRKRQN",
        "NRKRNQ",

        "QRNNKR",
        "RQNNKR",
        "RNQNKR",
        "RNNQKR",
        "RNNKQR",
        "RNNKRQ",
        "QRNKNR",
        "RQNKNR",
        "RNQKNR",
        "RNKQNR",
        "RNKNQR",
        "RNKNRQ",

        "QRNKRN",
        "RQNKRN",
        "RNQKRN",
        "RNKQRN",
        "RNKRQN",
        "RNKRNQ",
        "QRKNNR",
        "RQKNNR",
        "RKQNNR",
        "RKNQNR",
        "RKNNQR",
        "RKNNRQ",

        "QRKNRN",
        "RQKNRN",
        "RKQNRN",
        "RKNQRN",
        "RKNRQN",
        "RKNRNQ",
        "QRKRNN",
        "RQKRNN",
        "RKQRNN",
        "RKRQNN",
        "RKRNQN",
        "RKRNNQ",

    ]

    piecesPlaced = 0

    for file in range(8):
        if pieceArray[file] is None:
            pieceArray[file] = Piece(kingTable[kingTableIndex][piecesPlaced])
            piecesPlaced += 1

    return pieceArray

def printPosition(positionNo):

    pieceArray = positionNoToPieceArray(positionNo)

    print("black")
    print()
    print("a b c d e f g h")

    for piece in pieceArray:
        print(piece.symbol(white=False), end=" ")
    print()
    for piece in pieceArray:
        print(Piece("p").symbol(white=False), end=" ")
    print()

    print(f"\n{positionNo}\n")

    for piece in pieceArray:
        print(Piece("p").symbol(white=True), end=" ")
    print()
    for piece in pieceArray:
        print(piece.symbol(white=True), end=" ")
    print()

    print("a b c d e f g h")
    print()
    print("white")

# --------

def getPositionNo():
    useStandardPosition = False
    #useStandardPosition = True
    return 518 if useStandardPosition else randbelow(960)

# --------

def run():
    printPosition(getPositionNo())

# --------

if __name__ == "__main__":
    run()

