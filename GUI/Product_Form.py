import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw

from Application.UI.ui_Product_Form import Ui_W_Product_Form
URL = "http://127.0.0.1:5000/api/"

class Form(qtw.QWidget, Ui_W_Product_Form):
    """This class is a product form it will handle both updating and creating new products for our application.
    """
    finished = qtc.Signal()
    def __init__(self, product_name:str = None) -> None:
        super().__init__()
        self.setupUi(self)
        self.gb.setTitle("Create Product")
        self.update_bool = False
        self.product_info = None
        if product_name:
            self.fetch_product(product_name)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_ok)

    def fetch_product(self, product_name) -> None:
        """This function is to prefill in the label edits of with product information.
        Prevents changing to name label as well.

        Args:
            product_name (str): Name of the product
        """

        self.gb.setTitle("Update Product")
        self.le_1.setText(product_name)
        product_name = self.le_1.text()
        get_url = URL + "product/" + product_name
        response = requests.get(get_url, json=product_name)
        content = json.loads(response.text)
        self.sb_price.setValue(content['price'])
        self.sb_quantity.setValue(content['quantity'])
        self.le_1.setDisabled(True)
        self.update_bool = True

    def update_request(self) -> None:
        """On Update it will send the request to the api to update the product.
        """        
        product_name = self.le_1.text()
        new_price = self.sb_price.value()
        new_quantity = self.sb_quantity.value()
        url = URL + "/product/" + product_name
        payload = {"price": new_price, "quantity": new_quantity}
        requests.put(url, json=payload)


    def create_request(self) -> None:
        """On Update it will send the request to the api to create the product.
        """
        product_name = self.le_1.text().lower()
        quantity = self.sb_quantity.value()
        price = self.sb_price.value()
        content= requests.get(URL + "/product/" + product_name)
        if content.ok:
            self.update_request()
        url = URL + "product"
        payload = {"name": product_name, "price": price, "quantity": quantity}
        requests.post(url, json=payload)


    @qtc.Slot()
    def process_ok(self) -> None:
        """Checks if we are updating or creating and call the request methods for create or update.
        then emit finished event to notify main application we are done and to update the product table.
        then closes the form window.
        """
        if self.update_bool:
            self.update_request()
        else:
            self.create_request()
        self.finished.emit()
        self.close()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Form('apple')
    window.show()
    sys.exit(app.exec())
