import sqlite3
import sys
import module
import csv
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QTableWidget, QListWidgetItem, QTreeWidgetItem, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
''''''''

class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('pr.ui', self)
        '''self.mw = module.MainWindow()'''
        self.arp = []
        self.derp = []
        self.sl = {}
        self.c = 0
        self.t_y = 0
        self.exp = {}
        self.setWindowTitle('Построитель')
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать базу данных', '',
            'База данных (*.db);;База данных (*.sqlite);;Все файлы (*);;Файл csv (*.csv)')[0]
        self.rassh = self.fname[len(self.fname) - self.fname[::-1].index('.'):]
        self.z = -1
        print(self.rassh)
        self.zerp = {self.fname[len(self.fname) - self.fname[::-1].index('/'):-3]: self.fname}
        if self.rassh == 'db' or self.rassh == 'sqlite':
            self.data_base = sqlite3.connect(self.fname)
        else:
            self.z += 1
        """self.pushButton.clicked.connect(self.select_data)
        # По умолчанию будем выводить все данные из таблицы films
        self.textEdit.setPlainText("SELECT * FROM films")"""
        self.select_data()
        self.tableWidget.cellClicked.connect(self.tab_cell_click)
        self.menuButton.clicked.connect(self.plot_window)
        self.revButton.clicked.connect(self.rev)
        '''self.listWidget.itemClicked.connect(self.list_click)'''
        self.chooseButton.clicked.connect(self.choose)
        self.treeWidget.itemClicked.connect(self.tree_click)

    def select_data(self):
        # Получим результат запроса,
        # который ввели в текстовое поле
        """query = self.textEdit.toPlainText()"""
        if self.rassh == 'db' or self.rassh == 'sqlite':
            names = self.data_base.cursor().execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
            print(names)
            print(self.fname[len(self.fname) - self.fname[::-1].index('/'):])
            self.arp.append(self.fname[len(self.fname) - self.fname[::-1].index('/'):])
            root  = QTreeWidgetItem(self.treeWidget)
            root.setText(0, self.fname[len(self.fname) - self.fname[::-1].index('/'):])
            for i in names:
                b = str(i)[2:-3]
                '''self.listWidget.addItem(QListWidgetItem(b))'''
                titm = QTreeWidgetItem(root)
                titm.setText(0, b)
                titm.setText(1, self.fname[len(self.fname) - self.fname[::-1].index('/'): -3])
            '''self.re_st(str(names[0])[2:-3])'''
        else:
            root  = QTreeWidgetItem(self.treeWidget)
            root.setText(0, self.fname[len(self.fname) - self.fname[::-1].index('/'):])
            root.setText(1, str(self.z))

    def closeEvent(self, event):
        # При закрытии формы закроем и наше соединение
        # с базой данных
        if self.rassh == 'db':
            self.data_base.close()
        else:
            pass

    def it(self):
        print(self.tableWidget.item(1, 1).text())
        self.tableWidget.cellClicked.connect(self.tab_cell_click)
        self.tableWidget.selectedItems.connect(self.tab_cells_click)

    def tab_cell_click(self, row, col):
        zap = self.tableWidget.item(row, col).text()
        cr = self.tableWidget.currentColumn()
        if zap.isdigit():
            self.exp[cr] = self.exp.get(cr, [])
            self.exp[cr] += [int(zap)]
        print(self.exp.items())
        if self.t_y:
            self.p_w.exp = self.exp

    def st_plt_window(self): # убрать
        print(self.p_w.yplt)
        if self.p_w.yplt == 1:
            self.derp.append(module.MainWindow(self.c))
            self.c += 1
            print(self.p_w.listWidget.currentItem().text())
            self.derp[-1].Graph(self.arp, type=self.p_w.listWidget.currentItem().text())



        self.arp.clear()

    def rev(self):
        print(self.derp)

    '''def list_click(self):
        print(self.listWidget.currentItem().text())

        print(self.listWidget.currentItem().text())
        self.re_st(self.listWidget.currentItem().text())'''

    def re_st(self, name, ob_name=None):
        self.data_base = sqlite3.connect(self.zerp[ob_name])
        res = self.data_base.cursor().execute(f"SELECT * FROM {name};").fetchall()
        c = len(self.data_base.cursor().execute(f"""select * from pragma_table_info('{name}');""").fetchall())
        self.tableWidget.setColumnCount(c)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def re_st_for_csv(self, name):
        with open(name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

    def plot_window(self):
        self.p_w = P_W(self.exp)
        self.t_y = 1

    def choose(self):
        self.fname = QFileDialog.getOpenFileName(
            self, 'Выбрать базу данных', '',
            'База данных (*.db);;База данных (*.sqlite);;Все файлы (*);;Файл csv (*.csv)')[0]
        if self.fname != '':
            if self.fname[len(self.fname) - self.fname[::-1].index('/'):] not in self.arp:
                print(self.rassh)
                self.rassh = self.fname[len(self.fname) - self.fname[::-1].index('.'):]
                print(self.rassh)
                self.data_base = sqlite3.connect(self.fname)
                self.zerp[self.fname[len(self.fname) - self.fname[::-1].index('/'):-3]] = self.fname
                self.select_data()

    def tree_click(self):
        cra = self.treeWidget.currentItem()
        if cra.text(0) not in self.arp:
            if '.csv' not in cra.text(0) or '.txt' not in cra.text(0):
                print(self.treeWidget.currentItem().text(1))
                print(self.zerp)
                self.re_st(cra.text(0), cra.text(1))
            else:
                self.re_st_for_csv(cra.text(0))


class P_W(QMainWindow):
    def __init__(self, exp):
        super().__init__()
        uic.loadUi('plot_window.ui', self)
        pm = QPixmap('sphx_glr_plot_thumb.jpg')
        self.label.setPixmap(pm)
        self.setWindowTitle('Меню графиков')
        self.listWidget.addItem(QListWidgetItem('pie'))
        self.listWidget.addItem(QListWidgetItem('plot'))
        self.listWidget.addItem(QListWidgetItem('bar'))
        self.listWidget.addItem(QListWidgetItem('stem'))
        self.listWidget.addItem(QListWidgetItem('step'))
        self.listWidget.addItem(QListWidgetItem('stackplot'))
        self.listWidget.addItem(QListWidgetItem('fill_between'))
        self.listWidget.addItem(QListWidgetItem('hist'))
        self.listWidget.addItem(QListWidgetItem('boxplot'))
        self.listWidget.addItem(QListWidgetItem('errorbar'))
        self.listWidget.addItem(QListWidgetItem('violinplot'))
        self.listWidget.addItem(QListWidgetItem('hexbin'))
        self.listWidget.addItem(QListWidgetItem('hist2d'))
        self.listWidget.addItem(QListWidgetItem('eventplot'))
        self.listWidget.addItem(QListWidgetItem('scatter'))
        self.yplt = 0
        self.derp = []
        self.c = 0
        self.exp = exp
        self.ims = {'pie': 'sphx_glr_pie_thumb.jpg',
                       'plot': 'sphx_glr_plot_thumb.jpg',
                       'bar': 'sphx_glr_bar_thumb.jpg',
                       'stem': 'sphx_glr_stem_thumb.jpg',
                       'step': 'sphx_glr_step_thumb.jpg',
                       'stackplot': 'sphx_glr_stackplot_thumb.jpg',
                       'fill_between': 'sphx_glr_fill_between_thumb.jpg',
                       'hist': 'sphx_glr_hist_plot_thumb.jpg',
                       'boxplot': 'sphx_glr_boxplot_plot_thumb.jpg',
                       'errorbar': 'sphx_glr_errorbar_plot_thumb.jpg',
                       'violinplot': 'sphx_glr_violin_thumb.jpg',
                       'hexbin': 'sphx_glr_hexbin_thumb.jpg',
                       'hist2d': 'sphx_glr_hist2d_thumb.jpg',
                       'eventplot': 'sphx_glr_eventplot_thumb.jpg',
                       'scatter': 'sphx_glr_scatter_thumb.jpg',
                       }
        self.plotButton.clicked.connect(self.st_plt_window)
        self.listWidget.itemClicked.connect(self.im_change)
        self.clearButton.clicked.connect(self.clear_exp)
        self.dialog = QDialog()
        self.dialog.setWindowTitle('Ошибка')
        self.dialog.setGeometry(200, 200, 200, 100)
        self.show()

    def plt_pls(self):
        self.yplt = 1

    def st_plt_window(self):
        self.derp.append(module.MainWindow(self.c))
        self.c += 1
        print(self.listWidget.currentItem().text())
        print(self.exp)
        self.derp[-1].Graph(self.exp, type=self.listWidget.currentItem().text())

    def im_change(self):
        pm =QPixmap(self.ims[self.listWidget.currentItem().text()])
        self.label.setPixmap(pm)

    def clear_exp(self):
        self.exp.clear()


class For_db:
    def __init__(self, db_path):
        self.ir = sqlite3.connect(db_path)
        self.cur = self.ir.cursor()

    def close_db(self):
        self.ir.close()

    def insert_to_db(self, values, table=1):
        columns = tuple([i[1] for i in self.cur.execute(f"""select * from pragma_table_info({table});""").fetchall()])
        print(columns)
        self.cur.execute(f"""INSERT INTO '{table}' {columns} {values};""")
        self.ir.commit()

    def select(self):
        return


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())