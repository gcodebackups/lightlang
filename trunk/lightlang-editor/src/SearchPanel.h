#ifndef SEARCHPANEL_H
#define SEARCHPANEL_H

#include <QtGui/QWidget>

class QTimer;
class QLabel;
class QLineEdit;
class QToolButton;
class QListWidget;
class QKeyEvent;
class DatabaseCenter;
class QSpinBox;
class InfoButton;
class PopupWindow;
class QListWidgetItem;

class SearchPanel : public QWidget
{
	Q_OBJECT
	signals:
		void closed();
		void wordChosen(const QString&);
	public slots:
		void showWithRolling();
		void hideWithRolling();
	public:
		SearchPanel(DatabaseCenter *databaseCenter);
		~SearchPanel();
		
		void setFocusAtLineEdit();
		void saveSettings();
	private slots:
		void updateSize();
		void textChanged(const QString& text);
		void search();
		void emitSignalToEditTheWord(QListWidgetItem *item);
	private:
		QTimer *timer;
		bool rollingToShow;
		
		DatabaseCenter *databaseCenter;
		
		QLabel *titleLabel;
		QLabel *warningLabel;
		
		QLineEdit *lineEdit;
		
		QToolButton *clearLineButton;
		QToolButton *closeButton;
		QToolButton *searchButton;
		
		QListWidget *listWidget;
		QSpinBox *limitSpinBox;
		
		PopupWindow *popupWindow;
		InfoButton *infoButton;
	protected:
		void keyPressEvent(QKeyEvent *);
};

#endif
