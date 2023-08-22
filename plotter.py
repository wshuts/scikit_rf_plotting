import matplotlib.pyplot as plt
import skrf
from skrf import plotting


def setup_plot():
    fig, ax = plt.subplots()
    skrf.stylely()
    return ax


def save_all_figs():
    plotting.save_all_figs()


class Plotter:

    @staticmethod
    def smith():
        ax = setup_plot()
        ax.set_title('smith')
        plotting.smith(smithR=1, chart_type='z', draw_labels=False, border=False, ax=ax, ref_imm=1.0,
                       draw_vswr=None)
        save_all_figs()
        return
