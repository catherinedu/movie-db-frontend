for(i = 0; i < data.length; i++){
	if(data[i]["Id"] == item_id){
		var item = data[i]
		break
	}
}

console.log(item)

var display_item = function(item){
	var dl = $("<dl class='row'>")
	var text_title = "Title"
	var title = $("<dt class='col-sm-3'> "+text_title+" </dt> ")
	$(dl).append(title)
	var text_1 = item["Title"]
	var des_title = $("<dd class='col-sm-9'>  "+text_1+"  </dd>")
	$(dl).append(des_title)

	var text_year = "Year"
	var year = $("<dt class='col-sm-3'> "+text_year+" </dt> ")
	$(dl).append(year)
	var text_2 = item["Year"]
	var des_year = $("<dd class='col-sm-9'>  "+text_2+"  </dd>")
	$(dl).append(des_year)

	var text_poster = "Poster"
	var poster = $("<dt class='col-sm-3'> "+text_poster+" </dt> ")
	$(dl).append(poster)
	var text_3 = item["Poster"]
	var des_poster = $("<dd class='col-sm-9'>  </dd>")
	var image = $("<img src="+text_3+" width='200'>  ")
	$(des_poster).append(image)
	$(dl).append(des_poster)

	var text_sum = "Summary"
	var summary = $("<dt class='col-sm-3'> "+text_sum+" </dt> ")
	$(dl).append(summary)
	var text_4 = item["Summary"]
	var des_sum = $("<dd class='col-sm-9'>  "+text_4+"  </dd>")
	$(dl).append(des_sum)

	var text_dir = "Director"
	var director = $("<dt class='col-sm-3'> "+text_dir+" </dt> ")
	$(dl).append(director)
	var text_5 = item["Director"]
	var des_dir = $("<dd class='col-sm-9'>  "+text_5+"  </dd>")
	$(dl).append(des_dir)

	var text_bud = "Budget"
	var budget = $("<dt class='col-sm-3'> "+text_bud+" </dt> ")
	$(dl).append(budget)
	var text_6 = item["Budget"]
	var des_bud = $("<dd class='col-sm-9'>  "+text_6+"  </dd>")
	$(dl).append(des_bud)

	var text_run = "Runtime"
	var runtime = $("<dt class='col-sm-3'> "+text_run+" </dt> ")
	$(dl).append(runtime)
	var text_7 = item["Runtime"]
	var des_run = $("<dd class='col-sm-9'>  "+text_7+"  </dd>")
	$(dl).append(des_run)

	var text_score = "Score"
	var score = $("<dt class='col-sm-3'> "+text_score+" </dt> ")
	$(dl).append(score)
	var text_8 = item["Score"]
	var des_score = $("<dd class='col-sm-9'>  "+text_8+"  </dd>")
	$(dl).append(des_score)


	var text_mp = "MPAA"
	var mpaa = $("<dt class='col-sm-3'> "+text_mp+" </dt> ")
	$(dl).append(mpaa)
	var text_9 = item["MPAA"]
	var des_mp = $("<dd class='col-sm-9'>  "+text_9+"  </dd>")
	$(dl).append(des_mp)



	$("#item").append(dl)

	
}



$(document).ready(function(){
	display_item(item)
});
