# main.py

import os

from PyQt5.QtWidgets import (QApplication, QComboBox, QTextEdit, QVBoxLayout,
                             QWidget)
from PyQt5.QtGui import QFont
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

formatter = HtmlFormatter(cssclass='highlight')

class ScriptViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.combo = QComboBox()
        self.combo.addItems(['select', 'cs412_lab0_a.py', 'cs412_lab4_a.py', 'cs412_lab9_a.py'])
        self.combo.currentIndexChanged.connect(self.display_script)

        self.text = QTextEdit()
        self.text.setFont(QFont('monospace'))
        self.text.setLineWrapMode(QTextEdit.NoWrap)

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.text)
        self.setLayout(layout)

    def display_script(self, index):
        # formatter = HtmlFormatter(cssclass='highlight')
        script_name = self.combo.itemText(index)
        if script_name == 'select':
            script_path = 'labs/' + script_name + '.txt'
        else:
            scripts_dir = os.path.abspath('labs')
            script_path = os.path.join(scripts_dir, script_name)

        with open(script_path, 'r') as f:
            script_contents = f.read()

        # Use Pygments to highlight the syntax of the script
        highlighted_code = highlight(script_contents, PythonLexer(), formatter)

        # Set the HTML output as the HTML content of the text edit widget
        self.text.setHtml(highlighted_code)

        # Use a PyQt stylesheet to apply the styles to the text edit widget
        self.text.setStyleSheet(formatter.get_style_defs('.highlight'))





        # print(f'Opening file {script_path}')
        # try:
        #     with open(script_path, 'r') as f:
        #         script_contents = f.read()
        #         # highlighted_code = highlight(script_contents, PythonLexer(), HtmlFormatter())
        #         # self.text.setHtml(highlighted_code)
        # except Exception as e:
        #     print(f'Error opening file: {e}')
        #     return
        # # self.text.setPlainText(script_contents)
        # highlighted_code = highlight(script_contents, PythonLexer(), HtmlFormatter())
        # self.text.setHtml(highlighted_code)



app = QApplication([])
viewer = ScriptViewer()
viewer.show()
app.exec_()
