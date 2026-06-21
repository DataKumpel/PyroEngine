import pyray as pr
from pyro_engine_app import PyroEngineApp


WIN_WIDTH = 800
WIN_HEIGHT = 450


def main():
    pyro = PyroEngineApp(WIN_WIDTH, WIN_HEIGHT)
    pyro.run()


if __name__ == "__main__":
    main()
