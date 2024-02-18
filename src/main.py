"""
Authors : Charbel Salhab, Theo Eloy, Adam Yahia Abdchafee
DataFilter Project
Fevrier 2024
"""

from gui.root import App
from gui.menu import AppMenu
from upload import upload_file
from stats import find_average
from stats import find_percentage
from stats import find_min_list
from stats import find_max_list
from stats import find_average_list
from stats import find_min

if __name__ == "__main__":
    app = App()
    app.menu = AppMenu(app)
    app.mainloop()
