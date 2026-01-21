from PySide6.QtCore import QEvent
from PySide6.QtGui import Qt, QStandardItem
from PySide6.QtWidgets import QComboBox, QStyledItemDelegate


class CheckableComboBox(QComboBox):

    # Subclass Delegate to increase item height
    class Delegate(QStyledItemDelegate):
        def sizeHint(self, option, index):
            size = super().sizeHint(option, index)
            size.setHeight(20)
            return size

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # Set the minimum size and style for the QComboBox
        self.setMinimumSize(0, 30)
        self.setStyleSheet("""color: black; background-color: white;""")

        # Make the combo editable to set a custom text, but readonly
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.lineEdit().setText('')

        # Use a custom delegate to increase item height in the popup
        self.setItemDelegate(CheckableComboBox.Delegate())

        # Update the text when an item is toggled
        self.model().dataChanged.connect(self.update_text)

        # Hide and show popup when clicking the line edit
        self.lineEdit().installEventFilter(self)
        self.close_on_line_edit_click = False

        # Prevent popup from closing when clicking on an item
        self.view().viewport().installEventFilter(self)

    def eventFilter(self, widget, event):
        # Handle clicks on the line edit to show/hide the popup
        if widget == self.lineEdit():
            if event.type() == QEvent.MouseButtonRelease:
                if not self.isEnabled():
                    return True
                if self.close_on_line_edit_click:
                    self.hidePopup()
                else:
                    self.showPopup()
            return super().eventFilter(widget, event)

        if widget == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                if not self.isEnabled():
                    return True

                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                # HEADER: não fecha, não faz nada
                if not (item.flags() & Qt.ItemIsUserCheckable):
                    return True  # consome o evento completamente

                # ITEM NORMAL
                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)

                return True

        # Handle clicks on the viewport to toggle item check state
        if widget == self.view().viewport():
            if event.type() == QEvent.MouseButtonRelease:
                if not self.isEnabled():
                    return True

                index = self.view().indexAt(event.pos())
                item = self.model().item(index.row())

                if item.checkState() == Qt.Checked:
                    item.setCheckState(Qt.Unchecked)
                else:
                    item.setCheckState(Qt.Checked)
                return True
            return super().eventFilter(widget, event)

    def update_text(self):
        text_container = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.Checked:
                text_container.append(self.model().item(i).text())
        text_str = ', '.join(text_container)
        self.lineEdit().setText(text_str)

    def addItems(self, items, itemList=None):
        for index, text in enumerate(items):
            try:
                data = itemList[index]
            except (TypeError, IndexError):
                data = None
            self.addItem(text, data)

    def addItem(self, text, userData=None):
        item = QStandardItem()
        item.setText(text)
        if userData is not None:
            item.setData(userData, Qt.UserRole)

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        item.setData(Qt.Unchecked, Qt.CheckStateRole)
        self.model().appendRow(item)

    def get_selected_texts(self):
        selected_texts = []
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if item and item.checkState() == Qt.Checked:
                selected_texts.append(item.text())
        return selected_texts

    def get_selected_indexes(self):
        selected_indexes = []
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if item and item.checkState() == Qt.Checked:
                selected_indexes.append(row)
        return selected_indexes

    def set_current_texts(self, text, checked=True):
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if item.text() == text:
                state = Qt.Checked if checked else Qt.Unchecked
                item.setCheckState(state)
                self.update_text()
                return True
        return False

    def set_current_indexes(self, indexes):
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if row in indexes:
                item.setCheckState(Qt.Checked)
            else:
                item.setCheckState(Qt.Unchecked)
        self.update_text()

    def showPopup(self):
        super().showPopup()
        # When the popup is displayed, a click on the lineedit should close it
        self.close_on_line_edit_click = True

    def hidePopup(self):
        super().hidePopup()
        # Used to prevent immediate reopening when clicking on the lineEdit
        self.startTimer(100)
        # Refresh the display text when closing
        self.update_text()

    def timerEvent(self, event):
        # After timeout, kill timer, and re-enable click on lineEdit
        self.killTimer(event.timerId())
        self.close_on_line_edit_click = False

    def addTitle(self, text):
        item = QStandardItem(text)
        item.setFlags(Qt.ItemIsEnabled)
        item.setData(None)
        font = item.font()
        font.setBold(True)
        item.setFont(font)
        item.setForeground(Qt.gray)
        self.model().appendRow(item)

    def disable_by_user_data(self, value):
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if item.data(Qt.UserRole) == value:
                self._set_item_disabled_style(item)
                return True
        return False

    def disable_by_index(self, index):
        item = self.model().item(index)
        if not item:
            return False
        self._set_item_disabled_style(item)
        return True

    def enable_by_user_data(self, value):
        for row in range(self.model().rowCount()):
            item = self.model().item(row)
            if item.data(Qt.UserRole) == value:
                self._set_item_enabled_style(item)
                return True
        return False

    def enable_by_index(self, index):
        item = self.model().item(index)
        if not item:
            return False
        self._set_item_enabled_style(item)
        return True

    def _set_item_disabled_style(self, item):
        item.setFlags(Qt.ItemIsEnabled)  # sem check

        item.setForeground(Qt.darkGray)

        font = item.font()
        font.setItalic(True)
        item.setFont(font)

        item.setBackground(Qt.lightGray)

    def _set_item_enabled_style(self, item):
        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)

        item.setForeground(Qt.black)

        font = item.font()
        font.setItalic(False)
        item.setFont(font)

        item.setBackground(Qt.white)


