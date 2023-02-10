Public Class Form1

    Private depts As New List(Of Department) From {
        New Department("CSE", "Computer Science"),
        New Department("IT", "Information Technology"),
        New Department("ECE", "Electronics and Communications"),
        New Department("MECH", "Mechanical Engineering")
    }

    Private students As New List(Of Student)

    Private currentPage As Integer = 1
    Private pageSize As Integer = 4


    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        cbDept.DataSource = depts
        cbDept.DisplayMember = "Name"
        cbDept.ValueMember = "Code"
        UpdateDataGrid()



    End Sub

    Private Sub Label1_Click(sender As Object, e As EventArgs) Handles Label1.Click

    End Sub

    Private Sub Label2_Click(sender As Object, e As EventArgs) Handles Label2.Click

    End Sub

    Private Sub TextBox1_TextChanged(sender As Object, e As EventArgs) Handles txtName.TextChanged

    End Sub

    Private Sub Label3_Click(sender As Object, e As EventArgs) Handles Label3.Click

    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles btnEdit.Click
        Dim roll As Integer = CInt(txtSearchRoll.Text)
        Dim student As Student = students.Find(Function(s) s.Roll = roll)
        If student IsNot Nothing Then
            student.DeptCode = CStr(cbDept.SelectedValue)
            student.Name = txtName.Text
            student.Address = txtAddress.Text
            student.Phone = txtPhone.Text
            MessageBox.Show("Student edited successfully.")
            UpdateDataGrid()
        Else
            MessageBox.Show("No student found with this roll number.")
        End If


    End Sub

    Private Sub btnDelete_Click(sender As Object, e As EventArgs) Handles btnDelete.Click
        Dim roll As Integer = CInt(txtSearchRoll.Text)
        Dim student As Student = students.Find(Function(s) s.Roll = roll)

        If student IsNot Nothing Then
            students.Remove(student)
            MessageBox.Show("Student deleted successfully.")
            UpdateDataGrid()
        Else
            MessageBox.Show("No student found with this roll number.")
        End If
    End Sub

    Private Sub ListBox1_SelectedIndexChanged(sender As Object, e As EventArgs) Handles cbDept.SelectedIndexChanged

    End Sub

    Private Sub btnSave_Click(sender As Object, e As EventArgs) Handles btnSave.Click

        Dim roll As Integer = CInt(txtRoll.Text)
        Dim deptCode As String = CStr(cbDept.SelectedValue)
        Dim name As String = txtName.Text
        Dim address As String = txtAddress.Text
        Dim phone As String = txtPhone.Text

        If Not students.Exists(Function(s) s.Roll = roll) Then
            students.Add(New Student(roll, deptCode, name, address, phone))
            MessageBox.Show("Student added successfully.")
        Else
            MessageBox.Show("A student with this roll number already exists.")
        End If

        UpdateDataGrid()
        ClearInputFields()


    End Sub

    Private Sub UpdateDataGrid()
        Dim startIndex As Integer = (currentPage - 1) * pageSize
        Dim endIndex As Integer = startIndex + pageSize

        If endIndex > students.Count Then
            endIndex = students.Count
        End If

        dgvStudents.DataSource = students.GetRange(startIndex, endIndex - startIndex)
        dgvStudents.DisplayMember = "Name"
        btnPrev.Enabled = currentPage > 1
        btnNext.Enabled = (currentPage * pageSize) < students.Count
    End Sub

    Private Sub ClearInputFields()
        txtRoll.Text = ""
        cbDept.SelectedIndex = -1
        txtName.Text = ""
        txtAddress.Text = ""
        txtPhone.Text = ""
        txtSearchRoll.Text = ""
    End Sub

    Private Sub dgvStudents_SelectedIndexChanged(sender As Object, e As EventArgs) Handles dgvStudents.SelectedIndexChanged

    End Sub

    Private Sub btnCancel_Click(sender As Object, e As EventArgs) Handles btnCancel.Click
        ClearInputFields()
    End Sub

    Private Sub btnSearch_Click(sender As Object, e As EventArgs) Handles btnSearch.Click
        Dim roll As Integer = CInt(txtSearchRoll.Text)
        Dim student As Student = students.Find(Function(s) s.Roll = roll)

        If student IsNot Nothing Then
            txtRoll.Text = CStr(student.Roll)
            cbDept.SelectedValue = student.DeptCode
            txtName.Text = student.Name
            txtAddress.Text = student.Address
            txtPhone.Text = student.Phone
        Else
            MessageBox.Show("No student found with this roll number.")
        End If
    End Sub

    Private Sub btnPrev_Click(sender As Object, e As EventArgs) Handles btnPrev.Click
        If currentPage > 1 Then
            currentPage -= 1
            UpdateDataGrid()
        End If
    End Sub

    Private Sub btnNext_Click(sender As Object, e As EventArgs) Handles btnNext.Click
        If (currentPage * pageSize) < students.Count Then
            currentPage += 1
            UpdateDataGrid()
        End If
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

