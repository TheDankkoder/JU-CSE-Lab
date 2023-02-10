/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.3.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpinBox>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>
#include <my_label.h>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    my_label *frame;
    QLabel *mouse_movement;
    QLabel *label_3;
    QLabel *mouse_pressed;
    QLabel *label_5;
    QFrame *x_axis;
    QFrame *y_axis;
    QCheckBox *show_axes;
    QPushButton *Draw;
    QSpinBox *circle_radius;
    QRadioButton *draw_circle;
    QRadioButton *draw_line;
    QPushButton *set_point1;
    QPushButton *set_point2;
    QPushButton *resetButton;
    QPushButton *setgridbutton;
    QSpinBox *spinBox;
    QPushButton *quadrantShow;
    QPushButton *DDALine;
    QPushButton *bresenhamLine;
    QSpinBox *radiusspinbox;
    QSpinBox *r1spinbox;
    QSpinBox *r2spinbox;
    QPushButton *midPointCircle;
    QPushButton *bresenhamCircle;
    QPushButton *PollarEllipse;
    QPushButton *setvertex;
    QPushButton *clearvertex;
    QPushButton *scanlinefill;
    QPushButton *boundaryfill2;
    QPushButton *boundaryfill1;
    QLabel *timeValue;
    QPushButton *MidpointEllipse;
    QLabel *label_6;
    QLabel *label;
    QLabel *label_2;
    QPushButton *floodfill;
    QPushButton *floodfill_2;
    QPushButton *translate;
    QSpinBox *tx;
    QSpinBox *ty;
    QPushButton *rotate;
    QSpinBox *degree;
    QPushButton *setOriginButton;
    QLabel *originValue;
    QPushButton *scale;
    QSpinBox *sx;
    QSpinBox *sy;
    QSpinBox *shy;
    QSpinBox *shx;
    QPushButton *shear;
    QPushButton *reflection;
    QLabel *label_7;
    QPushButton *setCorner1;
    QPushButton *setCorner2;
    QPushButton *lineClipping;
    QPushButton *polygonClipping;
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1215, 911);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        frame = new my_label(centralWidget);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(0, 0, 700, 700));
        frame->setCursor(QCursor(Qt::CrossCursor));
        frame->setMouseTracking(true);
        frame->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        frame->setFrameShape(QFrame::Box);
        frame->setLineWidth(1);
        mouse_movement = new QLabel(centralWidget);
        mouse_movement->setObjectName(QString::fromUtf8("mouse_movement"));
        mouse_movement->setGeometry(QRect(720, 70, 111, 31));
        mouse_movement->setFrameShape(QFrame::Panel);
        label_3 = new QLabel(centralWidget);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(720, 50, 111, 20));
        mouse_pressed = new QLabel(centralWidget);
        mouse_pressed->setObjectName(QString::fromUtf8("mouse_pressed"));
        mouse_pressed->setGeometry(QRect(720, 140, 111, 31));
        mouse_pressed->setFrameShape(QFrame::Panel);
        label_5 = new QLabel(centralWidget);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(730, 120, 81, 20));
        x_axis = new QFrame(centralWidget);
        x_axis->setObjectName(QString::fromUtf8("x_axis"));
        x_axis->setGeometry(QRect(0, 225, 700, 1));
        x_axis->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 85, 255);"));
        x_axis->setFrameShape(QFrame::HLine);
        x_axis->setFrameShadow(QFrame::Sunken);
        y_axis = new QFrame(centralWidget);
        y_axis->setObjectName(QString::fromUtf8("y_axis"));
        y_axis->setGeometry(QRect(225, 0, 1, 700));
        y_axis->setStyleSheet(QString::fromUtf8("\n"
"background-color: rgb(85, 255, 255);"));
        y_axis->setFrameShape(QFrame::VLine);
        y_axis->setFrameShadow(QFrame::Sunken);
        show_axes = new QCheckBox(centralWidget);
        show_axes->setObjectName(QString::fromUtf8("show_axes"));
        show_axes->setGeometry(QRect(720, 10, 91, 21));
        Draw = new QPushButton(centralWidget);
        Draw->setObjectName(QString::fromUtf8("Draw"));
        Draw->setGeometry(QRect(710, 290, 101, 41));
        circle_radius = new QSpinBox(centralWidget);
        circle_radius->setObjectName(QString::fromUtf8("circle_radius"));
        circle_radius->setGeometry(QRect(900, 240, 46, 20));
        draw_circle = new QRadioButton(centralWidget);
        draw_circle->setObjectName(QString::fromUtf8("draw_circle"));
        draw_circle->setGeometry(QRect(820, 240, 81, 17));
        draw_line = new QRadioButton(centralWidget);
        draw_line->setObjectName(QString::fromUtf8("draw_line"));
        draw_line->setGeometry(QRect(710, 240, 77, 17));
        set_point1 = new QPushButton(centralWidget);
        set_point1->setObjectName(QString::fromUtf8("set_point1"));
        set_point1->setGeometry(QRect(720, 200, 81, 23));
        set_point2 = new QPushButton(centralWidget);
        set_point2->setObjectName(QString::fromUtf8("set_point2"));
        set_point2->setGeometry(QRect(830, 200, 81, 23));
        resetButton = new QPushButton(centralWidget);
        resetButton->setObjectName(QString::fromUtf8("resetButton"));
        resetButton->setGeometry(QRect(840, 290, 101, 41));
        setgridbutton = new QPushButton(centralWidget);
        setgridbutton->setObjectName(QString::fromUtf8("setgridbutton"));
        setgridbutton->setGeometry(QRect(720, 350, 83, 29));
        spinBox = new QSpinBox(centralWidget);
        spinBox->setObjectName(QString::fromUtf8("spinBox"));
        spinBox->setGeometry(QRect(820, 350, 48, 29));
        quadrantShow = new QPushButton(centralWidget);
        quadrantShow->setObjectName(QString::fromUtf8("quadrantShow"));
        quadrantShow->setGeometry(QRect(880, 350, 111, 31));
        DDALine = new QPushButton(centralWidget);
        DDALine->setObjectName(QString::fromUtf8("DDALine"));
        DDALine->setGeometry(QRect(710, 410, 91, 31));
        bresenhamLine = new QPushButton(centralWidget);
        bresenhamLine->setObjectName(QString::fromUtf8("bresenhamLine"));
        bresenhamLine->setGeometry(QRect(810, 410, 91, 31));
        radiusspinbox = new QSpinBox(centralWidget);
        radiusspinbox->setObjectName(QString::fromUtf8("radiusspinbox"));
        radiusspinbox->setGeometry(QRect(890, 490, 48, 29));
        r1spinbox = new QSpinBox(centralWidget);
        r1spinbox->setObjectName(QString::fromUtf8("r1spinbox"));
        r1spinbox->setGeometry(QRect(720, 570, 48, 29));
        r2spinbox = new QSpinBox(centralWidget);
        r2spinbox->setObjectName(QString::fromUtf8("r2spinbox"));
        r2spinbox->setGeometry(QRect(780, 570, 48, 29));
        midPointCircle = new QPushButton(centralWidget);
        midPointCircle->setObjectName(QString::fromUtf8("midPointCircle"));
        midPointCircle->setGeometry(QRect(710, 470, 111, 31));
        bresenhamCircle = new QPushButton(centralWidget);
        bresenhamCircle->setObjectName(QString::fromUtf8("bresenhamCircle"));
        bresenhamCircle->setGeometry(QRect(710, 510, 121, 31));
        PollarEllipse = new QPushButton(centralWidget);
        PollarEllipse->setObjectName(QString::fromUtf8("PollarEllipse"));
        PollarEllipse->setGeometry(QRect(860, 560, 111, 31));
        setvertex = new QPushButton(centralWidget);
        setvertex->setObjectName(QString::fromUtf8("setvertex"));
        setvertex->setGeometry(QRect(730, 660, 80, 21));
        clearvertex = new QPushButton(centralWidget);
        clearvertex->setObjectName(QString::fromUtf8("clearvertex"));
        clearvertex->setGeometry(QRect(830, 660, 80, 21));
        scanlinefill = new QPushButton(centralWidget);
        scanlinefill->setObjectName(QString::fromUtf8("scanlinefill"));
        scanlinefill->setGeometry(QRect(920, 660, 80, 21));
        boundaryfill2 = new QPushButton(centralWidget);
        boundaryfill2->setObjectName(QString::fromUtf8("boundaryfill2"));
        boundaryfill2->setGeometry(QRect(740, 720, 91, 31));
        boundaryfill1 = new QPushButton(centralWidget);
        boundaryfill1->setObjectName(QString::fromUtf8("boundaryfill1"));
        boundaryfill1->setGeometry(QRect(880, 720, 91, 31));
        timeValue = new QLabel(centralWidget);
        timeValue->setObjectName(QString::fromUtf8("timeValue"));
        timeValue->setGeometry(QRect(900, 450, 111, 31));
        timeValue->setFrameShape(QFrame::Panel);
        MidpointEllipse = new QPushButton(centralWidget);
        MidpointEllipse->setObjectName(QString::fromUtf8("MidpointEllipse"));
        MidpointEllipse->setGeometry(QRect(860, 600, 111, 31));
        label_6 = new QLabel(centralWidget);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(930, 420, 81, 20));
        label = new QLabel(centralWidget);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(830, 700, 71, 16));
        label_2 = new QLabel(centralWidget);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(1080, 690, 71, 16));
        floodfill = new QPushButton(centralWidget);
        floodfill->setObjectName(QString::fromUtf8("floodfill"));
        floodfill->setGeometry(QRect(1110, 720, 91, 31));
        floodfill_2 = new QPushButton(centralWidget);
        floodfill_2->setObjectName(QString::fromUtf8("floodfill_2"));
        floodfill_2->setGeometry(QRect(1000, 720, 91, 31));
        translate = new QPushButton(centralWidget);
        translate->setObjectName(QString::fromUtf8("translate"));
        translate->setGeometry(QRect(910, 60, 91, 31));
        tx = new QSpinBox(centralWidget);
        tx->setObjectName(QString::fromUtf8("tx"));
        tx->setGeometry(QRect(910, 110, 46, 20));
        ty = new QSpinBox(centralWidget);
        ty->setObjectName(QString::fromUtf8("ty"));
        ty->setGeometry(QRect(970, 110, 46, 20));
        rotate = new QPushButton(centralWidget);
        rotate->setObjectName(QString::fromUtf8("rotate"));
        rotate->setGeometry(QRect(1050, 60, 91, 31));
        degree = new QSpinBox(centralWidget);
        degree->setObjectName(QString::fromUtf8("degree"));
        degree->setGeometry(QRect(1070, 110, 46, 20));
        setOriginButton = new QPushButton(centralWidget);
        setOriginButton->setObjectName(QString::fromUtf8("setOriginButton"));
        setOriginButton->setGeometry(QRect(980, 10, 91, 31));
        originValue = new QLabel(centralWidget);
        originValue->setObjectName(QString::fromUtf8("originValue"));
        originValue->setGeometry(QRect(1090, 20, 81, 20));
        scale = new QPushButton(centralWidget);
        scale->setObjectName(QString::fromUtf8("scale"));
        scale->setGeometry(QRect(1050, 150, 91, 31));
        sx = new QSpinBox(centralWidget);
        sx->setObjectName(QString::fromUtf8("sx"));
        sx->setGeometry(QRect(1040, 200, 46, 20));
        sy = new QSpinBox(centralWidget);
        sy->setObjectName(QString::fromUtf8("sy"));
        sy->setGeometry(QRect(1100, 200, 46, 20));
        shy = new QSpinBox(centralWidget);
        shy->setObjectName(QString::fromUtf8("shy"));
        shy->setGeometry(QRect(1100, 290, 46, 20));
        shx = new QSpinBox(centralWidget);
        shx->setObjectName(QString::fromUtf8("shx"));
        shx->setGeometry(QRect(1040, 290, 46, 20));
        shear = new QPushButton(centralWidget);
        shear->setObjectName(QString::fromUtf8("shear"));
        shear->setGeometry(QRect(1050, 240, 91, 31));
        reflection = new QPushButton(centralWidget);
        reflection->setObjectName(QString::fromUtf8("reflection"));
        reflection->setGeometry(QRect(1050, 330, 91, 31));
        label_7 = new QLabel(centralWidget);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(1090, 390, 81, 20));
        setCorner1 = new QPushButton(centralWidget);
        setCorner1->setObjectName(QString::fromUtf8("setCorner1"));
        setCorner1->setGeometry(QRect(1020, 450, 91, 31));
        setCorner2 = new QPushButton(centralWidget);
        setCorner2->setObjectName(QString::fromUtf8("setCorner2"));
        setCorner2->setGeometry(QRect(1120, 450, 91, 31));
        lineClipping = new QPushButton(centralWidget);
        lineClipping->setObjectName(QString::fromUtf8("lineClipping"));
        lineClipping->setGeometry(QRect(1020, 490, 91, 31));
        polygonClipping = new QPushButton(centralWidget);
        polygonClipping->setObjectName(QString::fromUtf8("polygonClipping"));
        polygonClipping->setGeometry(QRect(1120, 490, 91, 31));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 1215, 19));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MainWindow->setStatusBar(statusBar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        frame->setText(QString());
        mouse_movement->setText(QString());
        label_3->setText(QCoreApplication::translate("MainWindow", "    Mouse Movement", nullptr));
        mouse_pressed->setText(QString());
        label_5->setText(QCoreApplication::translate("MainWindow", "Mouse Pressed", nullptr));
        show_axes->setText(QCoreApplication::translate("MainWindow", "Show Axes", nullptr));
        Draw->setText(QCoreApplication::translate("MainWindow", "Draw", nullptr));
        draw_circle->setText(QCoreApplication::translate("MainWindow", "Draw Circle", nullptr));
        draw_line->setText(QCoreApplication::translate("MainWindow", "Draw Line", nullptr));
        set_point1->setText(QCoreApplication::translate("MainWindow", "Set point 1", nullptr));
        set_point2->setText(QCoreApplication::translate("MainWindow", "Set point 2", nullptr));
        resetButton->setText(QCoreApplication::translate("MainWindow", "RESET", nullptr));
        setgridbutton->setText(QCoreApplication::translate("MainWindow", "make grid", nullptr));
        quadrantShow->setText(QCoreApplication::translate("MainWindow", "quadrantShow", nullptr));
        DDALine->setText(QCoreApplication::translate("MainWindow", "Draw_DDA", nullptr));
        bresenhamLine->setText(QCoreApplication::translate("MainWindow", "Draw_Bresenham", nullptr));
        midPointCircle->setText(QCoreApplication::translate("MainWindow", "draw midpoint circle", nullptr));
        bresenhamCircle->setText(QCoreApplication::translate("MainWindow", "draw bresenham circle", nullptr));
        PollarEllipse->setText(QCoreApplication::translate("MainWindow", "Polar ellipse", nullptr));
        setvertex->setText(QCoreApplication::translate("MainWindow", "setVertex", nullptr));
        clearvertex->setText(QCoreApplication::translate("MainWindow", "clear vertex", nullptr));
        scanlinefill->setText(QCoreApplication::translate("MainWindow", "scanline fill", nullptr));
        boundaryfill2->setText(QCoreApplication::translate("MainWindow", "8 connected", nullptr));
        boundaryfill1->setText(QCoreApplication::translate("MainWindow", "4 connected", nullptr));
        timeValue->setText(QString());
        MidpointEllipse->setText(QCoreApplication::translate("MainWindow", "Midpoint ellipse", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Time taken:", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Boundary Fill", nullptr));
        label_2->setText(QCoreApplication::translate("MainWindow", "Flood Fill", nullptr));
        floodfill->setText(QCoreApplication::translate("MainWindow", "4 connected", nullptr));
        floodfill_2->setText(QCoreApplication::translate("MainWindow", "8 connected", nullptr));
        translate->setText(QCoreApplication::translate("MainWindow", "Translate", nullptr));
        rotate->setText(QCoreApplication::translate("MainWindow", "Rotate", nullptr));
        setOriginButton->setText(QCoreApplication::translate("MainWindow", "set Origin", nullptr));
        originValue->setText(QString());
        scale->setText(QCoreApplication::translate("MainWindow", "Scale", nullptr));
        shear->setText(QCoreApplication::translate("MainWindow", "Shear", nullptr));
        reflection->setText(QCoreApplication::translate("MainWindow", "Reflect", nullptr));
        label_7->setText(QCoreApplication::translate("MainWindow", "Clipping :", nullptr));
        setCorner1->setText(QCoreApplication::translate("MainWindow", "Set Corner 1", nullptr));
        setCorner2->setText(QCoreApplication::translate("MainWindow", "Set Corner 2", nullptr));
        lineClipping->setText(QCoreApplication::translate("MainWindow", "Line Clip", nullptr));
        polygonClipping->setText(QCoreApplication::translate("MainWindow", "Polygon Clip", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
