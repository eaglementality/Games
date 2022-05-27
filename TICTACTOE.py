
name = input("Please Enter Your name : " )
message = 'Hope You Enjoy'

for i in message:
	print(i.center(10,'*'))
print('Hello\n' + name + '\nThanks for trying out my game')

theBoard = {'top-L': ' ','top-M': ' ','top-R': ' ',
            'mid-L': ' ','mid-M': ' ','mid-R': ' ',
            'low-L': ' ','low-M': ' ','low-R': ' '}
print('Use top-L, top-M, top-R', 'mid-L','mid-M', 'mid-R', 'low-L','low-M','low-R')
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'O'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


