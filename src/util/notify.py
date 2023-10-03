from plyer import notification




#code copied and official plyer docs
# https://python.plainenglish.io/how-to-send-desktop-notifications-with-python-62a738850fbf


def showNotify(title,message):
    notification.notify(
    title = title,
    message = message,
    app_icon =None,
    timeout = 10,
)