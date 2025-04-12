from PySide6.QtWidgets import (QApplication, QMainWindow, 
                              QPushButton, QLabel, QVBoxLayout, QWidget)
from PySide6.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("PySide6 Example")
        self.setGeometry(100, 100, 300, 200)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        
        # Create widgets
        self.label = QLabel("Click to ibrahim")
        self.button = QPushButton("Ibrahim")
        
        # Add widgets to layout
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        # Connect signal to slot
        self.button.clicked.connect(self.on_button_clicked)
    
    @Slot()
    def on_button_clicked(self):
        """Slot that handles button clicks"""
        self.label.setText("Button was clicked!")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()