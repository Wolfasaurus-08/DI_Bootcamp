magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magician():
    for magician in magician_names:
        print (magician)
show_magician()
def make_great():
    for i in range(len(magician_names)):
        magician_names[i] += " the great"
make_great()
show_magician()

