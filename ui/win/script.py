# Form implementation generated from reading ui file 'script.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(795, 526)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.close_mission_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.close_mission_btn.setGeometry(QtCore.QRect(700, 280, 81, 21))
        self.close_mission_btn.setObjectName("close_mission_btn")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 80, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 480, 91, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 591, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.richangTab1 = QtWidgets.QWidget()
        self.richangTab1.setObjectName("richangTab1")
        self.baotu_btn = QtWidgets.QPushButton(parent=self.richangTab1)
        self.baotu_btn.setGeometry(QtCore.QRect(40, 60, 75, 23))
        self.baotu_btn.setObjectName("baotu_btn")
        self.mijing_btn = QtWidgets.QPushButton(parent=self.richangTab1)
        self.mijing_btn.setGeometry(QtCore.QRect(40, 100, 75, 23))
        self.mijing_btn.setObjectName("mijing_btn")
        self.dati_btn = QtWidgets.QPushButton(parent=self.richangTab1)
        self.dati_btn.setGeometry(QtCore.QRect(40, 140, 75, 23))
        self.dati_btn.setObjectName("dati_btn")
        self.yabiao_btn = QtWidgets.QPushButton(parent=self.richangTab1)
        self.yabiao_btn.setGeometry(QtCore.QRect(40, 180, 75, 23))
        self.yabiao_btn.setObjectName("yabiao_btn")
        self.batch_richang = QtWidgets.QPushButton(parent=self.richangTab1)
        self.batch_richang.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.batch_richang.setObjectName("batch_richang")
        self.line = QtWidgets.QFrame(parent=self.richangTab1)
        self.line.setGeometry(QtCore.QRect(0, 40, 31, 191))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.baotu_chk = QtWidgets.QCheckBox(parent=self.richangTab1)
        self.baotu_chk.setGeometry(QtCore.QRect(20, 60, 21, 16))
        self.baotu_chk.setText("")
        self.baotu_chk.setChecked(True)
        self.baotu_chk.setObjectName("baotu_chk")
        self.mijing_chk = QtWidgets.QCheckBox(parent=self.richangTab1)
        self.mijing_chk.setGeometry(QtCore.QRect(20, 100, 21, 16))
        self.mijing_chk.setText("")
        self.mijing_chk.setChecked(True)
        self.mijing_chk.setObjectName("mijing_chk")
        self.dati_chk = QtWidgets.QCheckBox(parent=self.richangTab1)
        self.dati_chk.setGeometry(QtCore.QRect(20, 140, 21, 16))
        self.dati_chk.setText("")
        self.dati_chk.setChecked(True)
        self.dati_chk.setObjectName("dati_chk")
        self.yabiao_chk = QtWidgets.QCheckBox(parent=self.richangTab1)
        self.yabiao_chk.setGeometry(QtCore.QRect(20, 180, 21, 16))
        self.yabiao_chk.setText("")
        self.yabiao_chk.setChecked(True)
        self.yabiao_chk.setObjectName("yabiao_chk")
        self.baotu_cfg_btn = QtWidgets.QToolButton(parent=self.richangTab1)
        self.baotu_cfg_btn.setGeometry(QtCore.QRect(120, 60, 37, 18))
        self.baotu_cfg_btn.setObjectName("baotu_cfg_btn")
        self.yabiao_txt = QtWidgets.QLabel(parent=self.richangTab1)
        self.yabiao_txt.setGeometry(QtCore.QRect(133, 182, 151, 21))
        self.yabiao_txt.setObjectName("yabiao_txt")
        self.missionrichang_shutdown_chk = QtWidgets.QCheckBox(parent=self.richangTab1)
        self.missionrichang_shutdown_chk.setGeometry(QtCore.QRect(20, 220, 111, 16))
        self.missionrichang_shutdown_chk.setObjectName("missionrichang_shutdown_chk")
        self.tabWidget.addTab(self.richangTab1, "")
        self.richangTab2 = QtWidgets.QWidget()
        self.richangTab2.setObjectName("richangTab2")
        self.line_2 = QtWidgets.QFrame(parent=self.richangTab2)
        self.line_2.setGeometry(QtCore.QRect(0, 40, 31, 301))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.norm70_chk = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.norm70_chk.setGeometry(QtCore.QRect(20, 153, 21, 16))
        self.norm70_chk.setText("")
        self.norm70_chk.setChecked(True)
        self.norm70_chk.setObjectName("norm70_chk")
        self.batch_mission520 = QtWidgets.QPushButton(parent=self.richangTab2)
        self.batch_mission520.setGeometry(QtCore.QRect(10, 10, 111, 31))
        self.batch_mission520.setObjectName("batch_mission520")
        self.fuben_norm70_btn = QtWidgets.QPushButton(parent=self.richangTab2)
        self.fuben_norm70_btn.setGeometry(QtCore.QRect(40, 153, 75, 23))
        self.fuben_norm70_btn.setObjectName("fuben_norm70_btn")
        self.label_4 = QtWidgets.QLabel(parent=self.richangTab2)
        self.label_4.setGeometry(QtCore.QRect(130, 40, 241, 31))
        self.label_4.setObjectName("label_4")
        self.norm50_chk2 = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.norm50_chk2.setGeometry(QtCore.QRect(20, 193, 21, 16))
        self.norm50_chk2.setText("")
        self.norm50_chk2.setChecked(True)
        self.norm50_chk2.setAutoRepeat(True)
        self.norm50_chk2.setObjectName("norm50_chk2")
        self.xiashi70_chk = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.xiashi70_chk.setGeometry(QtCore.QRect(20, 73, 21, 16))
        self.xiashi70_chk.setText("")
        self.xiashi70_chk.setObjectName("xiashi70_chk")
        self.xiashi50_chk = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.xiashi50_chk.setGeometry(QtCore.QRect(20, 113, 21, 16))
        self.xiashi50_chk.setText("")
        self.xiashi50_chk.setChecked(True)
        self.xiashi50_chk.setObjectName("xiashi50_chk")
        self.fuben_xiashi70_btn = QtWidgets.QPushButton(parent=self.richangTab2)
        self.fuben_xiashi70_btn.setGeometry(QtCore.QRect(40, 73, 75, 23))
        self.fuben_xiashi70_btn.setObjectName("fuben_xiashi70_btn")
        self.fuben_xiashi50_btn = QtWidgets.QPushButton(parent=self.richangTab2)
        self.fuben_xiashi50_btn.setGeometry(QtCore.QRect(40, 113, 75, 23))
        self.fuben_xiashi50_btn.setObjectName("fuben_xiashi50_btn")
        self.fuben_norm50_btn2 = QtWidgets.QPushButton(parent=self.richangTab2)
        self.fuben_norm50_btn2.setGeometry(QtCore.QRect(40, 193, 75, 23))
        self.fuben_norm50_btn2.setObjectName("fuben_norm50_btn2")
        self.norm50_chk1 = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.norm50_chk1.setGeometry(QtCore.QRect(20, 233, 21, 16))
        self.norm50_chk1.setText("")
        self.norm50_chk1.setChecked(True)
        self.norm50_chk1.setObjectName("norm50_chk1")
        self.fuben_norm50_btn1 = QtWidgets.QPushButton(parent=self.richangTab2)
        self.fuben_norm50_btn1.setGeometry(QtCore.QRect(40, 233, 75, 23))
        self.fuben_norm50_btn1.setObjectName("fuben_norm50_btn1")
        self.ghost_chk = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.ghost_chk.setGeometry(QtCore.QRect(20, 293, 21, 16))
        self.ghost_chk.setText("")
        self.ghost_chk.setChecked(True)
        self.ghost_chk.setObjectName("ghost_chk")
        self.label_7 = QtWidgets.QLabel(parent=self.richangTab2)
        self.label_7.setGeometry(QtCore.QRect(20, 273, 54, 12))
        self.label_7.setObjectName("label_7")
        self.mission520_shutdown_chk = QtWidgets.QCheckBox(parent=self.richangTab2)
        self.mission520_shutdown_chk.setGeometry(QtCore.QRect(20, 333, 111, 16))
        self.mission520_shutdown_chk.setObjectName("mission520_shutdown_chk")
        self.label_8 = QtWidgets.QLabel(parent=self.richangTab2)
        self.label_8.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.richangTab2)
        self.label_9.setGeometry(QtCore.QRect(130, 70, 311, 31))
        self.label_9.setObjectName("label_9")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.richangTab2)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 290, 451, 41))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.ghost_2_rdo = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.ghost_2_rdo.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.ghost_2_rdo.setText("")
        self.ghost_2_rdo.setChecked(True)
        self.ghost_2_rdo.setObjectName("ghost_2_rdo")
        self.ghost_btn = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.ghost_btn.setGeometry(QtCore.QRect(300, 10, 41, 21))
        self.ghost_btn.setObjectName("ghost_btn")
        self.ghost5_btn = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.ghost5_btn.setGeometry(QtCore.QRect(140, 10, 75, 23))
        self.ghost5_btn.setObjectName("ghost5_btn")
        self.ghost_ipt = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.ghost_ipt.setGeometry(QtCore.QRect(250, 10, 51, 21))
        self.ghost_ipt.setMaxLength(2)
        self.ghost_ipt.setObjectName("ghost_ipt")
        self.ghost2_btn = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.ghost2_btn.setGeometry(QtCore.QRect(30, 10, 75, 23))
        self.ghost2_btn.setObjectName("ghost2_btn")
        self.ghost_5_rdo = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.ghost_5_rdo.setGeometry(QtCore.QRect(120, 10, 16, 16))
        self.ghost_5_rdo.setText("")
        self.ghost_5_rdo.setObjectName("ghost_5_rdo")
        self.ghost_cfg_btn = QtWidgets.QToolButton(parent=self.groupBox_3)
        self.ghost_cfg_btn.setGeometry(QtCore.QRect(360, 10, 37, 18))
        self.ghost_cfg_btn.setObjectName("ghost_cfg_btn")
        self.ghost_rdo = QtWidgets.QRadioButton(parent=self.groupBox_3)
        self.ghost_rdo.setGeometry(QtCore.QRect(230, 10, 16, 16))
        self.ghost_rdo.setText("")
        self.ghost_rdo.setObjectName("ghost_rdo")
        self.tabWidget.addTab(self.richangTab2, "")
        self.zhouchangTab = QtWidgets.QWidget()
        self.zhouchangTab.setObjectName("zhouchangTab")
        self.menpai_cfg_btn = QtWidgets.QToolButton(parent=self.zhouchangTab)
        self.menpai_cfg_btn.setGeometry(QtCore.QRect(100, 20, 37, 18))
        self.menpai_cfg_btn.setObjectName("menpai_cfg_btn")
        self.mihunta_btn = QtWidgets.QPushButton(parent=self.zhouchangTab)
        self.mihunta_btn.setGeometry(QtCore.QRect(20, 100, 75, 23))
        self.mihunta_btn.setObjectName("mihunta_btn")
        self.menpai_btn = QtWidgets.QPushButton(parent=self.zhouchangTab)
        self.menpai_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.menpai_btn.setObjectName("menpai_btn")
        self.haidi_btn = QtWidgets.QPushButton(parent=self.zhouchangTab)
        self.haidi_btn.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.haidi_btn.setObjectName("haidi_btn")
        self.mihunta_cfg_btn = QtWidgets.QToolButton(parent=self.zhouchangTab)
        self.mihunta_cfg_btn.setGeometry(QtCore.QRect(100, 100, 37, 18))
        self.mihunta_cfg_btn.setObjectName("mihunta_cfg_btn")
        self.tabWidget.addTab(self.zhouchangTab, "")
        self.utilTab = QtWidgets.QWidget()
        self.utilTab.setObjectName("utilTab")
        self.shopping2_btn = QtWidgets.QPushButton(parent=self.utilTab)
        self.shopping2_btn.setGeometry(QtCore.QRect(10, 55, 75, 23))
        self.shopping2_btn.setObjectName("shopping2_btn")
        self.shopping1_btn = QtWidgets.QPushButton(parent=self.utilTab)
        self.shopping1_btn.setGeometry(QtCore.QRect(10, 15, 75, 23))
        self.shopping1_btn.setObjectName("shopping1_btn")
        self.shopping3_btn = QtWidgets.QPushButton(parent=self.utilTab)
        self.shopping3_btn.setGeometry(QtCore.QRect(10, 95, 75, 23))
        self.shopping3_btn.setObjectName("shopping3_btn")
        self.shopping2_txt = QtWidgets.QLabel(parent=self.utilTab)
        self.shopping2_txt.setGeometry(QtCore.QRect(100, 55, 111, 21))
        self.shopping2_txt.setObjectName("shopping2_txt")
        self.shopping3_txt = QtWidgets.QLabel(parent=self.utilTab)
        self.shopping3_txt.setGeometry(QtCore.QRect(100, 90, 121, 31))
        self.shopping3_txt.setObjectName("shopping3_txt")
        self.bangpai2_btn = QtWidgets.QPushButton(parent=self.utilTab)
        self.bangpai2_btn.setGeometry(QtCore.QRect(10, 135, 75, 23))
        self.bangpai2_btn.setObjectName("bangpai2_btn")
        self.shopping1_txt = QtWidgets.QLabel(parent=self.utilTab)
        self.shopping1_txt.setGeometry(QtCore.QRect(100, 5, 361, 41))
        self.shopping1_txt.setObjectName("shopping1_txt")
        self.bangpai2_cfg_btn = QtWidgets.QToolButton(parent=self.utilTab)
        self.bangpai2_cfg_btn.setGeometry(QtCore.QRect(90, 135, 37, 18))
        self.bangpai2_cfg_btn.setObjectName("bangpai2_cfg_btn")
        self.auto_battle_btn = QtWidgets.QPushButton(parent=self.utilTab)
        self.auto_battle_btn.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.auto_battle_btn.setObjectName("auto_battle_btn")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.utilTab)
        self.groupBox_2.setGeometry(QtCore.QRect(100, 170, 311, 41))
        self.groupBox_2.setObjectName("groupBox_2")
        self.auto_battle_linglongshi_rdo = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.auto_battle_linglongshi_rdo.setGeometry(QtCore.QRect(150, 20, 61, 16))
        self.auto_battle_linglongshi_rdo.setObjectName("auto_battle_linglongshi_rdo")
        self.auto_battle_none_rdo = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.auto_battle_none_rdo.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.auto_battle_none_rdo.setChecked(True)
        self.auto_battle_none_rdo.setObjectName("auto_battle_none_rdo")
        self.auto_battle_jingjichang_rdo = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.auto_battle_jingjichang_rdo.setGeometry(QtCore.QRect(70, 20, 89, 16))
        self.auto_battle_jingjichang_rdo.setObjectName("auto_battle_jingjichang_rdo")
        self.auto_battle_huashang_rdo = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.auto_battle_huashang_rdo.setGeometry(QtCore.QRect(230, 20, 61, 16))
        self.auto_battle_huashang_rdo.setObjectName("auto_battle_huashang_rdo")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.utilTab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 230, 411, 51))
        self.groupBox_4.setObjectName("groupBox_4")
        self.cusomer_ipt = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.cusomer_ipt.setGeometry(QtCore.QRect(10, 20, 301, 21))
        self.cusomer_ipt.setText("")
        self.cusomer_ipt.setObjectName("cusomer_ipt")
        self.run_customer_btn = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.run_customer_btn.setGeometry(QtCore.QRect(320, 20, 75, 23))
        self.run_customer_btn.setObjectName("run_customer_btn")
        self.tabWidget.addTab(self.utilTab, "")
        self.game_process_small_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.game_process_small_btn.setGeometry(QtCore.QRect(620, 40, 75, 23))
        self.game_process_small_btn.setObjectName("game_process_small_btn")
        self.game_process_origin_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.game_process_origin_btn.setGeometry(QtCore.QRect(710, 40, 75, 23))
        self.game_process_origin_btn.setObjectName("game_process_origin_btn")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(620, 310, 161, 121))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.target_rdo2 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.target_rdo2.setGeometry(QtCore.QRect(80, 40, 89, 16))
        self.target_rdo2.setObjectName("target_rdo2")
        self.target_rdo1 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.target_rdo1.setGeometry(QtCore.QRect(80, 10, 89, 16))
        self.target_rdo1.setChecked(True)
        self.target_rdo1.setObjectName("target_rdo1")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_10.setObjectName("label_10")
        self.target_rdo3 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.target_rdo3.setGeometry(QtCore.QRect(80, 70, 89, 16))
        self.target_rdo3.setObjectName("target_rdo3")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label_5.setObjectName("label_5")
        self.target_rdo_m1 = QtWidgets.QRadioButton(parent=self.groupBox)
        self.target_rdo_m1.setGeometry(QtCore.QRect(80, 100, 89, 16))
        self.target_rdo_m1.setObjectName("target_rdo_m1")
        self.log_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.log_btn.setGeometry(QtCore.QRect(700, 450, 75, 23))
        self.log_btn.setObjectName("log_btn")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(620, 100, 161, 171))
        self.listWidget.setObjectName("listWidget")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 701, 16))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.black_win = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.black_win.setGeometry(QtCore.QRect(630, 450, 71, 16))
        self.black_win.setChecked(True)
        self.black_win.setObjectName("black_win")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "梦幻手游助手"))
        self.close_mission_btn.setText(_translate("MainWindow", "终止选中任务"))
        self.label.setText(_translate("MainWindow", "正在运行的程序"))
        self.label_2.setText(_translate("MainWindow", "本软件免费提供"))
        self.baotu_btn.setText(_translate("MainWindow", "宝图"))
        self.mijing_btn.setText(_translate("MainWindow", "秘境"))
        self.dati_btn.setText(_translate("MainWindow", "答题"))
        self.yabiao_btn.setText(_translate("MainWindow", "押镖"))
        self.batch_richang.setText(_translate("MainWindow", "一键顺序执行"))
        self.baotu_cfg_btn.setText(_translate("MainWindow", "配置"))
        self.yabiao_txt.setText(_translate("MainWindow", "自行保证此时活力到达50"))
        self.missionrichang_shutdown_chk.setText(_translate("MainWindow", "完成后自动关机"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.richangTab1), _translate("MainWindow", "单人日常"))
        self.batch_mission520.setText(_translate("MainWindow", "一键顺序执行"))
        self.fuben_norm70_btn.setText(_translate("MainWindow", "70普通"))
        self.label_4.setText(_translate("MainWindow", "需至少一个普通副本没有执行过才可运行"))
        self.fuben_xiashi70_btn.setText(_translate("MainWindow", "70侠士"))
        self.fuben_xiashi50_btn.setText(_translate("MainWindow", "50侠士"))
        self.fuben_norm50_btn2.setText(_translate("MainWindow", "50普通2"))
        self.fuben_norm50_btn1.setText(_translate("MainWindow", "50普通1"))
        self.label_7.setText(_translate("MainWindow", "捉鬼"))
        self.mission520_shutdown_chk.setText(_translate("MainWindow", "完成后自动关机"))
        self.label_8.setText(_translate("MainWindow", "副本"))
        self.label_9.setText(_translate("MainWindow", "通常不需要勾选第一个副本，因为一般开始时已经进去了"))
        self.ghost_btn.setText(_translate("MainWindow", "轮鬼"))
        self.ghost5_btn.setText(_translate("MainWindow", "五轮鬼"))
        self.ghost_ipt.setText(_translate("MainWindow", "25"))
        self.ghost2_btn.setText(_translate("MainWindow", "两轮鬼"))
        self.ghost_cfg_btn.setText(_translate("MainWindow", "配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.richangTab2), _translate("MainWindow", "多人日常"))
        self.menpai_cfg_btn.setText(_translate("MainWindow", "配置"))
        self.mihunta_btn.setText(_translate("MainWindow", "周五迷魂塔"))
        self.menpai_btn.setText(_translate("MainWindow", "周一门派"))
        self.haidi_btn.setText(_translate("MainWindow", "周三海底"))
        self.mihunta_cfg_btn.setText(_translate("MainWindow", "配置"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.zhouchangTab), _translate("MainWindow", "周常"))
        self.shopping2_btn.setText(_translate("MainWindow", "收关注"))
        self.shopping1_btn.setText(_translate("MainWindow", "收非珍品"))
        self.shopping3_btn.setText(_translate("MainWindow", "搜索截胡"))
        self.shopping2_txt.setText(_translate("MainWindow", "注意提前解锁安全锁"))
        self.shopping3_txt.setText(_translate("MainWindow", "需提前定好搜索条件"))
        self.bangpai2_btn.setText(_translate("MainWindow", "帮派任务"))
        self.shopping1_txt.setText(_translate("MainWindow", "自行设计mhxy_shopping.py脚本细节"))
        self.bangpai2_cfg_btn.setText(_translate("MainWindow", "配置"))
        self.auto_battle_btn.setText(_translate("MainWindow", "自动战斗"))
        self.groupBox_2.setTitle(_translate("MainWindow", "附加"))
        self.auto_battle_linglongshi_rdo.setText(_translate("MainWindow", "玲珑石"))
        self.auto_battle_none_rdo.setText(_translate("MainWindow", "无"))
        self.auto_battle_jingjichang_rdo.setText(_translate("MainWindow", "竞技场"))
        self.auto_battle_huashang_rdo.setText(_translate("MainWindow", "华山"))
        self.groupBox_4.setTitle(_translate("MainWindow", "自定义区"))
        self.run_customer_btn.setText(_translate("MainWindow", "执行命令"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.utilTab), _translate("MainWindow", "工具"))
        self.game_process_small_btn.setText(_translate("MainWindow", "调整为小窗"))
        self.game_process_origin_btn.setText(_translate("MainWindow", "调整为大窗"))
        self.target_rdo2.setText(_translate("MainWindow", "第二窗口"))
        self.target_rdo1.setText(_translate("MainWindow", "第一窗口"))
        self.label_10.setText(_translate("MainWindow", "执行目标"))
        self.target_rdo3.setText(_translate("MainWindow", "第三窗口"))
        self.label_5.setText(_translate("MainWindow", "从左往右"))
        self.target_rdo_m1.setText(_translate("MainWindow", "串行"))
        self.log_btn.setText(_translate("MainWindow", "打开日志"))
        self.label_3.setText(_translate("MainWindow", "脚本目录："))
        self.black_win.setText(_translate("MainWindow", "小黑窗"))
