$(document).ready(function () {
   var session_value = $('#Session').val();
   $('#Session').change(function () {
        var get_session_value = $('#Session').val();
        if (session_value != get_session_value) {
            var $form = $('#SessionForm').closest('form');
            $form.find('input[type=submit]').click();
        }
   });
   if ($('#CheckRequestSource').val() == 'FromIndex') {
        $("#All-Module-Section").show();
   }
   else {
        $("#All-Module-Section").hide();
        $("#Students-Container").show();
   }
   $('#Home').click(function() {
        $("#Students-Container").hide();
        $("#All-Module-Section").show();
   });
   var CurrentSession = $('#Session').val();
   $('#RegistrationInWhichSession').val(CurrentSession);
   if ($('#Session').change()) {
        var CurrentSession = $('#Session').val();
        $('#RegistrationInWhichSession').val(CurrentSession);
        $('#current_session_of_students').val(CurrentSession);
   }
   else {
        console.log('Session value not changed');
   }
   $('#StudentClass').change(function() {
        if ($('#StudentClass').val() == '9') {
            $('#CourseType').val('Four Year Program');
        }
        else if ($('#StudentClass').val() == '10') {
            $('#CourseType').val('Three Year Program');
        }
        else if ($('#StudentClass').val() == '11') {
            $('#CourseType').val('Two Year Program');
        }
        else {
            $('#CourseType').val('One Year Program');
        }
   });

   $('#Registeration-number-4').change(function () {
        var RegNo = $('#Registeration-number-4').val();
        var session = $('#Session').val();
        $.ajax({
        url: "/check_reg_no_availability/",
        /*url: '/result/',*/
        type: 'GET',
        data: {
            'Reg_No': RegNo,
            'Session': session
        },
        dataType: 'json',
        success: function (RegCheck) {
            if (RegCheck.is_taken) {
                alert("Registration number is already exists!");
            }
        },
        error: function (RegCheck){
                console.log("oops something went wrong!");
            }
       });
   });

    $('#StudentEditRegNo').change(function () {
        var RegNo = $('#StudentEditRegNo').val();
        var session = $('#Session').val();
        $.ajax({
        url: "/check_reg_no_availability/",
        /*url: '/result/',*/
        type: 'GET',
        data: {
            'Reg_No': RegNo,
            'Session': session
        },
        dataType: 'json',
        success: function (RegCheck) {
            if (RegCheck.is_taken) {
                alert("Registration number is already exists!");
            }
        },
        error: function (RegCheck){
                console.log("oops something went wrong!");
            }
       });
   });

   $("#AddStudentFormID").submit(function(e){
        var form = $(this).closest("form");
        if ($('#DiscountOnSessionFee').val().length != 0 && $('#RemarkForDiscount').val().length == 0) {
            alert("You have provided discount to this student and not provided the remark for it!");
            e.preventDefault(e);
        }
        else if ($('#DiscountOnSessionFee').val().length == 0 && $('#RemarkForDiscount').val().length != 0){
            alert("You have provided remark to this student and but not provided the discount to this student!");
            e.preventDefault(e);
        }
        else {
            console.log('form submitted successfully!')
        }
   });
   if ($('#CheckRequestSource').val() == 'FromEditFunction'){
        $("#EditStudentFormDiv").show();
        $("#Students-Container").show();
        $("#All-Module-Section").hide();
        $(".students_table_class").hide();
   }
   else {
        $("#EditStudentFormDiv").hide();
   }
   $('#NotificationMsg').delay(5000).fadeOut('slow');

   $('#CancelEditStudent').click(function() {
        if ($('#CheckRequestSource').val() == 'FromEditFunction') {
             $('#EditStudentForm')[0].reset();
        }
        else {
            console.log('You have not clicked on cancel button!');
        }
   });
   if ($('#CheckRequestSource').val() == 'UpdateDetailFunc'){
        $('#EditStudentForm')[0].reset();
   }
   else {
        console.log('This is not UpdateDetailFunc!');
   }
   $('#search').keyup(function(){
     search_table($(this).val());
   });
   function search_table(value){
       $('#student_table tr').each(function(){
          var found = 'false';
          $(this).each(function(){
              if($(this).text().toLowerCase().indexOf(value.toLowerCase()) >= 0)
              {
                  found = 'true';
              }
          });
          if(found == 'true')
          {
              $(this).show();
              $('#table_head').show();
          }
          else
          {
              $(this).hide();
              $('#table_head').show();
          }
     });
   }

   $('#promote_students_main_checkbox').click(function() {
        if ($(this).is(':checked')) {
            $('.promote_students_checkboxes').attr('checked', true);
        }
        else {
            $('.promote_students_checkboxes').attr('checked', false);
        }
   });
});


