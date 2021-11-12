#install package: pip install win10toast
from win10toast import ToastNotifier  #win10toast used to create desktop notifications
toast=ToastNotifier()  #creating an object to ToastNotifier class
#creating a notification
toast.show_toast("testing notification","Hey! my notification is up",icon_path=None,duration=15)