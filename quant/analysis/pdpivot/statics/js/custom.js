var _fields;
function init_fields(data){
    _fields = data;
    for (var i = 0; i < data.length; ++i) {
        var item = data[i];
        var name = item['name'], type = item['type'];
        if (type == 'category') {
            var unique = item['unique'];
            var html = '<li class="' + type + '" id="' + name + '"><a href="#">' + name + '</a>';
            html += '<select id="filter-' + name + '" class="selectpicker" data-width="10px" multiple>\n';
            for (var j = 0; j < unique.length; j ++) {
                html += '<option>' + unique[j] + '</option>\n';
            }
            html += '</select></li>\n';
            $('#idle-fields').append(html);
        } else {
            $('#idle-fields').append('<li class="' + type + '" id="' + name + '"><a href="#">' + name + '</a></li>\n');
        }
    }
}

function get_fields(selector){
    var data = '';
    var lis = $(selector + '>li>a');
    lis.each(function(i){
        data += '|' + lis.eq(i).text();
    });
    return data
}

function get_filters(){
    var filters = '';
    for (var i = 0; i < _fields.length; i++) {
        var item = _fields[i];
        var name = item['name'], type = item['type'];
        if (type != 'category') continue;
        var selected = $('.selectpicker#filter-' + name).val();
        if (selected == false) continue;
        for (var j = 0; j < selected.length; j++) {
            if (selected[j] == false) continue;
            filters += '|' + name + ':' + selected[j];
        }
    }
    return filters;
}

function refresh_table(){
    var columns = get_fields('.fields#columns'),
        values  = get_fields('.fields#values'),
        index   = get_fields('.fields#index');
    var method = $("#aggfunc>option:selected").val();
    var filters = get_filters();
    Backend.refresh_table(columns, index, values, method, filters);
}
$(function(){
    $("#index, #columns, #idle-fields, #values").sortable({
        'connectWith': '.fields',
        'update': function(event, ui){
            refresh_table();
        },
        'cancel': 'input, textarea, button'
    }).disableSelection();
    $("#index, #columns").on("sortreceive", function(event, ui){
        if ($(ui.item[0]).hasClass("numeric")){
            $(".fields").sortable("cancel");
        }
    });
    $("#aggfunc").change(refresh_table);
    $('[id^="filter"]').each(function(i){
        $('[id^="filter"]')[i].addEventListener('changed.bs.select', refresh_table);
    });
});
$(function(){
    Backend.get_fields();
    refresh_table();
});