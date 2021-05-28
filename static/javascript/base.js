$(document).ready(function() {
    $(".sms").click(function() {
        var array = [];
        var remarks=$(this).siblings().each(function(){
            array.push($(this).text())
        });
        title=$(".title").text()
        console.log(array);
        $.ajax({
            url: "/dryout/muni",
            type: "POST",
            dataType: "json",
            data: {
                array:array,
                title:title,
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

$(document).ready(function() {
    // Setup - add a text input to each footer cell
    $('#myTable thead tr').clone(true).appendTo( '#myTable thead' );
    $('#myTable thead tr:eq(1) th').each( function (i) {
        var title = $(this).text();
        // $(this).html( '<input type="text" placeholder="Search '+title+'" style="width: 6rem;" />' );
        $(this).html( '<input type="text" placeholder="Search.."/>' );
        $( 'input', this ).on( 'keyup change', function () {
            if ( table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } );
 
    var table = $('#myTable').DataTable( {
        orderCellsTop: true,
        // fixedHeader: true,
        // "scrollX": true,
            scrollX: true
    } );
} );
