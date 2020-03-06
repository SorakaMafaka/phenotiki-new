import random
import numpy as np

def update_graph(self):
    fs = 500
    f = random.randint(1, 100)
    ts = 1 / fs
    length_of_signal = 100
    t = np.linspace(0, 1, length_of_signal)

    cosinus_signal = np.cos(2 * np.pi * f * t)
    sinus_signal = np.sin(2 * np.pi * f * t)

    self.MplWidget.canvas.axes.clear()
    self.MplWidget.canvas.axes.plot(t, cosinus_signal)
    self.MplWidget.canvas.axes.plot(t, sinus_signal)
    self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
    self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
    self.MplWidget.canvas.draw()