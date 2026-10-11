from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QTabWidget, QLineEdit, QGridLayout, QHBoxLayout, QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
app = QApplication([])
window = QWidget()
converter_tab = QWidget()
Calc = QWidget()
tabs = QTabWidget()
tabs.addTab(Calc, "Calculator")
tabs.addTab(converter_tab, "Converter")
applayout = QVBoxLayout()
applayout.addWidget(tabs)
Calc.setWindowTitle('Calculator')
Calc.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
    }
    QLabel {
        color: white;
        font-size: 48px;
        padding: 20px;
        background-color: #1e1e1e;
        border-radius 10px;
    }
    QPushButton {
        font-size: 24px;
        color: white;
        background-color: #3c3c3c;
        border: none;
        border-radius: 10px;
        min-height: 80px;
    }
    QPushButton:hover {
        background-color: #505050;
    }
    QLineEdit {
        color: white;
        font-size: 48px;
    }
""")
converter_tab.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
    }
    QLabel {
        color: white;
        font-size: 13px;
        padding: 0px;
        background-color: transparent;
        border: none;
    }
    QPushButton {
        font-size: 15px;
        color: white;
        background-color: #ff9500;
        border: none;
        border-radius: 8px;
        padding: 10px;
        min-height: 0px;
    }
    QPushButton:hover {
        background-color: #ffb143;
    }
    QLineEdit {
        color: white;
        font-size: 18px;
        background-color: #1e1e1e;
        border: 1px solid #505050;
        border-radius: 8px;
        padding: 10px 12px;
    }
    QComboBox {
        font-size: 14px;
        color: white;
        background-color: #3c3c3c;
        border: 1px solid #505050;
        border-radius: 8px;
        padding: 8px 12px;
        min-height 20px;    
    }
    QComboBox QAbstractItemView {
        background-color: #3c3c3c;
        color: white;
        selection-background-color: #ff9500;
    }
""")
Calc.resize(500, 700)
Text = QLineEdit('0')
Text.setAlignment(Qt.AlignRight)
Text.setReadOnly(True)
Text.setFixedHeight(50)
ops = '+-*/'
def button_click(num):
    current = Text.text()
    if current == '0' or current == 'Error':
        if num in ops:
            return
        if num == '0':
            return
        if num == '.':
            Text.setText('0.')
            return
        Text.setText(num)
        return
    last = current[-1]

    import re
    parts = re.split(r'[+\-*/]', current)
    last_num = parts[-1]

    if num.isdigit() and last_num == '0':
        return

    if num in ops and last in ops:
        return

    if num == '.' and '.' in last_num:
        return
    Text.setText(current + num)
bttn1 = QPushButton('C')
bttn2 = QPushButton('0')
bttn3 = QPushButton('1')
bttn4 = QPushButton('2')
bttn5 = QPushButton('3')
bttn6 = QPushButton('4')
bttn7 = QPushButton('5')
bttn8 = QPushButton('6')
bttn9 = QPushButton('7')
bttn10 = QPushButton('8')
bttn11 = QPushButton('9')
bttn12 = QPushButton('=')
bttn13 = QPushButton('+')
bttn14 = QPushButton('-')
bttn15 = QPushButton('*')
bttn16 = QPushButton('/')
bttn17 = QPushButton('.')
def count():
    result = eval(Text.text())
    Text.setText(f"{result:.10g}")
bttn12.clicked.connect(count)
def clear():
    Text.clear()
bttn1.clicked.connect(clear)
for btn in [bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9, bttn10, bttn11, bttn13, bttn14, bttn15, bttn16, bttn17]:
    btn.clicked.connect(lambda checked, b=btn: button_click(b.text()))
for btn in [bttn1, bttn12, bttn13, bttn14, bttn15, bttn16, bttn17]:
    btn.setStyleSheet("QPushButton { background- color:#ff9500; color: white; font-size: 24px; border: none; border-radius: 10px; min-height: 80px;}QPushButton:hover { background-color: #ffb143; }")
main_layout = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH5 = QHBoxLayout()
layoutH6 = QHBoxLayout()
main_layout.setSpacing(8)
main_layout.setContentsMargins(10, 10, 10, 10)
layoutH1.addWidget(Text)
layoutH2.setSpacing(8)
layoutH2.addWidget(bttn9)
layoutH2.addWidget(bttn10)
layoutH2.addWidget(bttn11)
layoutH2.addWidget(bttn16)
layoutH3.setSpacing(8)
layoutH3.addWidget(bttn6)
layoutH3.addWidget(bttn7)
layoutH3.addWidget(bttn8)
layoutH3.addWidget(bttn15)
layoutH4.setSpacing(8)
layoutH4.addWidget(bttn3)
layoutH4.addWidget(bttn4)
layoutH4.addWidget(bttn5)
layoutH4.addWidget(bttn14)
layoutH5.setSpacing(8)
layoutH5.addWidget(bttn2)
layoutH5.addWidget(bttn17)
layoutH5.addWidget(bttn12)
layoutH5.addWidget(bttn13)
layoutH6.setSpacing(8)
layoutH6.addWidget(bttn1)
main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)
main_layout.addLayout(layoutH4)
main_layout.addLayout(layoutH5)
main_layout.addLayout(layoutH6)
Calc.setLayout(main_layout)
main_layout2 = QVBoxLayout()
lyout1 = QHBoxLayout()
lyout2 = QHBoxLayout()
lyout3 = QHBoxLayout()
lyout4 = QHBoxLayout()
lyout5 = QHBoxLayout()
Cate = QLabel("Category")
Type = QLabel("From / To") 
Arrow =  QPushButton("⇄")
txt = QLineEdit("Enter value")
txt2 = QLineEdit("Result")
Conv = QPushButton("Convert")
Arrow.setFixedSize(36, 36)
Arrow.setStyleSheet(
    "QPushButton { background-color : #505050; color: white; "
    "font-size: 16px; border-radius: 18px; padding: 0px; min-height: 0px; }"
    "QPushButton:hover { background-color: #666666; }"
)
def swap_units():
    fi = fromcombo.currentIndex()
    ti = tocombo.currentIndex()
    fromcombo.setCurrentIndex(ti)
    tocombo.setCurrentIndex(fi)
Arrow.clicked.connect(swap_units)
lyout1.addWidget(Cate)
lyout2.addWidget(Type)
main_layout2.addLayout(lyout1)
main_layout2.addLayout(lyout2)
main_layout2.addLayout(lyout3)
main_layout2.addLayout(lyout4)
main_layout2.addLayout(lyout5)
TEMP_UNITS = ["Celcius", "Fahrenheit", "Kelvin", "Reamur"]
LENGTH_TO_METERS = {"mm": 0.001, "cm": 0.01, "dm": 0.1, "m": 1.0, "km": 1000.0}
TIME_TO_SECONDS = {"second": 1, "minute": 60, "hour": 3600, "day": 86400}
CATEGORIES = {"Temperature": TEMP_UNITS, "Length": list(LENGTH_TO_METERS.keys()), "Time": list(TIME_TO_SECONDS.keys())}
category = QComboBox()
category.addItems(CATEGORIES.keys())
fromcombo = QComboBox()
tocombo = QComboBox()
def celcius_to(value, unit):
    if unit == "Celcius": return value
    if unit == "Fahrenheit": return value * 9/5 + 32
    if unit == "Kelvin": return value + 273.15
    if unit == "Reamur": return value * 4/5

def to_celcius(value, unit):
    if unit == "Celcius": return value
    if unit == "Fahrenheit": return (value - 32) * 5/9
    if unit == "Kelvin": return value - 273.15
    if unit == "Reamur": return value * 5/4

def conv_linear(value, from_unit, to_unit, unit_table):
    return value * unit_table[from_unit] / unit_table[to_unit] 

def convert_temperature(value, from_unit, to_unit):
    return celcius_to(to_celcius(value, from_unit), to_unit)

def do_convert():
    value = float(txt.text())
    category2 = category.currentText()
    from_unit = fromcombo.currentText()
    to_unit = tocombo.currentText()
    if category2 == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    if category2 == "Length":
        result = conv_linear(value, from_unit, to_unit, LENGTH_TO_METERS)
    if category2 == "Time":
        result = conv_linear(value, from_unit, to_unit, TIME_TO_SECONDS)
    txt2.setText(f"{result:.10g}")

def refresh_units():
    category2 = category.currentText()
    units = CATEGORIES[category2]
    fromcombo.clear(); fromcombo.addItems(units)
    tocombo.clear(); tocombo.addItems(units)
    if len(units) > 1:
        tocombo.setCurrentIndex(1)
category.currentIndexChanged.connect(refresh_units)
Conv.clicked.connect(do_convert)
txt2.setReadOnly(True)
lyout1.addWidget(category)
lyout2.addWidget(fromcombo)
lyout2.addWidget(Arrow)
lyout2.addWidget(tocombo)
lyout3.addWidget(txt)
lyout4.addWidget(Conv)
lyout5.addWidget(txt2)
converter_tab.setLayout(main_layout2)
window.setLayout(applayout)
window.show()
app.exec_()