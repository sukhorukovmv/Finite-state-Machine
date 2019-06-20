function createTable(size) {
    var table = $('<table class="table  table-bordered"></table>'); //.addClass('foo');
    var sizeWithNodes = Number(size) + 1;
    for(var i = 0; i < sizeWithNodes; i++){
        var row = $('<tr></tr>');//.text('result ' + i);
        for(var j = 0; j < sizeWithNodes; j++){
            var element = $('<td></td>').append('<input class="form-control" type="text" value=0>');//.text("result" + j + i); //append(input id ij)
            row.append(element);
        }
        table.append(row);
    }
    return table;
}

function step(num) {
    var i = 0;
    while (Math.pow(++i, 2) != num);
    return i;
}

function createNodesDictionary(arr) {
    step = Number(step(arr.length));
    var dict = {}; 
    //метод который должен вернуть json строку , после она должна передаваться на back
    for (var i = step; i < arr.length; i = i + step){
        dict[arr[i]] = null;
        var d = {};
        for (var j = 1; j < step; j++){
            if (arr[i + j] != 0){
                d[arr[j]] = arr[i + j];
                dict[arr[i]] = d;
            }   
        }
    }
    return dict;
}

//считывает и строит граф, наверное стоит назвать create graph
function readTable(table) {
    var arr = [];
    return function() {
        table.each(function(row){
            $(this).find('td').each(function(cell){
                arr.push($(this).children().val()); //происходит считывание таблицы в массив
            });
        });

        nodesDictionary = createNodesDictionary(arr);

        console.log(JSON.stringify(nodesDictionary));


       $.ajax({
            url: '/_create_picture',
            dataType: 'html', //тип данных с сервера
            type: 'POST',
            contentType: "application/json; charset=utf-8", //устанавливается как часть заголовка, для большей информативности на стороне сервера
            data: JSON.stringify(nodesDictionary),
            success: function(){
                  //$('#picture').prepend('<img src="{{url_for('static', filename='img/result.png')}}" />')
 //                 $('#picture').append('<img src="/static/img/result.png" />')
                  
                
                  $('#picture').load('/_draw_picture')

            }
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
        field.append('<input class="btn btn-success btn-sm" style="margin-top: 20px" type="button" value="Построить граф" id="createGraph"/>');
        //работа с динамически созданным объектом, field это родитель динамически добавленного объекта, createGraph это динамически добавленный объект
        field.on('click', '#createGraph', readTable(table));
    });
});
