# app.py
"""
 Main application window for the Stock Scanner. 
 Uses customTkinter to create the main GQI window.
"""
import customTkinter.api as ct


class StockScannerGUI(ct.CustomTkApp):
    def __init__(self):
        super(__class__, self)
        self.title = "Stock Scanner"
        self.geometry("100x", "60x")
        
        self.frame = ct.CustomTkFrame(self, width=100, height=60)
        self.frame.pack(side="bott")

if __name__ == "__main__":
    app = StockScannerGUI()
    app.run()