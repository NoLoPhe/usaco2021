fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
x, y = map(int, fin.readline().split())
sum = x + y
fout.write(str(sum) + '\n')
fout.close()