import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib

class NotificationListener:
    def __init__(self, callback):
        self.callback = callback
        DBusGMainLoop(set_as_default=True)
        try:
            self.bus = dbus.SessionBus()
            self.bus.add_match_string_member("Notify", "org.freedesktop.Notifications")
            self.bus.add_message_filter(self.handler)
        except Exception as e:
            print(f"Błąd DBus: {e}")

    def handler(self, bus, message):
        args = message.get_args_list()
        if len(args) > 3:
            title = str(args[3])  # Zazwyczaj nadawca
            body = str(args[4])   # Treść
            # Filtrujemy powiadomienia (Discord w przeglądarce często ma 'Discord' w tytule lub treści)
            if "discord" in title.lower() or "discord" in body.lower():
                self.callback(title)

    def start(self):
        loop = GLib.MainLoop()
        loop.run()