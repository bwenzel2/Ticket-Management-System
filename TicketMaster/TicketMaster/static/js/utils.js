var table = document.getElementsByTagName("table")[0];
var tbody = table.getElementsByTagName("tbody")[0];
tbody.onclick = function (e) {
    e = e || window.event;
    var data = [];
    var target = e.srcElement || e.target;
    while (target && target.nodeName !== "TR") {
        target = target.parentNode;
    }
    var ticketid;
    if (target) {
        var cells = target.getElementsByTagName("td");
        ticketid = cells[0].innerHTML;
    }
    $('#desc').html("Ticket id: " + ticketid);

    //get the ticket info via an AJAX call
    $.ajax({
        url: '/get_ticket_details/',
        data: {
            ticket_id: ticketid
        },
        success: function (result) {
            //alert('Success' + JSON.stringify(result));
            var description = result[0].fields.description;
            $('#desc').html("Ticket description: " + description);
        },
        error: function (status) {
            alert('Error: ' + JSON.stringify(status));
        }
    });

    //show the ticket info in the modal
    $('#ticketDetailModal').modal('show');

};


function addUpdate() {
    //Django CSRF setup for the POST request
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
            }
        }
    });

    //send the AJAX POST request
    $.ajax({
        url: '/new_update/',
        type: 'POST',
        data: {
            //TODO: GET THE RIGHT TICKET ID
            ticket_id: 4,
            description: document.getElementById('update_text').value
        },
        success: function (result) {
            alert('Success' + JSON.stringify(result));
        },
        error: function (status) {
            alert('Error: ' + JSON.stringify(status));
        }
    });
}
