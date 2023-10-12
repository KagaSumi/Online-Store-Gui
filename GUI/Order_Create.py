import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Order_Create import Ui_Create_Order_Form
from Alert import Alert
URL = "http://127.0.0.1:5000/api"
class Order_Create_Form(qtw.QWidget, Ui_Create_Order_Form):
    """This class host all functionality for the Create Order UI element.
    """    
    finished = qtc.Signal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.selected_product = None
        self.selected_cart = None
        self.pb_cancel.clicked.connect(self.close)
        self.pb_ok.clicked.connect(self.process_ok)
        self.pb_remove.clicked.connect(self.process_remove)
        self.p_add.clicked.connect(lambda: self.process_add(self.selected_product,self.sb_quantity.value()))
        self.output = {
            "name": None,
            "address": None,
            "products": []
        }
        self.fetch_product_table()

    def update_cart(self) -> None:
        """This is the function to update the new order products to display what we have in our order.
        """
        content = self.output["products"]
        table = self.tv_orderproducts
        if content:
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


    def fetch_product_table(self) -> None:
        """This function will fetch all products from our database through our API. 
        Then populates them and fills out the table, and add select functionality.
        """
        get_url = URL + "/product"
        response = requests.get(get_url)
        content = json.loads(response.text)
        table = self.tv_product
        model = qtg.QStandardItemModel()
        model.setColumnCount(3)
        model.setHorizontalHeaderLabels(['Name', 'Price', 'Quantity'])
        for row_num, row_data in enumerate(content):
            name = qtg.QStandardItem(row_data['name'].title())
            price = qtg.QStandardItem(str(row_data['price']))
            quantity = qtg.QStandardItem(str(row_data['quantity']))
            model.setItem(row_num, 0, name)
            model.setItem(row_num, 1, price)
            model.setItem(row_num, 2, quantity)

        table.setModel(model)
        table.selectionModel().selectionChanged.connect(self.product_changed)
        table.setSelectionBehavior(qtw.QTableView.SelectRows)
        table.resizeColumnsToContents()
        table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)

    def cart_changed(self,selected:qtc.QItemSelection) -> None:
        """This method is called when a product in the order is selected and will update and disable the buttons accordingly.

        Args:
            selected (qtc.QItemSelection): The selected row of the product in the new order.
        """
        try:
            row = selected.indexes()[0].row()
            self.selected_cart = self.tv_orderproducts.model().index(row, 0).data().lower()
            self.p_add.setDisabled(True)
            self.pb_remove.setEnabled(True)
        except IndexError:
            self.selected_product = None
            self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)

    def product_changed(self,selected:qtc.QItemSelection) -> None:
        """This method is called when a product in the product table is selected and will update and disable the buttons accordingly.

        This function will change the maximum the spin box for quantity to the quantity of the product ensuring orders can't order more than instock.

        Args:
            selected (qtc.QItemSelection): The selected row of the product in the new order.
        """
        try:
            row = selected.indexes()[0].row()
            self.selected_product = self.tv_product.model().index(row, 0).data().lower()
            self.sb_quantity.setMaximum(int(self.tv_product.model().index(row, 2).data()))
            if int(self.tv_product.model().index(row, 2).data()):
                self.p_add.setEnabled(True)
            else:
                self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)
        except IndexError:
            self.selected_product = None
            self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)

    def product_changed_cart(self,selected:qtc.QItemSelection) -> None:
        """This is the function to update the selected cart variable with the name of the product selected

        Args:
            selected (qtc.QItemSelection): Selected row of the product table view.
        """
        try:
            row = selected.indexes()[0].row()
            self.selected_cart = self.tv_product.model().index(row, 0).data().lower()
            self.p_add.setEnabled(True)
            self.pb_remove.setEnabled(True)
        except IndexError:
            self.selected_cart = None
            self.p_add.setDisabled(True)
            self.pb_remove.setDisabled(True)


    def raise_alert(self,message:str) -> None:
        """This will raise an alert to tell the user they must finish the form.

        Args:
            message (str): This is the message to be displayed to the user.
        """
        self.alert = Alert(message)
        self.alert.show()


    @qtc.Slot()
    def process_ok(self) -> None:
        """This function will pull the information from the line edits and add it to my output and send the requst to creat the request.
        After it will emit a finished signal to let main application to know that we have sent  the request and the application
        should refresh its table view.
        """
        if self.le_name.text():
            self.output["name"] = self.le_name.text()
            self.output["address"] = self.le_address.text()
            requests.post(f"{URL}/order", json=self.output)
            self.finished.emit()
            self.close()
        else:
            self.raise_alert("Please enter a Name")

    @qtc.Slot()
    def process_add(self,product_name:str ,quantity:int) -> None:
        """This is called when the add button is clicke, this will add the selected product and quantity specified, to our 
        list for our output. 

        Args:
            product_name (str): The name of the selected product.
            quantity (int): This is the quantity value to store of how many of the product we want.
        """        
        is_in_cart = False
        for cart_product in self.output["products"]:
            if cart_product["name"] == product_name:
                is_in_cart = True
        if not is_in_cart:
            self.output["products"].append({"name": product_name.lower(),"quantity": quantity})
        else:
            for cart_product in self.output["products"]:
                if cart_product["name"] == product_name:
                    cart_product["quantity"] = quantity
        self.update_cart()

    @qtc.Slot()
    def process_remove(self) -> None:
        """This removes the selected product from the order product view, from our list.
        Then refreshes the view.
        """        
        self.output["products"] = [product for product in self.output["products"] if product["name"] != self.selected_cart]
        self.update_cart()

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = Order_Create_Form()
    window.show()
    sys.exit(app.exec())
