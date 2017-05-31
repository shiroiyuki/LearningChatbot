var table = document.createElement("table");
table.style.border = "1px solid #000000";
var table_body = document.createElement("tbody");
var test=document.createElement("thead");
test.style.border ="1px solid #000000";
var aa=document.createElement("tr");
aa.style.border ="1px solid #000000";
var bb=document.createElement("th");
bb.style.border ="1px solid #000000";
var cc=document.createElement("th");
cc.style.border ="1px solid #000000";
bb.appendChild(document.createTextNode("商店"));
cc.appendChild(document.createTextNode("營業時間"));
aa.appendChild(bb);
aa.appendChild(cc);
for (var i = 0; i < restaurants.length; ++i) {
    var row = document.createElement("tr");
    for (key in restaurants[i]) {
        var cell = document.createElement("td");
        cell.appendChild(document.createTextNode(restaurants[i][key]));
		cell.style.border = "1px solid #000000";
        row.appendChild(cell);
    }
	console.log(restaurants[i].name);
    table_body.appendChild(row);
}
test.appendChild(aa);
table.appendChild(test);
table.appendChild(table_body);
document.body.appendChild(table);