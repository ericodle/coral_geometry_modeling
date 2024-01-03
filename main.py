# main.py
from src.functions import *
from src.plotting import *

def main():
    # Generate plots for hemispheroid surface area productivity
    hemispheroid_SAP()

    # Generate plots for hemispheroid planar area productivity
    hemispheroid_PAP()

    # Generate plots for hemispheroid surface area to volume ratio
    hemispheroid_SVR()

    # Generate plots for branching coral surface area productivity
    branching_SAP()

    # Generate plots for branching coral surface area to volume ratio
    branching_SVR()

if __name__ == '__main__':
    main()
