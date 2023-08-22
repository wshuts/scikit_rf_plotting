import matplotlib.pyplot as plt
import skrf
from skrf import plotting, Network


def setup_plot():
    fig, ax = plt.subplots()
    skrf.stylely()
    return ax


def save_all_figs():
    plotting.save_all_figs()


def create_network_from_data():
    ring_slot = Network('data/ring slot.s2p')
    return ring_slot


class Plotter:

    @staticmethod
    def smith():
        ax = setup_plot()
        ax.set_title('smith')
        plotting.smith(smithR=1, chart_type='z', draw_labels=False, border=False, ax=ax, ref_imm=1.0,
                       draw_vswr=None)
        save_all_figs()
        return

    @staticmethod
    def plot_smith():
        ax = setup_plot()
        ax.set_title('plot_smith')
        ring_slot = create_network_from_data()
        s11 = ring_slot.s[:, 0, 0]
        skrf.plotting.plot_smith(s11, smith_r=1, chart_type='z', x_label='Real', y_label='Imaginary',
                                 title='Complex Plane', show_legend=True, axis='equal', ax=None, force_chart=False,
                                 draw_vswr=None, draw_labels=False)
        save_all_figs()
        return
