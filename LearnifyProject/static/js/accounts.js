$(document).ready(function () {
    $('#FeeCollectionFormParentDiv').hide();
    $('.sessiondropdowndiv').show();
    if ($("#RequestComingFrom").val() == 'CollectFeePage') {
        $('#StudentFeeDetailTableDiv').hide();
        $('.sessiondropdowndiv').hide();
        $('#FeeCollectionFormParentDiv').show();
    }
    $("#FeeCollectionFormCancelBtn").click(function () {
        window.location.href='/Accounts/';
    });

    $('#FeeCollectionForm').submit(function (e) {
        var get_session_value = $('#Session').val();
        $('#FeesForSession').val(get_session_value);
    });

    var session_value = $('#Session').val();
    $('#Session').change(function () {
        var get_session_value = $('#Session').val();
        if (session_value != get_session_value) {
            var $form = $('#SessionForm').closest('form');
            $form.find('input[type=submit]').click();
        }
    });

    $('#ReceiptNumberInput_ID').change(function () {
        var receipt_number = $('#ReceiptNumberInput_ID').val();
        $.ajax({
            url: '/check_receipt_no_availability/',
            type: 'GET',
            data: {
                'RECEIPT_NO': receipt_number,
            },
            dataType: 'json',
            success: function (CheckReceiptNo) {
                if (CheckReceiptNo.is_taken) {
                    alert('This receipt number is already allocated!');
                }
            },
            error: function (CheckReceiptNo) {
                console.log('Receipt number is unique :)');
            }
        });
    });

    $("#FeeCollectionForm").submit(function (e) {
        var amount_receiving = parseInt($("#AmountReceivingInputId").val());
        var student_due_fee = parseInt($("#StudentDueFees").val());
        if (amount_receiving > student_due_fee) {
            alert("Amount is more than the students due fee!");
            e.preventDefault();
        }
        else if (amount_receiving <= 0) {
            alert("Please enter valid amount value!");
            e.preventDefault();
        }
        else {
            console.log("Fee collected successfully!");
        }
    });
    $('#EditStudentFeeReceiptsParentDiv').hide();
    $('#NotificationMsg').delay(5000).fadeOut('slow');
    $("#cashRadio").prop('checked', true);
    $("#PaymentByCheque").hide();
    $('#cashRadio').click(function () {
        $("#PaymentByCheque").hide();
        $("#chequeRadio").prop('checked', false);
        $("[name='BankName']").attr("required", false);
        $("[name='ChequeNumber']").attr("required", false);
    });
    $('#chequeRadio').click(function () {
        $("#PaymentByCheque").show();
        $("#cashRadio").prop('checked', false);
        $("[name='BankName']").attr("required", true);
        $("[name='ChequeNumber']").attr("required", true);
    });
    var gst = $('#GstOnFee').val();
    var grand_total_of_four_year_program = parseInt($('#SessionOneFee').val()) + parseInt($('#SessionTwoFee').val()) + parseInt($('#SessionThreeFee').val()) + parseInt($('#SessionFourFee').val());
    $('#GrandTotalOfFourYearProgram').text(grand_total_of_four_year_program + grand_total_of_four_year_program*gst);
    var grand_total_of_three_year_program = parseInt($('#SessionTwoFee').val()) + parseInt($('#SessionThreeFee').val()) + parseInt($('#SessionFourFee').val());
    $('#GrandTotalOfThreeYearProgram').text(grand_total_of_three_year_program + grand_total_of_three_year_program*gst);
    var grand_total_of_two_year_program = parseInt($('#SessionThreeFee').val()) + parseInt($('#SessionFourFee').val());;
    $('#GrandTotalOfTwoYearProgram').text(grand_total_of_two_year_program + grand_total_of_two_year_program*gst);

    $('#search').keyup(function(){
     search_table($(this).val());
    });
    function search_table(value){
       $('#StudentFeeReceiptsTable tr').each(function(){
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
   $('#searchFeeDetail').keyup(function(){
     search_table_fee_detail($(this).val());
   });
   function search_table_fee_detail(value){
       $('#StudentFeeDetailTable tr').each(function(){
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
              $('#table_head_fee_detail').show();
          }
          else
          {
              $(this).hide();
              $('#table_head_fee_detail').show();
          }
     });
   }
});