from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Canvas
def get_plot(f, label, x_min=-10, x_max=10, sep=0.1) -> tuple[plt.Figure, plt.axes]:
    fig, ax = plt.subplots()
    x = np.arange(x_min, x_max, sep)
    ax.plot(x, f(x), label=label)
    ax.grid(color='black', linewidth=1.0)
    return fig, ax
def redraw_plot(ax: plt.Axes, f, label, x_min=-10, x_max=10, sep=0.1):
    ax.clear()
    x = np.arange(x_min, x_max, sep)
    ax.plot(x, f(x), label=label)
    ax.grid(color='black', linewidth=1.0)
    ax.legend(fontsize=12)
def render_plot(fig, parent) -> tuple[ FigureCanvasTkAgg, NavigationToolbar2Tk]:
    canvas = FigureCanvasTkAgg(fig, parent)
    toolbar = NavigationToolbar2Tk(canvas, parent)
    toolbar.update()
    return canvas, toolbar
