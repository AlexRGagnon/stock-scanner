# sidebar.py
"## Sidebar for the stock scanner app.
# This will contain the filter options.

import customTkinter.api as ct

class Sidebar(ct.Frame):
    def __init__(self, master):
        super(__class__, self)
        self.pack_side="top"
        self.width = 2o
        self.background = "#333333"
        # Add filter options here
