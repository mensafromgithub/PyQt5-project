import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import uic

matplotlib.use('Qt5Agg')


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, ind, width=5, height=4, dpi=100,  *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.sc = Graphs(self, width=5, height=4, dpi=100)
        """uic.loadUi('pr_plot.ui', self)
        self.combobox.addItems([self.sc.st_pie, self.sc.st_plot,
                        self.sc.st_bar, self.sc.st_scatter, self.sc.st_hist])"""
        self.setWindowTitle(f'График {str(ind)}')
        self.name = ''

    def BD(self):
        pass

    def Graph(self, values, labels=None, type=None):
        #self.combobox.currentData()(values)
        print(type)
        b = self.sc.lan[type](values)
        '''.legend(loc='lower left', bbox_to_anchor=(1, 0), labels=labels)'''
        if b:

            # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
            toolbar = NavigationToolbar(self.sc, self)

            layout = QtWidgets.QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(self.sc)

            # Create a placeholder widget to hold our toolbar and canvas.
            widget = QtWidgets.QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)
            self.show()

    def closeEvent(self, event):
        # Переопределить colseEvent
        self.name = self.windowTitle()


class Graphs(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Graphs, self).__init__(fig)
        self.lan = {'pie': self.st_pie,
               'plot': self.st_plot,
               'bar': self.st_bar,
               'stem': self.st_stem,
               'step': self.st_step,
               'stackplot': self.st_stackplot,
               'fill_between': self.st_fill_between,
               'hist': self.st_hist,
               'boxplot': self.st_boxplot,
               'errorbar': self.st_errorbar,
               'violinplot': self.st_violinplot,
               'hexbin': self.st_hexbin,
               'hist2d': self.st_hist2d,
               'eventplot': self.st_eventplot,
               'scatter': self.st_scatter,
               }

    def st_pie(self, exp):
        if len(exp) >= 1:
            v = exp[list(exp.keys())[0]]
            self.axes.pie(v)
            self.axes.axis('equal')
            return 1

    def st_plot(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vy = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.plot(vx, vy)
                self.axes.axis('equal')
                return 1

    def st_bar(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vh = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.bar(vx, vh)
                self.axes.axis('equal')
                return 1

    def st_stem(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vy = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.stem(vx, vy)
                self.axes.axis('equal')
                return 1

    def st_step(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vy = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.step(vx,vy)
                self.axes.axis('equal')
                return 1

    def st_stackplot(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vy = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.stackplot(vx, vy)
                self.axes.axis('equal')
                return 1

    def st_fill_between(self, exp):
        if len(exp) >= 3:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]) == len(exp[list(exp.keys())[2]]):
                vx, vy1, vy2 = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]], exp[list(exp.keys())[2]]
                self.axes.grid()
                self.axes.fill_between(vx, vy1, vy2)
                self.axes.axis('equal')
                return 1

    def st_hist(self, exp):
        if len(exp) >= 1:
            vx = exp[list(exp.keys())[0]]
            self.axes.grid()
            self.axes.hist(vx)
            self.axes.axis('equal')
            return 1

    def st_boxplot(self, exp):
        if len(exp) >= 1:
            vx = exp[list(exp.keys())[0]]
            self.axes.grid()
            self.axes.boxplot(vx)
            self.axes.axis('equal')
            return 1

    def st_errorbar(self, exp):
        if len(exp) >= 4:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]) == len(exp[list(exp.keys())[2]]) == len(exp[list(exp.keys())[3]]):
                vx, vy, vxerr, vyerr = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]], exp[list(exp.keys())[2]], exp[list(exp.keys())[2]]
                self.axes.grid()
                self.axes.errorbar(vx, vy, vxerr, vyerr)
                self.axes.axis('equal')
                return 1

    def st_violinplot(self, exp):
        if len(exp) >= 1:
            vd = exp[list(exp.keys())[0]]
            self.axes.grid()
            self.axes.violinplot(vd)
            self.axes.axis('equal')
            return 1

    def st_hexbin(self, exp):
        if len(exp) >= 3:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]) == len(exp[list(exp.keys())[2]]):
                vx, vy, vc = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]], exp[list(exp.keys())[2]]
                self.axes.grid()
                self.axes.hexbin(vx, vy, vc)
                self.axes.axis('equal')
                return 1

    def st_hist2d(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vy = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.hist2d(vx, vy)
                self.axes.axis('equal')
                return 1

    def st_eventplot(self, exp):
        if len(exp) >= 1:
            vd = exp[list(exp.keys())[0]]
            self.axes.grid()
            self.axes.eventplot(vd)
            self.axes.axis('equal')
            return 1

    def st_scatter(self, exp):
        if len(exp) >= 2:
            if len(exp[list(exp.keys())[0]]) == len(exp[list(exp.keys())[1]]):
                vx, vy = exp[list(exp.keys())[0]], exp[list(exp.keys())[1]]
                self.axes.grid()
                self.axes.scatter(vx, vy)
                self.axes.axis('equal')
                return 1