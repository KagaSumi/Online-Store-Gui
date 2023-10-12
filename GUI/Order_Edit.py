import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Order_Edit import Ui_Edit_Order_Form

class Order_Edit_Form(qtw.QWidget, Ui_Edit_Order_Form):
    """This host all the functions for the functionality of the Edit Order UI element.
    """
    finished = qtc.Signal()
    def __init__(self,order_id):
        super().__init__()
        self.setupUi(self)
        self.url = f"http://127.0.0.1:5000/api/order/{order_id}"
        self.selected = None
        self.order_id = order_id
        self.content = json.loads(requests.get(self.url).text)
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_ok)
        self.le_name.setText(self.content.get('customer_name'))
        self.le_address.setText(self.content.get('customer_address'))
        self.pb_update.clicked.connect(lambda: self.process_update(self.selected,self.sb_quantity.value()))
        self.pb_ok.clicked.connect(self.process_ok)
        self.pb_remove.clicked.connect(self.process_remove)
        self.output = self.content["products"]
        self.fetch_table()

    def fetch_table(self) -> None:
        """This function will populate the table view with current state of the products in our order.
        """
        content = self.output
        table = self.tv_product
        if content != []:
            model = qtg.QStandardItemModel()
            model.setColumnCount(2)
            model.setHorizontalHeaderLabels(['Name', 'Quantity'])
            for row_num, row_data in enumerate(content):
                name = qtg.QStandardItem(row_data['name'].title())
                quantity = qtg.QStandardItem(str(row_data['quantity']))
                model.setItem(row_num, 0, name)
                model.setItem(row_num, 1, quantity)

            table.setModel(model)
            table.selectionModel().selectionChanged.connect(self.cart_changed)
            table.setSelectionBehavior(qtw.QTableView.SelectRows)
            table.resizeColumnsToContents()
            table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
            table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)
        else:
            table.setModel(None)

    def cart_changed(self,selected:qtc.QItemSelection) -> None:
        """This function will run when a new row is selected on the order product view

        Args:
            selected (qtc.QItemSelection): This is the selected row from the order product view.
        """
        try:
            row = selected.indexes()[0].row()
            self.selected = self.tv_product.model().index(row, 0).data().lower()
            self.sb_quantity.setValue(int(self.tv_product.model().index(row,1).data()))
            self.pb_update.setEnabled(True)
            self.pb_remove.setEnabled(True)
        except IndexError:
            self.selected = None
            self.pb_update.setDisabled(True)
            self.pb_remove.setDisabled(True)

    @qtc.Slot()
    def process_ok(self) -> None:
        """The is sending the request to the server with our new product list.
        After it will emit a finished signal so that the main application can refresh their order list.
        """
        requests.post(self.url, json={"products": self.output})
        self.finished.emit()
        self.close()

    @qtc.Slot()
    def process_remove(self) -> None:
        """The function will remove the selected product from our list.
        Then refresh table view.
        """
        self.output = [product for product in self.output if product["name"] != self.selected]
        self.fetch_table()

    @qtc.Slot()
    def process_update(self, product:str, quantity:int) -> None:
        """This will go over the order's product list and change the quantity to match the quantity value.

        Args:
            product (str): Name of the product
            quantity (int): Value of the quantity
        """
        for cart_product in self.output:
            if cart_product["name"] == product:
                cart_product["quantity"] = quantity
        self.fetch_table()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Order_Edit_Form(1)
    window.show()
    sys.exit(app.exec())
