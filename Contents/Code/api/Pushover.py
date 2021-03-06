PUSHOVER_API_URL = "https://api.pushover.net/1/messages.json"

TELEGRAM_API_KEY = "ajMtuYCg8KmRQCNZK2ggqaqiBw2UHi"

def setAPI(api):
    global TELEGRAM_API_KEY
    PUSHOVER_API_KEY = api


def send(title, message, user, sound=None):
    data = {'token': TELEGRAM_API_KEY, 'user': user, 'title': title, 'message': message, 'sound': sound}
    try:
        return HTTP.Request(PUSHOVER_API_URL, values=data)
    except Exception as e:
        Log.Debug("Error in send: " + e.message)
        Log.Error(str(traceback.format_exc()))  # raise last error
    return

