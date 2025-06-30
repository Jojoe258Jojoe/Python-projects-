from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox as mb
import datetime
import sqlite3
from tkcalendar import DateEntry

"""In the above snippet of code, we have imported all classes and modules from the
tkinter module to create the GUI window and add widgets to the application. We have
also imported the ttk and messagebox modules from the tkinter module to add ttk
widgets and display any important messages. We have then imported the datetime
module to retrieve the current date and time. We have also imported the sqlite3 module
to maintain a database of the entered entries. At last, we have imported the DateEntry
class of the tkcalendar module to insert the date from the drop-down calendar"""


"""now that we have imported all the necessary modules to the project, it is time to create
the database and define various functions implementing different operations in the
application. These functions include retrieving the data from the database and listing
them in the table, viewing a record from the data table, resetting the entry fields,
removing a selected record from the database, deleting all the records from the
database, adding a new record to the database, updating the details of the pre-existing
record in the database, and displaying the record details in text format.
Let us now understand the implementation of these functions in detail."""

