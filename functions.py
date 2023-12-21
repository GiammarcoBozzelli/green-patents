# libraries.py

import importlib

class LibraryInstaller:
    def __init__(self):
        self.libraries = ['numpy', 'pandas', 'seaborn', 'matplotlib', 'plotly', 'scipy', 'scikit-learn', 'statsmodels', 'linearmodels', 'stargazer', 'pycountry']
        self.missing_libraries = [lib for lib in self.libraries if importlib.util.find_spec(lib) is None]

        if self.missing_libraries:
            for lib in self.missing_libraries:
                !pip install {lib}
        else:
            print("All required libraries are already installed.")

def import_common_libraries():
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    import scipy.stats as stats
    from IPython.display import display
    from sklearn.linear_model import LinearRegression
    import statsmodels.api as sm
    from linearmodels.panel import PanelOLS
    from stargazer.stargazer import Stargazer
    import pycountry
    from IPython.display import Image, display, HTML
