n = int(input())
roster = []
while n > 0:
    d = {
        1: 0
    }
    roster.append(d)
    d[1] = input()
    if len(roster) == n:
        print('Кол-во словарей:', len(roster), 'Их значения:', roster, sep='\n')
        break