#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QMainWindow>
#include <QtGui>
#include <QtCore>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT
public slots:
    void Mouse_Pressed();
    void showMousePosition(QPoint& pos);
public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_show_axes_clicked();
    void on_set_point1_clicked();
    void on_set_point2_clicked();
    void on_setgridbutton_clicked();
    void on_resetButton_clicked();
    void on_spinBox_textChanged(const QString &arg1);
    void on_DDALine_clicked();
    void DDAline(int r, int g, int b);
    void BresenhamLINE (int r, int g, int b);
    void on_bresenhamLine_clicked();
    void on_midPointCircle_clicked();
    void on_bresenhamCircle_clicked();
    void on_PolarEllipse_clicked(); //ellipse
    void on_MidPointEllipse_clicked();
    void on_floodfill_clicked();
    void floodfillutil(int x, int y, int r, int g, int b);
    void on_floodfill2_clicked();
    void floodfill2util(int x, int y, int r, int g, int b);
    void on_boundaryfill1_clicked();
    void boundaryfill1util(int x, int y, QRgb q, int r, int g, int b);
    void on_boundaryfill2_clicked();
    void boundaryfill2util(int x, int y, QRgb q, int r, int g, int b);
    void on_scanlinefill_clicked();
    void initEdgeTable();
    void storeEdgeInTable (int x1,int y1, int x2, int y2);
    void on_setvertex_clicked();
    void on_clearvertex_clicked();
    void polyDraw (int r, int g, int b);
    void on_translate_clicked();
    void on_setOriginButton_clicked();
    void on_rotate_clicked();
    void on_shear_clicked();
    void on_scale_clicked();
    void on_reflection_clicked();
    void draw_Window();
    void on_setCorner1_clicked();
    void on_setCorner2_clicked();
    int computeCode(int xa, int ya);
    void cohenSutherlandClip(int x1, int y1,int x2, int y2);
    void on_lineClipping_clicked();
    int x_intersect(int x1, int y1, int x2, int y2,int x3, int y3, int x4, int y4);
    int y_intersect(int x1, int y1, int x2, int y2,int x3, int y3, int x4, int y4);
    void clip(int x1, int y1, int x2, int y2);
    void suthHodgClip();
    void on_polygonClipping_clicked();







private:
    Ui::MainWindow *ui;
    QPoint p1,p2;
    QPoint cp1;
    QPoint cp2;
    QPoint origin;
    void point(int x,int y, int r, int g, int b);
};

#endif // MAINWINDOW_H
