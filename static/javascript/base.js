$(document).ready(function() {
    $(".sms").click(function() {
        var remarks=$(this).siblings(".remarks").text();
        var roName=$(this).siblings(".roName").text();
        var SalesOrder=$(this).siblings(".SalesOrder").text();
        var MobileNumber=$(this).siblings(".MobileNumber").text();
        console.log(remarks);
        $.ajax({
            url: "/muni",
            type: "POST",
            dataType: "json",
            data: {
                RoName:roName,
                SO:SalesOrder,
                remark:remarks,
                MobileNumber:MobileNumber,
                csrfmiddlewaretoken: window.CSRF_TOKEN
                },
            success : function(json) {
                alert("sms sent.")
                // alert("Successfully sent the URL to Django");
                // window.location.replace('http://take-me-somewhere');
            },
            error : function(xhr,errmsg,err) {
                alert("error: "+err);
                // alert("Could not send URL to Django. Error: " + xhr.status + ": " + xhr.responseText);
            }
        });
    });  
});
$(document).ready(function() {
    $(".delete").click(function() {
        $(this).parent().remove();
    });
});

// $(document).ready(function() {
//     $(".sms").click(function() {
//         alert("sms sent")
//     });
// });


function Filterfun() {
         //Declare needed variables
    var doname,rocode,roname,product,donameFilter,rocodeFilter,ronameFilter,productFilter,table,tr,td_do,td_rocode,td_roname,td_product,i;
    //Set inputs by getElementById
    doname = document.getElementById('doname');
    rocode = document.getElementById('rocode');
    roname = document.getElementById('roname');
    product = document.getElementById('product');
    //Set filters
    donameFilter = doname.value.toUpperCase();
    rocodeFilter = rocode.value.toUpperCase();
    ronameFilter = roname.value.toUpperCase();
    productFilter = product.value.toUpperCase();
    //Set the table and tr variables
    table = document.getElementById("myTable");
    tr = document.getElementsByTagName("tr");

    //Loop through items and hide those that don't match the query -->
    for (i = 0; i < tr.length; i++) {
        td_do = tr[i].getElementsByTagName("td")[0];
        td_rocode = tr[i].getElementsByTagName("td")[1];
        td_roname = tr[i].getElementsByTagName("td")[2];
        td_product = tr[i].getElementsByTagName("td")[3];
        if(td_do&&td_rocode&&td_roname&&td_product){
        if (td_do.innerHTML.toUpperCase().indexOf(donameFilter) > -1 && td_rocode.innerHTML.toUpperCase().indexOf(rocodeFilter) > -1 
        && td_roname.innerHTML.toUpperCase().indexOf(ronameFilter) > -1&& td_product.innerHTML.toUpperCase().indexOf(productFilter) > -1) {
            tr[i].style.display = "";
        }
        else {
            tr[i].style.display = "none";
        }
    }
    }
}


