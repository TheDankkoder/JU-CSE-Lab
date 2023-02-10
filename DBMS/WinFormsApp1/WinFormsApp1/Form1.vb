Public Class Form1

    Private depts As New List(Of Department) From {
        New Department("CSE", "Computer Science"),
        New Department("IT", "Information Technology"),
        New Department("ECE", "Electronics and Communications"),
        New Department("MECH", "Mechanical Engineering")
    }
    Private students As New List(Of Student)

    Private currentPage As Integer = 1
    Private pageSize As Integer = 5


    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        Dim SomeVariable As String

        SomeVariable = DateTime.Now.ToString("MM/dd/yyyy")
        Me.Text = SomeVariable

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Addbtn.Click

        Dim num1 As Integer
        Dim num2 As Integer
        Dim result As Integer


        num1 = Integer.Parse(TextBox1.Text)
        num2 = Integer.Parse(TextBox2.Text)
        result = num1 + num2
        resBox.Text = result


    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles Label2.Click

    End Sub

    Private Sub Button1_Click_1(sender As Object, e As EventArgs) Handles Subbtn.Click

        Dim num1 As Integer
        Dim num2 As Integer
        Dim result As Integer


        num1 = Integer.Parse(TextBox1.Text)
        num2 = Integer.Parse(TextBox2.Text)
        result = num1 - num2
        resBox.Text = result


    End Sub

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles TextBox1.TextChanged

    End Sub

    Private Sub Label3_Click(sender As Object, e As EventArgs) Handles Label3.Click

    End Sub
End Class


Public Class Department
    Public Property Code As String
    Public Property Name As String



    Public Sub New(code As String, name As String)
        Me.Code = code
        Me.Name = name
    End Sub

End Class


Public Class Student
    Public Property Roll As Integer
    Public Property DeptCode As String
    Public Property Name As String
    Public Property Address As String
    Public Property Phone As String



    Public Sub New(roll As Integer, deptCode As String, name As String, address As String, phone As String)
        Me.Roll = roll
        Me.DeptCode = deptCode
        Me.Name = name
        Me.Address = address
        Me.Phone = phone
    End Sub

End Class
