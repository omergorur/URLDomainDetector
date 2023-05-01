# URL Domain Detector

URL Domain Detector is a PyQt6 application that detects the domain names of the URLs entered in a text area and displays them in a table. It also has a function to reset the text area and the table when the clear button is pressed.

![alt url domain detector](https://github.com/omergorur/URLDomainDetector/blob/main/screenshot.png?raw=true)

## Installation

To run this script, you need to have Python 3 and PyQt6 installed on your system. You can install PyQt6 using pip:
```bash
pip install PyQt6
```

You also need to have the tld module installed, which you can do with:
```bash
pip install tld
```

## Usage

To run this script, you need to have three files in the same directory: ```script.py```, ```gui.ui``` and ```tablewidget.py```. The ```script.py``` file contains the main logic of the application, the ```gui.ui``` file contains the user interface design, and the ```tablewidget.py``` file contains a custom table widget class that enables copying the table data to clipboard.

To start the application, run the following command in your terminal:
```bash
python script.py
```
This will open a window with a text area and a table. You can enter one or more URLs in the text area, separated by new lines. Then, click on the submit button to see the domain names of the URLs in the table. You can also sort the table by clicking on the column headers.

If you want to clear the text area and the table, click on the clear button. This will also reset the sorting order of the table.

You can copy the table data to clipboard by selecting rows or columns and pressing Ctrl+C. Then, you can paste the data to Excel or Google Sheets as you wish.

## Purpose
The purpose of this script is to help webmasters and SEO specialists to track and analyze their backlinks from different domains. By using this script, they can easily see which domains are linking to their site and how many links they have from each domain. This can help them to improve their site’s ranking and authority in search engines.

## Credits
This script is also sponsored by [harbiforum.net](https://www.harbiforum.net/), a forum site where you can find interesting topics and discussions.

