from project_finder import *
from circle_finder import *

from master import *


def main():

    app = QApplication([])
    window = master()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
