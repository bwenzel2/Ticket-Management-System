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
    $('#ticketDetailTitle').html("Ticket #" + ticketid);

    //get the ticket info via an AJAX call
    $.ajax({
        url: '/get_ticket_details/',
        data: {
            ticket_id: ticketid
        },
        success: function (result) {
            //alert('Successful' + JSON.stringify(result));

            //location
            var location = result[0].fields.location;
            $('#location_detail').val(location);

            //requestor
            var requestor = result[0].fields.requestor;
            $('#requestor_detail').val(requestor);

            //recipient
            var recipient = result[0].fields.recipient;
            $('#recipient_detail').val(recipient);

            //description
            var description = result[0].fields.description;
            $('#detail_description').text(description);

            var urgency_int = result[0].fields.urgency;
            var urgency_string;
            if (urgency_int == 1) {
                urgency_string = "High";
            } else if (urgency_int == 2) {
                urgency_string = "Medium";
            } else if (urgency_int == 3) {
                urgency_string = "Low";
            }

            $('#urgency_detail').html(urgency_string);
        },
        error: function (status) {
            alert('Error: ' + JSON.stringify(status));
        }
    });

    //get all updates associated with the ticket via an AJAX call
    $.ajax({
        url: '/get_updates/',
        data: {
            ticket_id: ticketid
        },
        success: function (result) {
            $('#detail_activity_log').empty();
            result.forEach(function (arrayItem) {
                $('#detail_activity_log').append('<li class="list-group-item">' + "UPDATE: " + arrayItem.fields.creation_date + "<br>" + arrayItem.fields.description + '</li>');
            });
            //alert('Success' + JSON.stringify(result));
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
    var ticketid = $('#ticketDetailTitle').text().split('#')[1];
    $.ajax({
        url: '/new_update/',
        type: 'POST',
        data: {
            //TODO: GET THE RIGHT TICKET ID
            ticket_id: ticketid,
            description: document.getElementById('update_text').value
        },
        success: function (result) {
            // alert('Success' + JSON.stringify(result));
            // add the new alert at the top of the activity log
            $('#detail_activity_log').prepend('<li class="list-group-item">' + "UPDATE: " + result[0].fields.creation_date + "<br>" + result[0].fields.description + '</li>');
        },
        error: function (status) {
            alert('Error: ' + JSON.stringify(status));
        }
    });

    //reset update text input field value
    document.getElementById('update_text').value = "";
}
