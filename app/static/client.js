$(document).ready(function() {
    field_id = $(this).attr("id");

    $("#id_client_number, #id_name1").autocomplete({

        source: function(request, callback){
            $.getJSON("/client/search/"+this.element[0].id.substring(3), { term: request.term }, callback);
        },
        minLength: 1,
        messages: {
            noResults: "",
            results: function() {}
        }
    });


    $("#id_client_number").focusout(function() {
        client_data = $.getJSON("/client/get/"+$("#id_client_number").val())

    });

});