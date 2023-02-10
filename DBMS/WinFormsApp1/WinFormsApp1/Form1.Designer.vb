<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
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
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.Addbtn = New System.Windows.Forms.Button()
        Me.Subbtn = New System.Windows.Forms.Button()
        Me.TextBox1 = New System.Windows.Forms.TextBox()
        Me.TextBox2 = New System.Windows.Forms.TextBox()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.resBox = New System.Windows.Forms.TextBox()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'Addbtn
        '
        Me.Addbtn.Location = New System.Drawing.Point(316, 405)
        Me.Addbtn.Name = "Addbtn"
        Me.Addbtn.Size = New System.Drawing.Size(307, 90)
        Me.Addbtn.TabIndex = 0
        Me.Addbtn.Text = "Add"
        Me.Addbtn.UseVisualStyleBackColor = True
        '
        'Subbtn
        '
        Me.Subbtn.Location = New System.Drawing.Point(743, 405)
        Me.Subbtn.Name = "Subbtn"
        Me.Subbtn.Size = New System.Drawing.Size(307, 90)
        Me.Subbtn.TabIndex = 1
        Me.Subbtn.Text = "Subtract"
        Me.Subbtn.UseVisualStyleBackColor = True
        '
        'TextBox1
        '
        Me.TextBox1.Location = New System.Drawing.Point(697, 128)
        Me.TextBox1.Name = "TextBox1"
        Me.TextBox1.Size = New System.Drawing.Size(353, 47)
        Me.TextBox1.TabIndex = 2
        '
        'TextBox2
        '
        Me.TextBox2.Location = New System.Drawing.Point(697, 238)
        Me.TextBox2.Name = "TextBox2"
        Me.TextBox2.Size = New System.Drawing.Size(353, 47)
        Me.TextBox2.TabIndex = 3
        '
        'Label1
        '
        Me.Label1.AutoSize = True
        Me.Label1.Location = New System.Drawing.Point(419, 128)
        Me.Label1.Name = "Label1"
        Me.Label1.Size = New System.Drawing.Size(205, 41)
        Me.Label1.TabIndex = 4
        Me.Label1.Text = "First Number :"
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(374, 241)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(249, 41)
        Me.Label2.TabIndex = 5
        Me.Label2.Text = "Second Number :"
        '
        'resBox
        '
        Me.resBox.Location = New System.Drawing.Point(547, 620)
        Me.resBox.Name = "resBox"
        Me.resBox.Size = New System.Drawing.Size(294, 47)
        Me.resBox.TabIndex = 6
        '
        'Label3
        '
        Me.Label3.AutoSize = True
        Me.Label3.Location = New System.Drawing.Point(631, 562)
        Me.Label3.Name = "Label3"
        Me.Label3.Size = New System.Drawing.Size(105, 41)
        Me.Label3.TabIndex = 7
        Me.Label3.Text = "Result:"
        '
        'Form1
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(17.0!, 41.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(1408, 731)
        Me.Controls.Add(Me.Label3)
        Me.Controls.Add(Me.resBox)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.Label1)
        Me.Controls.Add(Me.TextBox2)
        Me.Controls.Add(Me.TextBox1)
        Me.Controls.Add(Me.Subbtn)
        Me.Controls.Add(Me.Addbtn)
        Me.Name = "Form1"
        Me.Text = "Form1"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents Addbtn As Button
    Friend WithEvents Subbtn As Button
    Friend WithEvents TextBox1 As TextBox
    Friend WithEvents TextBox2 As TextBox
    Friend WithEvents Label1 As Label
    Friend WithEvents Label2 As Label
    Friend WithEvents resBox As TextBox
    Friend WithEvents Label3 As Label
End Class
