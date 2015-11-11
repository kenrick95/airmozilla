$(function() {
    'use strict';
    // all the things we're going to do select2 on,
    // explicitely make sure they're 100%
    $('#id_timezone').css('width', '100%');

    $('#id_timezone').select2();

    // Autofill template environments
    $('#id_template').change(function() {
        var selected = $('#id_template').val();
        if (selected) {
            $.getJSON('/manage/templates/env-autofill/',
                {'template': selected},
                function(data) {
                    $('#id_template_environment').val(data.variables);
                }
            );
        }
    });
});
