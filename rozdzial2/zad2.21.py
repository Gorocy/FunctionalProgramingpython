def main():
    N =30

    trojkat_pitagorejski = [(a, b, c) for a in range(1, N) for b in range(a, N) for c in range(b, N) if(a*a+b*b==c*c)]

    print("trojkat pitagorejski z przedzialu 1 do ", N, "to : ",trojkat_pitagorejski, " .", sep="")
main()