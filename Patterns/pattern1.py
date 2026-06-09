#https://takeuforward.org/pattern/pattern-7-star-pyramid

class solution:
    def pattern(self,N):
        for i in range(N):
            for j in range(N-i-1):
                print(" ",end="")
            for j in range(2*i+1):
                print("*",end="")
            for j in range(N-i-1):
                print(" ",end="")
            print()
            
                

if __name__ == "__main__":
    sol = solution()
    sol.pattern(5)