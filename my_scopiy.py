def find_intervents(row, mn, name):
    """
    Класифікує рядок

    Ця функцiя приймае строку та повертае клас до якоi вона вiноситься.
    Крiм строки ще подаеться список значень для класифiкацii та назви
    класу

    Аргументи:
    row (str): Строка для класифiкацii
    mn (str, list, set): Список з множествами
    якi служать для визначення до якоi групи вiднести запис
    name (str, list): Список назв класiв
    
    """
    row_set = set(row.split(","))
    for index, value in enumerate(range(len(mn))):
        element = len(mn[index] & row_set)
        if element > 0:   
              return name[index]

        
if __name__ == "__main__":
    
    mn = [{'a', 'b'}, {'c', 'd'}, {'e', 'f'}]
    mnn = "f,c,a,f,j,k,m,n,c,e"
    name = ['Колоноскопия', 'Эндоскопия', 'Гистероскопия']

    print(find_intervents(mnn, mn, name))

