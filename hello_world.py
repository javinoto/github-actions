import os

def run():
    nombre = os.getenv("USERNAME")
    print(f'Hola {nombre} desde Github Actions!')

if __name__ == '__main__':
    run()
