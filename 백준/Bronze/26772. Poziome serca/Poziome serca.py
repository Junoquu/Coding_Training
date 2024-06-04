love=[' @@@   @@@  ',
      '@   @ @   @ ',
      '@    @    @ ',
      '@         @ ',
      ' @       @  ',
      '  @     @   ',
      '   @   @    ',
      '    @ @     ',
      '     @      ']

n=int(input())

for i in love:
    for j in range(n):
        print(i,end='')
    print()