import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.add_new_tab('https://duckduckgo.com', 'DuckDuckGo')
        self.initUI()

        self.history = []  # Store browsing history

    def initUI(self):
        navbar = QToolBar()
        self.addToolBar(navbar)

        # ... (Existing button creation code remains unchanged)

        history_button = QAction('History', self)
        history_button.triggered.connect(self.show_history)
        navbar.addAction(history_button)

        self.history_table = QTableWidget()
        self.history_table.setColumnCount(2)
        self.history_table.setHorizontalHeaderLabels(['Title', 'URL'])
        self.history_table.cellClicked.connect(self.load_from_history)

    def add_new_tab(self, url, title="New Tab"):
        # ... (Existing tab creation code remains unchanged)

        # Add page to history when a new tab is created
        self.history.append({'title': title, 'url': url})
        self.update_history_table()

    def navigate_home(self):
        # ... (Existing navigation code remains unchanged)

        self.history.append({'title': 'Home', 'url': 'https://duckduckgo.com'})
        self.update_history_table()

    def navigate_to_url(self):
        # ... (Existing navigation code remains unchanged)

        current_tab = self.active_webview()
        self.history.append({'title': current_tab.title(), 'url': current_tab.url().toString()})
        self.update_history_table()

    def show_history(self):
        self.history_table.setRowCount(len(self.history))
        for i, page in enumerate(self.history):
            title_item = QTableWidgetItem(page['title'])
            url_item = QTableWidgetItem(page['url'])
            self.history_table.setItem(i, 0, title_item)
            self.history_table.setItem(i, 1, url_item)
        self.history_table.resizeColumnsToContents()
        history_dialog = QDialog(self)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(self.history_table)
        history_dialog.setLayout(dialog_layout)
        history_dialog.setWindowTitle('History')
        history_dialog.exec_()

    def load_from_history(self, row, column):
        url = self.history[row]['url']
        self.active_webview().setUrl(QUrl(url))

    def update_history_table(self):
        self.history_table.setRowCount(len(self.history))
        for i, page in enumerate(self.history):
            title_item = QTableWidgetItem(page['title'])
            url_item = QTableWidgetItem(page['url'])
            self.history_table.setItem(i, 0, title_item)
            self.history_table.setItem(i, 1, url_item)
        self.history_table.resizeColumnsToContents()

    # ... (Other methods remain unchanged)
