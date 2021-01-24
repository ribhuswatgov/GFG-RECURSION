class Hanoi:
    moves = 0  # stores count of moves. You need to update the count in this variable

    def toh(self, N, fromm, to, aux):
        if N == 1:
            print("Move disk {} from rod {} to rod {} \n".format(N, fromm, to))
            Hanoi.moves+=1
            return
            
        self.toh(N-1, fromm, aux, to)
        print("Move disk {} from rod {} to rod {} \n".format(N, fromm, to))
        Hanoi.moves+=1
        self.toh(N-1, aux, to, fromm)

import math

def main():
    
    N = int(input("Enter no of Rings: "))
    Hanoi.moves = 0
    h = Hanoi()
    h.toh(N,1,3,2)
    print(Hanoi.moves)

if __name__ == "__main__":
    main()
