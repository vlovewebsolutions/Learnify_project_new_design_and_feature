$(document).ready(function () {
   $('#SelectAllResult').click(function() {
        if ($(this).is(':checked')) {
            $('.CheckedResult').attr('checked', true);
        }
        else {
            $('.CheckedResult').attr('checked', false);
        }
    });
   $('#NotificationMsg').delay(5000).fadeOut('slow');
   $('#Session').change(function() {
        var form = $(this).closest("form");
        var result = $('#ResultNames').val();
        var session = $('#Session').val();
        $('#CurrentSessionSelected').val(session);
        $('#ResultTable tbody > tr'). remove();
        output = "";
        $.ajax({
        url: form.attr("filter-data-on-session-basis"),
        /*url: '/result/',*/
        data: {
            'Result_Name': result,
            'Session': session
        },
        dataType: 'json',
        success: function (data) {
            console.log(data.student_data);
            x = data.student_data;
            if (data.student_data) {
                for (i=0; i<x.length; i++) {
                    output += "<tr><td><input type='checkbox' name='RESULT[]' value="+ y[i].StuRegNo +" class='CheckedResult'></td>" + "<td>" + x[i].StuRegNo + "</td><td>" +
                    x[i].StuRegDate + "</td><td>" + x[i].StuName + "</td><td>" +
                    x[i].CourseType + "</td><td>" + x[i].Physics_MARKS + "</td><td>" + x[i].Chemistry_MARKS +
                    "</td><td>" + x[i].Maths_MARKS + "</td><td>" + x[i].BIO_MARKS + "</td><td>"+ x[i].MAT_MARKS +"</td><td>"
                     + x[i].SST_MARKS + "</td><td>" + x[i].TOTAL_MARKS + "</td><td>" + x[i].Overall_RANK + "</td>";
                }
                $('#tbody').html(output);
            }
            else if (x == 'None'){
                alert("There is no result!");
            }
        },
        error: function (data){
            alert("Please select result from dropdown box!");
        }
      });
   });
   $('#ResultNames').change(function() {
        var result = $('#ResultNames').val();
        var session = $('#Session').val();
        var session = $('#Session').val();
        $('#CurrentSessionSelected').val(session);
        $('#ResultTable tbody > tr'). remove();
        outputResult = "";
        $.ajax({
        url: '/Filter_objects_on_result_name_basis/',
        data: {
            'Result_Name': result,
            'Session': session
        },
        dataType: 'json',
        success: function (StuData) {
            console.log(StuData.student_data);
            y = StuData.student_data;
            if (StuData.student_data) {
                for (i=0; i<y.length; i++) {
                    outputResult += "<tr><td><input type='checkbox' name='RESULT[]' value="+ y[i].StuRegNo +" class='CheckedResult'></td>" + "<td>" + y[i].StuRegNo + "</td><td>" +
                    y[i].StuRegDate + "</td><td>" + y[i].StuName + "</td><td>" +
                    y[i].CourseType + "</td><td>" + y[i].Physics_MARKS + "</td><td>" + y[i].Chemistry_MARKS +
                    "</td><td>" + y[i].Maths_MARKS + "</td><td>" + y[i].BIO_MARKS + "</td><td>"+ y[i].MAT_MARKS +"</td><td>"
                     + y[i].SST_MARKS + "</td><td>" + y[i].TOTAL_MARKS + "</td><td>" + y[i].Overall_RANK + "</td>";
                }
                $('#tbody').html(outputResult);
            }
            else if (y == 'None'){
                alert("There is no result!");
            }
        },
        error: function (StuData){
            alert("Please select result from dropdown box!");
        }
      });
   });
});