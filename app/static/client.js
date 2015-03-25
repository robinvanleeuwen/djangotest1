$(document).ready(function() {

    $("#id_client_number").autocomplete({
        source: "/client/search/client_number",
        minLength: 1,
        messages: {
            noResults: "",
            results: function() {}
        }
    });
    $("#id_name1").autocomplete({
       source: "/client/search/name1",
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