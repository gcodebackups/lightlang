# -*- coding: utf8 -*-
#
# XSL - graphical interface for SL
# Copyright (C) 2007-2016 Devaev Maxim
#
# This file is part of XSL.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import Qt
import Config
import Const


#####
MyIcon = Config.Prefix+"/lib/xsl/icons/xsl_16.png"
IconsDir = Config.Prefix+"/lib/xsl/icons/"


#####
def tr(str) :
	return Qt.QApplication.translate("@default", str)


#####
class AboutWindow(Qt.QDialog) :
	def __init__(self, parent = None) :
		Qt.QDialog.__init__(self, parent)

		self.setModal(True)

		self.setWindowTitle(tr("About %1").arg(Const.MyName))
		self.setWindowIcon(Qt.QIcon(MyIcon))

		#####

		self.main_layout = Qt.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.info_label_layout = Qt.QHBoxLayout()
		self.main_layout.addLayout(self.info_label_layout)

		self.ok_button_layout = Qt.QHBoxLayout()
		self.ok_button_layout.setAlignment(Qt.Qt.AlignRight)
		self.main_layout.addLayout(self.ok_button_layout)

		#####

		self.icon_label = Qt.QLabel()
		self.icon_label.setAlignment(Qt.Qt.AlignTop)
		self.icon_label.setPixmap(Qt.QPixmap(IconsDir+"xsl_64.png"))
		self.info_label_layout.addWidget(self.icon_label)

		self.text_label = Qt.QLabel(tr("<h3>%1 - the graphical interface for SL</h3>"
			"All the programs of the <strong>%2</strong> package are distributable, according<br>"
			"to the license <strong>GPLv2</strong>. For details visit <em>License agreement</em> of the<br>"
			"<strong>%2</strong> manual.<br>"
			"<br>"
			"Author of the <strong>%2</strong> package:<br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Devaev Maxim</em><br>"
			"Thanks to:<br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Baburina Elisabeth</em><br>"
			"Valuable assistants:<br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Vladimir Fomkin</em><br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Tihonov Sergey</em><br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Renat Nasyrov</em><br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Du Vinh</em><br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Aleksey Yum</em><br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Olga Polyakova</em><br>"
			"Translators:<br>"
			"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<em>Kirill Nebogin</em><br>"
			"<br>"
			"<em>Copyright &copy; 2007-2016 Devaev Maxim (<a href=\"mailto:%3?subject=%2\">%3</a>)</em>")
				.arg(Const.MyName).arg(Const.Organization).arg(Const.DeveloperMail))
		self.text_label.setOpenExternalLinks(True)
		self.info_label_layout.addWidget(self.text_label)

		self.ok_button = Qt.QPushButton(tr("&OK"))
		self.ok_button.setDefault(True)
		self.ok_button_layout.addWidget(self.ok_button)

		#####

		self.connect(self.ok_button, Qt.SIGNAL("clicked()"), self.accept)


	### Public ###

	def show(self) :
		Qt.QDialog.show(self)
		self.raise_()
		self.activateWindow()
