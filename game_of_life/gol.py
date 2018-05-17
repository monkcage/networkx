import sys
from PyQt4 import QtGui, QtCore

class GameErea(QtGui.QWidget) :
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self._pos = []
        for i in range(20) :
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self._pos.append(arr)
        # print self._pos



    def paintEvent(self, QPaintEvent):
        QtGui.QWidget.paintEvent(self,QPaintEvent)
        step_x = self.width()/20
        step_y = self.height()/20

        painter = QtGui.QPainter(self)
        pen = QtGui.QPen()
        brush = QtGui.QBrush(QtCore.Qt.red, QtCore.Qt.SolidPattern)
        painter.setPen(pen)
        painter.setBrush(brush)
        for i in range(40) :
            painter.drawLine(0, i*step_y, self.width(), i*step_y)
            painter.drawLine(i*step_x, 0, i*step_x, self.height())
        painter.drawLine(self.width()-1, 0, self.width()-1, self.height())
        painter.drawLine(0, self.height()-1, self.width(), self.height()-1)


        for i in range(20) :
            for j in range(20) :
                if self._pos[i][j] == 1 :
                    # print self._pos[i][j]
                    painter.drawRect(i*step_x, j*step_y, step_x, step_y)
        pass


    def mousePressEvent(self, ev):
        x = ev.pos().x() / 20
        y = ev.pos().y() / 20
        self._pos[x][y] = 1
        # print self._pos
        # self.paintEvent(ev)
        self.update()

    def get_matrix(self):
        return self._pos

    def set_matrix(self, val):
        self._pos = val



class GameLife(QtGui.QWidget) :
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('Game of life')
        self.showUi()
        self._timer = QtCore.QTimer(self)
        pass

    def showUi(self):
        self._game_erae = GameErea(None)
        self._game_erae.setFixedSize(400, 400)
        self._btn_start = QtGui.QPushButton('Start', self)
        self._btn_stop = QtGui.QPushButton('Stop', self)

        self.connect(self._btn_start, QtCore.SIGNAL('clicked()'), self.slot_start)
        self.connect(self._btn_stop, QtCore.SIGNAL('clicked()'), self.slot_stop)


        layout_h = QtGui.QHBoxLayout()
        layout_h.addWidget(self._btn_start)
        layout_h.addWidget(self._btn_stop)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self._game_erae)
        layout.addLayout(layout_h)
        self.setLayout(layout)
        pass


    def slot_start(self):
        # print 'start'
        self._timer.timeout.connect(self._game_rule)
        self._timer.start(1000)

        pass

    def slot_stop(self):
        self._timer.stop()
        pass

    def _game_rule(self):
        matrix = self._game_erae.get_matrix()
        # size = len(matrix)

        mat_next = []
        for i in range(20) :
            arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            mat_next.append(arr)

        for i in range(1,19) :
            for j in range(1,19) :
                count = matrix[i-1][j-1] + matrix[i-1][j] + \
                    matrix[i-1][j+1] + matrix[i][j-1] +\
                    matrix[i][j+1] + matrix[i+1][j-1] +\
                    matrix[i+1][j] + matrix[i+1][j+1]
                if count == 2:
                    mat_next[i][j] = matrix[i][j]
                elif count == 3:
                    mat_next[i][j] = 1
                elif count > 3:
                    mat_next[i][j] = 0
                else:
                    mat_next[i][j] = 0
        self._game_erae.set_matrix(mat_next)
        self._game_erae.update()



if __name__ == '__main__' :
    app = QtGui.QApplication(sys.argv)
    view = GameLife()
    view.show()
    sys.exit(app.exec_())
