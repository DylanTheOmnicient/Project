import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from transposition_cipher_ui import Ui_MainWindow

def encrypt(text, key):
    rows = [text[i:i+key] for i in range(0, len(text), key)]
    if len(rows[-1]) < key:
        rows[-1] += ' ' * (key - len(rows[-1]))
    encrypted_text = ''.join([''.join(row[i] for row in rows) for i in range(key)])
    return encrypted_text

def decrypt(text, key):
    num_rows = len(text) // key
    columns = [text[i:i+num_rows] for i in range(0, len(text), num_rows)]
    decrypted_text = ''.join([''.join(columns[j][i] for j in range(key)) for i in range(num_rows)])
    return decrypted_text.strip()

class TranspositionCipherApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.processButton.clicked.connect(self.processText)

    def processText(self):
        text = self.textEdit.toPlainText()
        key = self.keyEdit.text()

        if not key.isdigit():
            QMessageBox.warning(self, 'Ошибка', 'Ключ должен быть числом!')
            return

        key = int(key)

        if self.encryptButton.isChecked():
            result = encrypt(text, key)
        else:
            result = decrypt(text, key)

        self.resultEdit.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TranspositionCipherApp()
    window.show()
    sys.exit(app.exec_())