var submit_item = function(){
	console.log(data)
	var title = $("#enter_title").val()
	var year = $("#enter_year").val()
	var image_link = $("#enter_image_link").val()
	var summary = $("#enter_summary").val()
	var director = $("#enter_director").val()
	var budget = $("#enter_budget").val()
	var runtime = $("#enter_runtime").val()
	var score = $("#enter_score").val()
	var mpaa = $("#enter_MPAA").val()

	var new_item = {
		"Title": title,
		"Year": year,
		"Poster": image_link,
		"Summary": summary,
		"Director": director,
		"Budget": budget,
		"Runtime": runtime,
	 	"Score": score,
	 	"MPAA": mpaa
	}
	save_item(new_item)


}



var save_item = function(new_item){
	var item_to_add = {
		"Title": new_item["Title"],
		"Year": new_item["Year"],
		"Poster": new_item["Poster"],
		"Summary": new_item["Summary"],
		"Director": new_item["Director"],
		"Budget": new_item["Budget"],
		"Runtime": new_item["Runtime"],
	 	"Score": new_item["Score"],
	 	"MPAA": new_item["MPAA"]

	}
	$.ajax({
		type: "POST",
		url: "save_item",
		datatype: "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(item_to_add),
        success: function(result){
            var all_data = result["data"]
            data = all_data
            console.log(data)
            item_id = data[0]["Id"]
           	display_to_user(item_id)
            
        },
        error: function(request, status, error){
        	alert("Operation Unsuccessful")
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }

	})



}

var display_to_user = function(item_id){
	var text = "Link to movie"
	var text2 = "Operation Successful"
	var message = "<h3> "+text2+" </h3>"
	var link = "<a href='/item/"+item_id+"'> "+text+" </a>"
	$("#display").append(message)
	$("#display").append(link)

}


$(document).ready(function(){
      $("#submit_item").click(function(){
           submit_item()
      })
});
















