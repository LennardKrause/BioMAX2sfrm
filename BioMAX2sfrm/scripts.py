import sys
from PyQt6 import QtGui, QtWidgets
import h5py, hdf5plugin
import BioMAX2sfrm
from BioMAX2sfrm.classes import ConversionWindow
from BioMAX2sfrm.functions import prepare_conversion, convert_to_sfrm

def run():
    app = QtWidgets.QApplication(sys.argv)
    font = QtGui.QFont()
    font.setStyleHint(QtGui.QFont.StyleHint.Monospace)
    app.setFont(font)
    app.setStyle('fusion')
    win = ConversionWindow(title=f'Convert MicroMAX / BioMAX to .sfrm, version {BioMAX2sfrm.__version__} (released {BioMAX2sfrm.__date__})',
                           fn_suffix='_master.h5',
                           header_ext=['Run', 'Kappa'],
                           # 'add': add to counter
                           # 'mul': multiply with counter
                           # None : insert value
                           header_val=[('add', 1), ('mul', 50)],
                           fc_prepare=prepare_conversion,
                           fc_process=convert_to_sfrm)
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run()
