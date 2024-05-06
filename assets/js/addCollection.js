// --------- Region wise Branch start -----------------------//
$("#numberOfEMI").change(function () {
    var Product = $(this).val();
    // console.log(Product);
    $.ajax({
        type: "GET",
        url: "/emiAmount",
        data: {
            no_of_emi: Product
        },
        success: function (amount,id) {
            console.log(amount);
            console.log(id);
            $("#collectedAmount").html(amount);
        }
    })
});

// --------- Region wise Branch start -----------------------/