$(document).ready(function () {
   if ($('#CheckRequestSource').val() == 'FromIndex'){
        $("#All-Module-Section").show();
   }
   else {
        $("#Students-Container").show();
        $("#All-Module-Section").hide();
   }
   $('#Home').click(function() {
        $("#Students-Container").hide();
        $("#All-Module-Section").show();
   });
   var CurrentSession = $('#Session').val();
   $('#CurrentSessionSelected').val(CurrentSession);
   if ($('#Session').change()) {
        var CurrentSession = $('#Session').val();
        $('#CurrentSessionSelected').val(CurrentSession);
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
   $("#AddStudentFormID").submit(function(e){
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
   /*$('.EditStudentDataLink').click(function() {
        alert('Are you sure want to edit these details?');
   });*/
   if ($('#CheckRequestSource').val() == 'FromEditFunction'){
        $("#EditStudentFormDiv").show();
        $("#Students-Container").show();
        $("#All-Module-Section").hide();
        $("#StudentListHeads").hide();
        $(".StudentListRows").hide();
   }
   else {
        $("#EditStudentFormDiv").hide();
   }
   $('#NotificationMsg').delay(5000).fadeOut('slow');

   $('#CancelEditStudent').click(function() {
        if ($('#CheckRequestSource').val() == 'FromEditFunction') {
             $("#EditStudentFormDiv").hide();
             $("#Students-Container").show();
             $("#All-Module-Section").hide();
             $("#StudentListHeads").show();
             $(".StudentListRows").show();
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
});