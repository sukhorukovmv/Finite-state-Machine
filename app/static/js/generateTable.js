function createTable(size) {
    var table = $('<table class="table"></table>'); //.addClass('foo');
    var sizeWithNodes = Number(size) + 1;
    for(var i = 0; i < sizeWithNodes; i++){
        var row = $('<tr></tr>');//.text('result ' + i);
        for(var j = 0; j < sizeWithNodes; j++){
            var element = $('<td></td>').append('<input type="text" value=0>');//.text("result" + j + i); //append(input id ij)
            row.append(element);
        }
        table.append(row);
    }
    return table;
}

//считывает и строит граф, наверное стоит назвать create graph
function readTable(table) {
    return function() {
        table.each(function(row){
            $(this).find('td').each(function(cell){
                console.log($(this).children().val());
            });
        });
    };
}

$(document).ready(function(){
    var her = $("h2");
    her.css("color", "red"); 
    var field = $('#content');
    var table = $('#table');
    var butCreateTable = $("#createTable");
    var butCreateGraph = $("#createGraph");
    butCreateTable.on('click', function () {
        var countNodes = $("#countNodes").val();
        table.html(createTable(countNodes));

        //добавление кнопки после построения таблицы под ввод
        field.append('<input type="button" value="CreateGraph" id="createGraph"/>');
        //работа с динамически созданным объектом, field это родитель динамически добавленного объекта, createGraph это динамически добавленный объект
        field.on('click', '#createGraph', readTable(table));
    });
});
