import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.vigenere import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data.get("encrypted_text", ""))
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/vigenere/decrypt"
        cipher_text = self.ui.txt_cipher_text.toPlainText()
        key = self.ui.txt_key.toPlainText()
        
        print(f"Cipher Text: {cipher_text}")  # In ra cipher_text
        print(f"Key: {key}")  # In ra key

        payload = {
            "cipher_text": cipher_text,
            "key": key
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                print(data)  # In ra phản hồi để kiểm tra
                decrypted_text = data.get("decrypted_text", "")
                if decrypted_text:  # Kiểm tra nếu có dữ liệu
                    self.ui.txt_plain_text.setPlainText(decrypted_text)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Decrypted Successfully")
                    msg.exec_()
                else:
                    print("Decrypted text is empty.")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())