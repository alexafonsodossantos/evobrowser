from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QtWebEngineWidgets.QWebEnginePage.NavigationTypeLinkClicked:
            return True
        return super(WebEnginePage, self).acceptNavigationRequest(url, _type, isMainFrame)

class HtmlView(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, windows, *args, **kwargs):
        super(HtmlView, self).__init__(*args, **kwargs)
        self.setPage(WebEnginePage(self))
        self._windows = windows
        self._windows.append(self)

    def createWindow(self, _type):
        if QtWebEngineWidgets.QWebEnginePage.WebBrowserTab:
            v = HtmlView(self._windows)
            v.resize(640, 480)
            v.show()
            return v

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    windows = []
    w = HtmlView(windows)
    w.load(QtCore.QUrl("https:/swdagencia.com/projetos/diskbreja"))
    w.show()
    sys.exit(app.exec_())