<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.txtRoll = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.txtName = New System.Windows.Forms.TextBox()
        Me.txtAddress = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.txtPhone = New System.Windows.Forms.TextBox()
        Me.btnSave = New System.Windows.Forms.Button()
        Me.btnEdit = New System.Windows.Forms.Button()
        Me.btnCancel = New System.Windows.Forms.Button()
        Me.btnSearch = New System.Windows.Forms.Button()
        Me.btnDelete = New System.Windows.Forms.Button()
        Me.btnNext = New System.Windows.Forms.Button()
        Me.btnPrev = New System.Windows.Forms.Button()
        Me.cbDept = New System.Windows.Forms.ListBox()
        Me.dgvStudents = New System.Windows.Forms.ListBox()
        Me.txtSearchRoll = New System.Windows.Forms.TextBox()
        Me.Label5 = New System.Windows.Forms.Label()
        Me.Label6 = New System.Windows.Forms.Label()
        Me.Label7 = New System.Windows.Forms.Label()
        Me.Label8 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'txtRoll
        '
        Me.txtRoll.Location = New System.Drawing.Point(526, 68)
        Me.txtRoll.Name = "txtRoll"
        Me.txtRoll.Size = New System.Drawing.Size(524, 38)
        Me.txtRoll.TabIndex = 1
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(347, 74)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(147, 32)
        Me.Label1.TabIndex = 2
        Me.Label1.Text = "Enter Roll:"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(322, 151)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(172, 32)
        Me.Label2.TabIndex = 4
        Me.Label2.Text = "Enter Name:"
        '
        'txtName
        '
        Me.txtName.Location = New System.Drawing.Point(526, 145)
        Me.txtName.Name = "txtName"
        Me.txtName.Size = New System.Drawing.Size(524, 38)
        Me.txtName.TabIndex = 3
        '
        'txtAddress
        '
        Me.txtAddress.Location = New System.Drawing.Point(526, 231)
        Me.txtAddress.Name = "txtAddress"
        Me.txtAddress.Size = New System.Drawing.Size(524, 38)
        Me.txtAddress.TabIndex = 5
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(293, 231)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(201, 32)
        Me.Label3.TabIndex = 6
        Me.Label3.Text = "Enter Address:"
        '
        'Label4
        '
        Me.Label4.AutoSize = True
        Me.Label4.Location = New System.Drawing.Point(256, 322)
        Me.Label4.Name = "Label4"
        Me.Label4.Size = New System.Drawing.Size(238, 32)
        Me.Label4.TabIndex = 8
        Me.Label4.Text = "Enter Phone No. :"
        '
        'txtPhone
        '
        Me.txtPhone.Location = New System.Drawing.Point(526, 322)
        Me.txtPhone.Name = "txtPhone"
        Me.txtPhone.Size = New System.Drawing.Size(524, 38)
        Me.txtPhone.TabIndex = 7
        '
        'btnSave
        '
        Me.btnSave.Location = New System.Drawing.Point(605, 428)
        Me.btnSave.Name = "btnSave"
        Me.btnSave.Size = New System.Drawing.Size(163, 67)
        Me.btnSave.TabIndex = 9
        Me.btnSave.Text = "SAVE"
        Me.btnSave.UseVisualStyleBackColor = True
        '
        'btnEdit
        '
        Me.btnEdit.Location = New System.Drawing.Point(798, 428)
        Me.btnEdit.Name = "btnEdit"
        Me.btnEdit.Size = New System.Drawing.Size(167, 67)
        Me.btnEdit.TabIndex = 10
        Me.btnEdit.Text = "EDIT"
        Me.btnEdit.UseVisualStyleBackColor = True
        '
        'btnCancel
        '
        Me.btnCancel.Location = New System.Drawing.Point(1514, 428)
        Me.btnCancel.Name = "btnCancel"
        Me.btnCancel.Size = New System.Drawing.Size(172, 67)
        Me.btnCancel.TabIndex = 11
        Me.btnCancel.Text = "CANCEL"
        Me.btnCancel.UseVisualStyleBackColor = True
        '
        'btnSearch
        '
        Me.btnSearch.Location = New System.Drawing.Point(1330, 838)
        Me.btnSearch.Name = "btnSearch"
        Me.btnSearch.Size = New System.Drawing.Size(160, 67)
        Me.btnSearch.TabIndex = 12
        Me.btnSearch.Text = "SEARCH"
        Me.btnSearch.UseVisualStyleBackColor = True
        '
        'btnDelete
        '
        Me.btnDelete.Location = New System.Drawing.Point(1300, 428)
        Me.btnDelete.Name = "btnDelete"
        Me.btnDelete.Size = New System.Drawing.Size(176, 67)
        Me.btnDelete.TabIndex = 13
        Me.btnDelete.Text = "DELETE"
        Me.btnDelete.UseVisualStyleBackColor = True
        '
        'btnNext
        '
        Me.btnNext.Location = New System.Drawing.Point(709, 838)
        Me.btnNext.Name = "btnNext"
        Me.btnNext.Size = New System.Drawing.Size(180, 67)
        Me.btnNext.TabIndex = 14
        Me.btnNext.Text = "NEXT"
        Me.btnNext.UseVisualStyleBackColor = True
        '
        'btnPrev
        '
        Me.btnPrev.Location = New System.Drawing.Point(364, 838)
        Me.btnPrev.Name = "btnPrev"
        Me.btnPrev.Size = New System.Drawing.Size(182, 67)
        Me.btnPrev.TabIndex = 15
        Me.btnPrev.Text = "PREV"
        Me.btnPrev.UseVisualStyleBackColor = True
        '
        'cbDept
        '
        Me.cbDept.FormattingEnabled = True
        Me.cbDept.ItemHeight = 31
        Me.cbDept.Location = New System.Drawing.Point(1161, 139)
        Me.cbDept.Name = "cbDept"
        Me.cbDept.Size = New System.Drawing.Size(525, 221)
        Me.cbDept.TabIndex = 16
        '
        'dgvStudents
        '
        Me.dgvStudents.FormattingEnabled = True
        Me.dgvStudents.ItemHeight = 31
        Me.dgvStudents.Location = New System.Drawing.Point(364, 664)
        Me.dgvStudents.Name = "dgvStudents"
        Me.dgvStudents.Size = New System.Drawing.Size(525, 128)
        Me.dgvStudents.TabIndex = 17
        '
        'txtSearchRoll
        '
        Me.txtSearchRoll.Location = New System.Drawing.Point(1161, 766)
        Me.txtSearchRoll.Name = "txtSearchRoll"
        Me.txtSearchRoll.Size = New System.Drawing.Size(524, 38)
        Me.txtSearchRoll.TabIndex = 18
        '
        'Label5
        '
        Me.Label5.AutoSize = True
        Me.Label5.Location = New System.Drawing.Point(1155, 708)
        Me.Label5.Name = "Label5"
        Me.Label5.Size = New System.Drawing.Size(282, 32)
        Me.Label5.TabIndex = 19
        Me.Label5.Text = "Search Student Roll :"
        '
        'Label6
        '
        Me.Label6.AutoSize = True
        Me.Label6.Location = New System.Drawing.Point(1155, 74)
        Me.Label6.Name = "Label6"
        Me.Label6.Size = New System.Drawing.Size(139, 32)
        Me.Label6.TabIndex = 20
        Me.Label6.Text = "Set Dept :"
        '
        'Label7
        '
        Me.Label7.AutoSize = True
        Me.Label7.Location = New System.Drawing.Point(293, 545)
        Me.Label7.Name = "Label7"
        Me.Label7.Size = New System.Drawing.Size(1427, 32)
        Me.Label7.TabIndex = 21
        Me.Label7.Text = "---------------------------------------------------------------------------------" &
    "----------------------------------------------------------------------------"
        '
        'Label8
        '
        Me.Label8.AutoSize = True
        Me.Label8.Location = New System.Drawing.Point(520, 610)
        Me.Label8.Name = "Label8"
        Me.Label8.Size = New System.Drawing.Size(203, 32)
        Me.Label8.TabIndex = 22
        Me.Label8.Text = "View Records :"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(16.0!, 31.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1934, 968)
        Me.Controls.Add(Me.Label8)
        Me.Controls.Add(Me.Label7)
        Me.Controls.Add(Me.Label6)
        Me.Controls.Add(Me.Label5)
        Me.Controls.Add(Me.txtSearchRoll)
        Me.Controls.Add(Me.dgvStudents)
        Me.Controls.Add(Me.cbDept)
        Me.Controls.Add(Me.btnPrev)
        Me.Controls.Add(Me.btnNext)
        Me.Controls.Add(Me.btnDelete)
        Me.Controls.Add(Me.btnSearch)
        Me.Controls.Add(Me.btnCancel)
        Me.Controls.Add(Me.btnEdit)
        Me.Controls.Add(Me.btnSave)
        Me.Controls.Add(Me.Label4)
        Me.Controls.Add(Me.txtPhone)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.txtAddress)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.txtName)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.txtRoll)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents txtRoll As TextBox
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents txtName As TextBox
    Friend WithEvents txtAddress As TextBox
    Friend WithEvents Label3 As Label
    Friend WithEvents Label4 As Label
    Friend WithEvents txtPhone As TextBox
    Friend WithEvents btnSave As Button
    Friend WithEvents btnEdit As Button
    Friend WithEvents btnCancel As Button
    Friend WithEvents btnSearch As Button
    Friend WithEvents btnDelete As Button
    Friend WithEvents btnNext As Button
    Friend WithEvents btnPrev As Button
    Friend WithEvents cbDept As ListBox
    Friend WithEvents dgvStudents As ListBox
    Friend WithEvents txtSearchRoll As TextBox
    Friend WithEvents Label5 As Label
    Friend WithEvents Label6 As Label
    Friend WithEvents Label7 As Label
    Friend WithEvents Label8 As Label
End Class
