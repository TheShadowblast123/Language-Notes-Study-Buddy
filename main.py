import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QStackedWidget
from PyQt5.uic import loadUi  # Import loadUi to load .ui files

temp_data = []
review_queue = [{'concept': 'tengo', 'knowledge': 'I have',"accuracy" : [0, 0]}, {'concept': 'te amo', 'knowledge': 'I love you',"accuracy" : [0, 0]}]
current_reviews = []
groups = []
current_group = []
target = 7
bounds = 2
review_mode = False
def card_completed (new):
    global current_group, review_queue, review_mode
    current_group.append(new)
    review_queue.append(new)
    review_mode = False
    return
def group_completed (new):
    global current_group, review_queue,groups, review_mode
    current_group.append(new)
    
    for item in current_group:
        review_queue.append(item)
    review_queue.insert(0,new)
    for group in groups:
        for item in group:
            review_queue.append(item)
    groups.append(current_group)
    current_group.clear()
    review_mode = True
    print(review_queue)
    return

class FormWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        loadUi('ui/FormWidget.ui', self)
        self.SubmitButton.clicked.connect(self.submit)
        self.GroupButton.clicked.connect(self.group)
        
        self.show()
    def handleRadio(self):
        
        return
    def group(self):
        i_e = self.InputEdit
        k_e = self.KnowledgeEdit
        input_edit_text = i_e.text()
        knowledge_edit_text = k_e.text()
        temp = {"concept" : input_edit_text,
                "knowledge" : knowledge_edit_text,
                "accuracy" : [0, 0]}
        
        temp_data.append(temp)
        group_completed(temp)
        i_e.setText("")
        k_e.setText("")
        self.parent().parent().switchToFlashCard(input_edit_text, knowledge_edit_text)
        self.parent().parent().set_numbers()

        print(groups)
    def submit(self):
        i_e = self.InputEdit
        k_e = self.KnowledgeEdit
        input_edit_text = i_e.text()
        knowledge_edit_text = k_e.text()
        temp = {"concept" : input_edit_text,
                "knowledge" : knowledge_edit_text,
                "accuracy" : [0, 0]}
        
        temp_data.append(temp)
        card_completed(temp)
        i_e.setText("")
        k_e.setText("")
        print(input_edit_text, knowledge_edit_text)
        self.parent().parent().switchToFlashCard(input_edit_text, knowledge_edit_text)
        self.parent().parent().set_numbers()


class BasicFlashCardWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('ui/BasicFlashCardWidget.ui', self)
        self.FailButton.clicked.connect(self.goBack)
        self.PassButton.clicked.connect(self.pass_func)
        self.FlipButton.clicked.connect(self.flip)
        self.unflip()
        self.show()
    def unflip(self):
        self.FailButton.setVisible(False)
        self.AnswerLabel.setVisible(False)
        self.PassButton.setVisible(False)
        self.FlipButton.setVisible(True)
    def flip(self):
        self.FailButton.setVisible(True)
        self.AnswerLabel.setVisible(True)
        self.PassButton.setVisible(True)
        self.FlipButton.setVisible(False)
    def pass_func(self):
        global current_group, review_queue, review_mode
        update = review_queue.pop(-1)
        update["accuracy"][0] += 1
        update["accuracy"][1] += 1
        if update not in current_group and not review_mode:
            current_group.append(update)
            self.parent().parent().set_numbers()
            print("adding to group")
        print(target - len(current_group))
        
        if(len(review_queue) > 0):
            temp = review_queue[-1]
            self.QuestionLabel.setText(temp["concept"])
            self.AnswerLabel.setText(temp["knowledge"])
            self.unflip()
            return
        
        self.goBack()
        return
    def goBack(self):
        self.unflip()
        self.parent().parent().switchToFormWidget()
class TypeFlashCardWidget(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('ui/TypeFlashCardWidget.ui', self)
        self.FailButton.clicked.connect(self.goBack)
        self.PassButton.clicked.connect(self.goBack)

    def goBack(self):
        self.parent().parent().switchToFormWidget()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('ui/MainWindow.ui', self)
        self.stacked_widget = QStackedWidget(self)

        # Create instances of your widgets
        self.form_widget = FormWidget()
        self.basic_flash_card_widget = BasicFlashCardWidget()
        self.type_flash_card_widget = TypeFlashCardWidget()

        # Add widgets to the stacked widget
        self.stacked_widget.addWidget(self.form_widget)
        self.stacked_widget.addWidget(self.basic_flash_card_widget)
        self.stacked_widget.addWidget(self.type_flash_card_widget)

        # Set the initial central widget as the stacked widget
        self.setCentralWidget(self.stacked_widget)
    def set_numbers(self):
        global current_group
        self.form_widget.TargetNumber.setText(str(target - len(current_group)))
        self.form_widget.LowerBoundNumber.setText(str(target - len(current_group) - bounds))
        self.form_widget.UpperBoundNumber.setText(str(target - len(current_group) + bounds))
    def switchToFlashCard(self, question, knowledge):
        # Assuming flash card widget is the second widget in the stacked widget
        _translate = QtCore.QCoreApplication.translate
        self.stacked_widget.setCurrentIndex(1)
        self.basic_flash_card_widget.QuestionLabel.setText(_translate("BasicFlashCardWidget", question))
        self.basic_flash_card_widget.AnswerLabel.setText(_translate("BasicFlashCardWidget", knowledge))

    
    def switchToFormWidget(self):
        self.stacked_widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
