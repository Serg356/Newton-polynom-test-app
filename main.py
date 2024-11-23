from tkinter import *
from tkinter.messagebox import Message, ERROR
import matplotlib.pyplot as plt
import numpy as np
from lab4.plot_render import render_plot
from aproximation import back_interpolation

def f(x: np.ndarray):
    return np.sin(2*np.pi*np.sin(np.pi*x/2)**2)
def _quit():
    window.quit()
    window.destroy()

def render_interpolation(ax: plt.Axes, sep=0.01):
    try:
        dots = [float(val) for val in points_textbox.get().split(',')]
        for x, y in zip(dots, f(np.array(dots))):
            ax.plot(x, y, 'o', color='red')
        pol = back_interpolation(np.array(dots), f)
        x = np.arange(float(min_textbox.get()), float(max_textbox.get()), sep)
        ax.plot(x, [pol(x_i) for x_i in x])
        return pol
    except:
        Message(message='Точки введены неверно', icon=ERROR, title='Ошибка').show()
        return

def render_error_plot(ax: plt.Axes, f, pol, x_min, x_max, sep=0.01):
    x = np.arange(x_min, x_max, sep)
    ax.plot(x, f(x) - np.array([pol(x_i) for x_i in x]))
    ax.grid(color='black', linewidth=1.0)

def render_f_plot(ax, f, label, x_min, x_max, sep=0.01):
    x = np.arange(x_min, x_max, sep)
    ax.plot(x, f(x), label=label)
    ax.grid(color='black', linewidth=1.0)

def render_plots(f, label, x_min=0.0, x_max=1.0, sep=0.01):
    fig, axs = plt.subplots(2)
    render_f_plot(axs[0], f, label, x_min=x_min, x_max=x_max, sep=sep)
    pol = render_interpolation(axs[0])
    render_error_plot(axs[1], f,  pol, x_min=x_min, x_max=x_max, sep=sep)
    return fig, axs
def calc():
    try:
        x_min = float(min_textbox.get())
        x_max = float(max_textbox.get())
    except:
        Message(message='В поля диапазонов должны быть числа', icon=ERROR, title='Ошибка').show()
        return
    # fig, ax = get_plot(f, 'f(x) = Sin[2pi * Sin2(pi * x/2)]', x_min=x_min, x_max=x_max, sep=0.01)
    # render_interpolation(ax)
    # ax2 = plt.axes()
    # render_error_plot(ax2)
    fig, axs = render_plots(f, 'f(x) = Sin[2pi * Sin2(pi * x/2)]', x_min=x_min, x_max=x_max, sep=0.01)
    plot_win = Toplevel(window)
    plot_win.title('Результат')
    canvas, tool_bar = render_plot(fig, plot_win)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    plot_win.grab_set()



FONT = 'Times 20'

if __name__ == '__main__':
    window = Tk()
    window.title('Выч. мат')
    window.protocol('WM_DELETE_WINDOW', _quit)
    Label(window, text='Диапозон функции', font=FONT).pack()
    Label(window, text='От', font=FONT).pack()
    min_textbox = Entry(window, font=FONT)
    min_textbox.insert(0, 0)
    min_textbox.pack()
    Label(window, text='До', font=FONT).pack()
    max_textbox = Entry(window, font=FONT)
    max_textbox.insert(0, 1)
    max_textbox.pack()
    Label(window, text='Введите координаты точек через запятую', font=FONT).pack()
    points_textbox = Entry(window, font=FONT)
    points_textbox.insert(0, '0.1,0.3,0.5,0.7,0.8,0.9')
    points_textbox.pack()
    render_btn = Button(window, text='Рассчитать', command=calc , font=FONT)
    render_btn.pack()
    window.mainloop()