import matplotlib.pyplot as plt
import skrf
from skrf import plotting, Network


class Plotter:

    @staticmethod
    def setup_plot():
        fig, ax = plt.subplots()
        skrf.stylely()
        return ax

    @staticmethod
    def save_all_figs():
        plotting.save_all_figs()

    @staticmethod
    def create_network_from_data():
        ring_slot = Network('data/ring slot.s2p')
        return ring_slot

    def smith(self):
        ax = self.setup_plot()
        ax.set_title('smith')
        plotting.smith(smithR=1, chart_type='z', draw_labels=False, border=False, ax=ax, ref_imm=1.0,
                       draw_vswr=None)

    def plot_smith(self):
        ax = self.setup_plot()
        ax.set_title('plot_smith')
        ring_slot = self.create_network_from_data()
        s11 = ring_slot.s[:, 0, 0]
        plotting.plot_smith(s11, smith_r=1, chart_type='z', x_label='Real', y_label='Imaginary',
                            title='Complex Plane', show_legend=True, axis='equal', ax=ax, force_chart=False,
                            draw_vswr=None, draw_labels=False)
