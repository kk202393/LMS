// --------- Region wise Branch start -----------------------//
$("#id_branch_Name").change(function () {
    var branchID = $(this).val();
    // console.log(Product);
    $.ajax({
      type: "GET",
      url: "/agent_branch",
      data: {
        BranchID: branchID,
      },
      success: function (data) {
        $("#id_agents_Name").html(data);
      },
    });
  });
  
  // --------- Region wise Branch start -----------------------//