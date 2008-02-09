# -*- mode: python; coding: utf-8; -*-

import gtk, gtk.gdk as gdk
import gobject
import re

from slog.config import SlogConf
from slog.slengine import SLEngine
from slog.TransPanel import TransView

class Spy:
	def __init__(self):
		self.pattern = re.compile("\W+")
		self.timer = 0;
		self.prev_selection = ""
		self.clipboard = gtk.clipboard_get(gdk.SELECTION_PRIMARY)
		self.sl = SLEngine()
		self.conf = SlogConf()
		self.spy_view = SpyView()

		mod_key = self.conf.get_mod_key()
		self.void_mask = self.__get_modifier_mask() | mod_key

	def __get_modifier_mask(self):
		display = gdk.display_get_default()
		screen, x, y, mask = display.get_pointer()
		mask = mask & ((1<<13)-1)
		return mask

	def __on_clipboard_text_received(self, clipboard, text, data):
		if text is None:
			return
		selection = text.lower().strip()
		if selection == "" or selection == self.prev_selection:
			return
		self.prev_selection = selection

		words = self.pattern.split(selection)
		for word in words:
			if word != "":
				lines = self.sl.get_translate(self.conf.get_spy_dicts(), word)
				translate = "".join(lines)
				self.spy_view.show_translate(word, translate)

	def __on_timer_timeout(self):
		if self.timer == 0:
			return False
		if self.__get_modifier_mask() == self.void_mask:
			self.clipboard.request_text(self.__on_clipboard_text_received)
		else:
			if self.spy_view.get_property("visible"):
				self.spy_view.hide()

		return True

	def start(self):
		self.clipboard.set_text("")
		self.prev_selection = ""
		self.timer = gobject.timeout_add(300, self.__on_timer_timeout)

	def stop(self):
		self.timer = 0


class SpyView(gtk.Window):
	def __init__(self):
		gtk.Window.__init__(self, gtk.WINDOW_POPUP)

		self.set_app_paintable(True)
		self.set_resizable(False)
		self.set_size_request(320, 240)
		self.set_name("gtk-tooltips")
		self.connect("expose_event", self.__on_expose_event)

		self.tv = TransView()
		self.add(self.tv)
		self.tv.show()

	def __on_expose_event(self, window, event):
		w, h = window.size_request()
		window.style.paint_flat_box(window.window, gtk.STATE_NORMAL, gtk.SHADOW_OUT,
									None, window, "tooltip", 0, 0, w, h)
		return False

	def __get_pos(self):
		display = gdk.display_get_default()
		screen, x, y, mask = display.get_pointer()
		return (x+5), (y+5)

	def show_translate(self, word, translate):
		self.tv.set_translate(word, translate)

		x, y = self.__get_pos()
		self.move(x, y)
		self.show()
