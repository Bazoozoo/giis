__author__ = 'drain'


from PySide import QtCore, QtGui

from scene.SceneManager import SceneManger

class SceneView(QtGui.QGraphicsView):
    def __init__(self,parent = None):
        self.__sceneManager = SceneManger()
        super(SceneView,self).__init__(self.__sceneManager.getScene(),parent)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setFixedSize(self.sceneRect().width(),self.sceneRect().height())


