import matplotlib.pyplot as plt
import skrf
from skrf import plotting


class Plotter:
    @staticmethod
    def smith():
        fig, ax = plt.subplots()
        skrf.stylely()
        ax.set_title('namedPlot')
        plotting.smith(smithR=1, chart_type='z', draw_labels=False, border=False, ax=None, ref_imm=1.0,
                       draw_vswr=None)
        plotting.save_all_figs()
        return
