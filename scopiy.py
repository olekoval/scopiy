mn = [{'a', 'b'}, {'c', 'd'}, {'e', 'f'}]
mnn = "f,c,f,j,k,m,n,c,e"
name = ['Колоноскопия', 'Эндоскопия', 'Гистероскопия']

def find_intervents(row, mn, name):
    row_set = set(row.split(","))
    for index, value in enumerate(range(len(mn))):
        element = len(mn[index] & row_set)
        if element > 0:   
              return name[index]

        
