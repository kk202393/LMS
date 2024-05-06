// ---------  -----------------------//
$("#Preclosure_Amount_add").click(function (event) {
  var custId = $(this).val();
  event.preventDefault();
  $.ajax({
    type: "GET",
    url: "/Preclosure_Amount",
    data: {
      cust_Id: custId,
    },
    success: function (data) {
      console.log(data.error)
      if (data.error) {
        Swal.fire({
          icon: "error",
          title: "Oops...",
          text: data.error,
        });
      } else {
        const Preclosure_Amount_Lable_Handler = document.getElementById(
          "Preclosure_Amount_add"
        ).innerHTML;
        LPF = Number((data.amount) * (data.LPF))
        LPC = Number((data.amount) * (data.LPC))
        console.log(data.pre_closure_loanID);
        netDisburseAmount = Number(data.amount) - (LPF + LPC + data.preclosureAmount)
        var selectElement = document.getElementById("Loan_Mode_id");
        var newOption = document.createElement("option");
        if (Preclosure_Amount_Lable_Handler !== "Remove Preclosure Amount") {
          document.getElementById("Preclosure_Amount_div").value = Math.round(data.preclosureAmount);
          document.getElementById("Net_Pay_Amount").value = Math.round(netDisburseAmount);
          document.getElementById("pre_closure_loanID").value = data.pre_closure_loanID;
          document.getElementById("Preclosure_Amount_add").innerHTML =
            "Remove Preclosure Amount";
          while (selectElement.options.length > 0) {
            selectElement.remove(0);
          }
          newOption.value = data.formStatus;
          newOption.text = `${data.form_status_name} with PreClose`;
          selectElement.appendChild(newOption);
        } else {
          while (selectElement.options.length > 0) {
            selectElement.remove(0);
          }
          newOption.value = 0;
          newOption.text = `Disbursement`;
          selectElement.appendChild(newOption);
          document.getElementById("Preclosure_Amount_div").value = Math.round(data.preclosureAmount);
          document.getElementById("Net_Pay_Amount").value = Number(data.amount) - (LPF + LPC);
          document.getElementById("Preclosure_Amount_add").innerHTML =
            "Add Preclosure Amount";
        }
      }

      
      // $("#Net_Pay_Amount").val(Net_Pay_Amount);
    },
  });
});

// ---------  -----------------------//
