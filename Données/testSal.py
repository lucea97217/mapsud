#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# widget manipulation
from ipywidgets import widgets, interact, interactive, fixed, interact_manual

from download import download  # download data / avoid re-downloading
from IPython import get_ipython

pd.options.display.max_rows = 8

# %%
url = "http://josephsalmon.eu/enseignement/datasets/titanic.csv"
path_target = "./titanic.csv"
download(url, path_target, replace=False)  # if needed `pip install download`

# %%
df_titanic_raw = pd.read_csv("titanic.csv")

# %%
df_titanic_raw.tail(n=3)

# %%
df_titanic_raw.head(n=5)

# %%
pd.NA == 1


# %%
np.nan==1
#%%
df_titanic = df_titanic_raw.dropna()
df_titanic.tail(3)

# %%
def hist_explore(
    dataset=df_titanic,
    variable=df_titanic.columns,
    n_bins=24,
    alpha=0.25,
    density=False,
):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.hist(
        dataset[variable], density=density, bins=n_bins, alpha=alpha
    )  # standardization
    plt.ylabel("Density level")
    plt.title(f"Dataset {dataset.attrs['name']}:\n Histogram for passengers' age")
    plt.tight_layout()
    plt.show()


interact(
    hist_explore,
    dataset=fixed(df_titanic),
    n_bins=(1, 50, 1),
    alpha=(0, 1, 0.1),
    density=True,
)
# %%
