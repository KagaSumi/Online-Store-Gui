import sys, requests, json
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application.UI.ui_Main import Ui_Main
from Product_Form import Form
from Order_Create import Order_Create_Form
from Order_Edit import Order_Edit_Form
URL = "http://127.0.0.1:5000/api/"

class Main(qtw.QMainWindow, Ui_Main):
    """This is defining our main application that will tie all the other ui elements together.
    It has functions to populate all information and handle the logic for any restrictions for the UI I had.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #Initialize variables
        self.selected_product = None
        self.order_list = json.loads(requests.get(URL + "/order").text)
        self.selected_order_id = None
        self.selected_order_products = None
        self.order_process_sort = None

        #Tie function calls to button clicked or clicked functionality
        self.pb_create.clicked.connect(self.process_form)
        self.pb_update.clicked.connect(lambda: self.process_form(self.selected_product))
        self.pb_delete.clicked.connect(self.process_delete_product)
        self.pb_order_create.clicked.connect(self.process_create_order)
        self.cb_out_of_stock.clicked.connect(self.update_product)
        self.pb_order_delete.clicked.connect(self.process_delete_order)
        self.pb_order_process.clicked.connect(self.process_process_order)
        self.pb_order_update.clicked.connect(self.process_update_order)
        self.rb_order_no_filter.clicked.connect(self.order_no_filter)
        self.rb_order_unprocessed.clicked.connect(self.order_unprocessed_filter)
        self.rb_order_processed.clicked.connect(self.order_processed_filter)
        self.le_order_filter.textChanged.connect(self.update_order)

        #Run Fetch Tables to populate on launch
        self.update_product()
        self.update_order()

    def update_product(self):
        """Loads variables to fetch the table from.
        """
        content = json.loads(requests.get(URL + "/product").text)
        if self.cb_out_of_stock.isChecked():
            content = [item for item in content if item["quantity"] == 0]
        self.fetch_table(content,self.tv_product_list,['Name', 'Price', 'Quantity'])
        self.tv_product_list.selectionModel().selectionChanged.connect(self.product_changed)

    def fetch_table(self, content:list[dict], table:qtw.QTableView, headers:list[str]) -> None:
        """This function will update the table with the content under the headers

        Args:
            content (dict): This a list of dictionaries containing the data to display.
            table (qtw.QTableView): This is the table to display the data.
            headers (list[*str]): This is a list of strings holding the headers to display.
            
        """
        model = qtg.QStandardItemModel(len(content), len(headers))
        model.setHorizontalHeaderLabels(headers)
        for row_num, row_data in enumerate(content):
            for col_num, col_data in enumerate(row_data.values()):
                model.setItem(row_num, col_num, qtg.QStandardItem(str(col_data)))
        table.setModel(model)
        table.resizeColumnsToContents()
        table.setSelectionBehavior(qtw.QTableView.SelectRows)
        table.setEditTriggers(qtw.QAbstractItemView.NoEditTriggers)
        table.setSelectionMode(qtw.QAbstractItemView.SingleSelection)

    def update_order(self) -> None:
        """This function much like update_products will update the order table with the order list.
        """
        self.order_list = json.loads(requests.get(URL + "/order").text)
        unfilter_content = self.order_list
        if self.order_process_sort == True:
            unfilter_content = sorted([order for order in unfilter_content if order["completed"]], key=lambda x: (x["time_processed"], x["time_created"]))
        elif self.order_process_sort == False:
            unfilter_content = sorted([order for order in unfilter_content if not order["completed"]], key=lambda x: x["time_created"])
        if self.le_order_filter.text():
            unfilter_content = [order for order in unfilter_content if self.le_order_filter.text().lower() in order["customer_name"].lower()]
        content = [{"order_id": order["id"],
                    "name": order["customer_name"], 
                    "address": order["customer_address"], 
                    "time_created": order["time_created"],
                    "time_processed": order["time_processed"]}
                   for order in unfilter_content]
        self.fetch_table(content,self.tv_order_view,['Order_ID', 'Name', 'Address','Time Created', 'Time Processed'])
        self.tv_order_view.selectionModel().selectionChanged.connect(self.order_changed)

    def product_changed(self,selected:qtc.QItemSelection):
        """This function is called when there is a selection change in product table.
        This will change the local vairable to update to the name of product selected.
        If there is a selected product it will update the button states so that user can select
        Update and Delete
        
        Otherwise it will Disable those buttons.

        Args:
            selected (QItemSelection): This is the row we selected from the table. 
        """
        try:
            row = selected.indexes()[0].row()
            self.selected_product = self.tv_product_list.model().index(row, 0).data().lower()
            self.pb_delete.setEnabled(True)
            self.pb_update.setEnabled(True)
        except IndexError:
            self.selected_product = None
            self.pb_delete.setDisabled(True)
            self.pb_update.setDisabled(True)

    def order_changed(self,selected:qtc.QItemSelection) -> None:
        """This function is called when the order selected has changed.
        This function handles enabling and disabling the buttons on the order section.
        This will also update our stored order id to for our other button to use.
        
        If an order is selected it will call the fetch_order_product_table function
        which populates the adjacent table view with the items in the order selected.

        Args:
            selected (QItemSelection): Selected row for the order selected
        """
        try:
            row = selected.indexes()[0].row()
            self.selected_order_id = int(self.tv_order_view.model().index(row, 0).data())
            self.pb_order_delete.setEnabled(True)
            self.pb_order_update.setEnabled(True)
            self.pb_order_process.setEnabled(True)
            self.fetch_order_product_table()
        except IndexError:
            self.selected_order_products = None
            self.selected_order_id = None
            self.pb_order_delete.setDisabled(True)
            self.pb_order_update.setDisabled(True)
            self.pb_order_process.setDisabled(True)
            self.tv_order_items.setModel(None)

    def fetch_order_product_table(self) -> None:
        """This will fetch all the products for the selected order.
        """
        for order in self.order_list:
            if order["id"] == self.selected_order_id:
                self.fetch_table(order["products"],self.tv_order_items,['Name','Quantity'])

# ----------------------------------------------------------------
# ----------------- Button Functionality--------------------------
# ----------------------------------------------------------------
    @qtc.Slot()
    def process_form(self, product = None) -> None:
        """
        Opens a form for creating or editing a product and connects its finished signal to the fetch_product_table method.
        
        If product_name is None then it is assumed that we are creating a new product
        If product_name is not None then it is assumed that passed is a name of the product
        Args:
            product_name (str or None): The name of the product to edit, or None to create a new product.
        
        Returns:
            None
        """
        if product:
            self.product_form = Form(self.selected_product)
        else:
            self.product_form = Form()
        self.product_form.finished.connect(self.update_product)
        self.product_form.show()

    @qtc.Slot()
    def process_delete_product(self) -> None:
        """
        Deletes a product from the database by sending a DELETE request to the API.
        
        Args:
            product_name (str): The name of the product to be deleted.
        
        Returns:
            None
        """
        delete_url = URL + "/product/" + self.selected_product
        requests.delete(delete_url)
        self.selected_product=None
        self.fetch_product_table()

    @qtc.Slot()
    def process_create_order(self) -> None:
        """
        Opens a new order creation form and connects its finished signal to the update_order_table method.
        
        Returns:
            None
        """
        self.order_create_form = Order_Create_Form()
        self.order_create_form.finished.connect(self.update_order)
        self.order_create_form.show()

    @qtc.Slot()
    def process_delete_order(self) -> None:
        """
    Deletes the selected order from the database by sending a DELETE request to the API.
    Disables the delete, process, and update buttons, updates the order table, and clears the item list.
    
    Returns:
        None
        """
        requests.delete(URL + "/order/" + str(self.selected_order_id))
        self.selected_product=None
        self.pb_order_delete.setDisabled(True)
        self.pb_order_process.setDisabled(True)
        self.pb_order_update.setDisabled(True)
        self.update_order()
        self.tv_order_items.setModel(None)

    @qtc.Slot()
    def process_update_order(self) -> None:
        """
    Opens an order editing form for the selected order and connects its finished signal to the update_order_table method.
    Clears the item list.
    
    Returns:
        None
        """
        self.order_update_form = Order_Edit_Form(self.selected_order_id)
        self.order_update_form.finished.connect(self.update_order)
        self.tv_order_items.setModel(None)
        self.order_update_form.show()

    @qtc.Slot()
    def process_process_order(self) -> None:
        """
    Marks the selected order as processed by sending a PUT request to the API.
    Fetches the product table and updates the order table.
    
    Returns:
        None
        """
        requests.put(URL +'/order/' + str(self.selected_order_id), json={"process": True})
        self.update_order()

    @qtc.Slot()
    def order_no_filter(self) -> None:
        """
    Resets the order process sort filter to None and updates the order table.
    
    Returns:
        None
        """
        self.order_process_sort = None
        self.update_order()

    @qtc.Slot()
    def order_processed_filter(self) -> None:
        """
    Sets the order process sort filter to True (processed orders only) and updates the order table.
    
    Returns:
        None
        """
        self.order_process_sort = True
        self.update_order()

    @qtc.Slot()
    def order_unprocessed_filter(self) -> None:
        """
        Sets the order process sort filter to False (unprocessed orders only) and updates the order table.
        
        Returns:
            None
        """
        self.order_process_sort = False
        self.update_order()

if __name__ == "__main__":
    app = qtw.QApplication()
    main_window = Main()
    main_window.show()
    sys.exit(app.exec())
