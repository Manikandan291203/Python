
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def change(a, b, c):
    # Validate input and position
    if 1 <= b <= 9 and a[b-1] not in ['X', 'O']:
        a[b-1] = c
    else:
        print("Invalid move or position already taken.")
    
def show(a):
    for i in range(len(a)):
        if i % 3 == 0:
            print("\n------------")
        print(a[i], "|", end=" ")
    print("\n------------")

def wins(c):
    # Check for winning conditions
    if ((c[0] == 'X' and c[1] == 'X' and c[2] == 'X') or
        (c[0] == 'X' and c[3] == 'X' and c[6] == 'X') or
        (c[0] == 'X' and c[4] == 'X' and c[8] == 'X') or
        (c[2] == 'X' and c[4] == 'X' and c[6] == 'X') or
        (c[1] == 'X' and c[4] == 'X' and c[7] == 'X') or
        (c[3] == 'X' and c[4] == 'X' and c[5] == 'X') or
        (c[6] == 'X' and c[7] == 'X' and c[8] == 'X') or
        (c[2] == 'X' and c[5] == 'X' and c[8] == 'X')):
        return 'X'
    
    elif ((c[0] == 'O' and c[1] == 'O' and c[2] == 'O') or
          (c[0] == 'O' and c[3] == 'O' and c[6] == 'O') or
          (c[0] == 'O' and c[4] == 'O' and c[8] == 'O') or
          (c[2] == 'O' and c[4] == 'O' and c[6] == 'O') or
          (c[1] == 'O' and c[4] == 'O' and c[7] == 'O') or
          (c[3] == 'O' and c[4] == 'O' and c[5] == 'O') or
          (c[6] == 'O' and c[7] == 'O' and c[8] == 'O') or
          (c[2] == 'O' and c[5] == 'O' and c[8] == 'O')):
        return 'O'
    
    return None

c = 'X' 

for j in range(9):
    b = int(input("Enter position (1-9): "))
    
    change(a, b, c)
    show(a)
    
    winner = wins(a)
    if winner:
        print(winner+'wins')
        break
    elif all(cell in ['X', 'O'] for cell in a):
        print("Match tie!")
        break
    
    # Switch player
    c = 'O' if c == 'X' else 'X'



    