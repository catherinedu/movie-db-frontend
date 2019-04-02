from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


current_id = 30
data = [
	{
		"Id": 1,
		"Title": "Avengers: Infinity War",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjMxNjY2MDU1OV5BMl5BanBnXkFtZTgwNzY1MTUwNTM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
		"Summary": "As the Avengers and their allies have continued to protect the world from threats too large for any one hero to handle, a new danger has emerged from the cosmic shadows: Thanos. A despot of intergalactic infamy, his goal is to collect all six Infinity Stones, artifacts of unimaginable power, and use them to inflict his twisted will on all of reality. Everything the Avengers have fought for has led up to this moment, the fate of Earth and existence has never been more uncertain. Written by Marvel Studios",
		"Director": "Anthony Russo, Joe Russo",
		"Budget": "$321,000,000",
	 	"Score": "8.5",
	 	"Runtime":"149 min",
	 	"MPAA": "PG-13"
	},
	{
		"Id": 2,
		"Title": "Pacific Rim: Uprising",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjI3Nzg0MTM5NF5BMl5BanBnXkFtZTgwOTE2MTgwNTM@._V1_.jpg",
		"Summary": "Jake Pentecost, son of Stacker Pentecost, reunites with Mako Mori to lead a new generation of Jaeger pilots, including rival Lambert and 15-year-old hacker Amara, against a new Kaiju threat.",
		"Director": "Steven S. DeKnight",
		"Budget": "$150,000,000",
		"Runtime": "111 min",
	 	"Score": "5.6",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 3,
		"Title": "Ready Player One",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BY2JiYTNmZTctYTQ1OC00YjU4LWEwMjYtZjkwY2Y5MDI0OTU3XkEyXkFqcGdeQXVyNTI4MzE4MDU@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
		"Summary": "When the creator of a virtual reality world called the OASIS dies, he releases a video in which he challenges all OASIS users to find his Easter Egg, which will give the finder his fortune.",
		"Director": "Steven Spielberg",
		"Budget": "$175,000,000",
		"Runtime": "140 min",
		"Score": "7",
		"MPAA": "PG-13"

	},
	{
		"Id": 4,
		"Title": "Hunter Killer",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BYjRkNzQ0NmYtZmQyMS00Yzk5LWEzZjQtYzhlOTRlMzVjMzA3XkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
		"Summary": "An untested American submarine captain teams with U.S. Navy Seals to rescue the Russian president, who has been kidnapped by a rogue general.",
		"Director": "Donovan Marsh",
		"Budget": "NA",
		"Runtime": "122 min",
	 	"Score": "6.6",
	 	"MPAA": "R"

	},
	{
		"Id": 5,
		"Title": "Hotel Artemis",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMDhhNWE3NmQtY2Y1OC00MzQ4LWJhNjktZWEzNjEzMTE3YWIyXkEyXkFqcGdeQXVyMjM4NTM5NDY@._V1_SY1000_CR0,0,639,1000_AL_.jpg",
		"Summary": "Set in riot-torn, near-future Los Angeles, 'Hotel Artemis' follows the Nurse, who runs a secret, members-only emergency room for criminals.",
		"Director": "Drew Pearce",
		"Budget": "$15,000,000",
		"Runtime": "94 min",
	 	"Score": "6.1",
	 	"MPAA": "R"

	},
	{
		"Id": 6,
		"Title": "Warfighter",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BNmRjOWViMzYtYWQ5Yi00N2E1LTk3NjktNWExNzNhYmIyMTdlXkEyXkFqcGdeQXVyMTM4NjQxNTU@._V1_UY268_CR2,0,182,268_AL_.jpg",
		"Summary": "Rusty Wittenburg is a Navy SEAL struggling to balance his family life and his job. He fights daily to maintain the line between reality and the nightmares his PTSD conjures up for him. Dedicated to his team and his mission, he is willing to give the ultimate sacrifice for his fellow brothers and teammates.",
		"Director": "Jerry G. Angelo",
		"Budget": "NA",
		"Runtime": "105 min",
	 	"Score": "8.8",
	 	"MPAA": "R"

	},
	{
		"Id": 7,
		"Title": "The Marine 6: Close Quarters",
		"Year": "2018",
		"Poster": "https://m.media-amazon.com/images/M/MV5BZDQ3ZmYzYzEtMjg5ZC00YjBkLTk1ZTAtNGM3ZTY1ZDQwMDk4XkEyXkFqcGdeQXVyODgxNzAyMDk@._V1_SY999_CR0,0,802,999_AL_.jpg",
		"Summary": "Jake Carter and another former Marine, Luke Trapper, join forces to rescue a kidnapped girl from a gang of international criminals.",
		"Director": "James Nunn",
		"Budget": "NA",
		"Runtime": "85 min",
	 	"Score": "4.9",
	 	"MPAA": "R"

	},
	{
		"Id": 8,
		"Title": "Alita: Battle Angel",
		"Year": "2019",
		"Poster": "https://m.media-amazon.com/images/M/MV5BNzVhMjcxYjYtOTVhOS00MzQ1LWFiNTAtZmY2ZmJjNjIxMjllXkEyXkFqcGdeQXVyNTc5OTMwOTQ@._V1_.jpg",
		"Summary": "A deactivated female cyborg is revived, but cannot remember anything of her past life and goes on a quest to find out who she is.",
		"Director": "Robert Rodriguez",
		"Budget": "$170,000,000",
		"Runtime": "122 min",
	 	"Score": "7.6",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 9 ,
		"Title": "Star Wars: Episode VIII - The Last Jedi",
		"Year": "2017",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjQ1MzcxNjg4N15BMl5BanBnXkFtZTgwNzgwMjY4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "Rey develops her newly discovered abilities with the guidance of Luke Skywalker, who is unsettled by the strength of her powers. Meanwhile, the Resistance prepares for battle with the First Order.",
		"Director": "Rian Johnson",
		"Budget": "NA",
		"Runtime": "155 min",
	 	"Score": "7.2",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 10 ,
		"Title": "Wonder Woman",
		"Year": "2017",
		"Poster": "https://m.media-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "When a pilot crashes and tells of conflict in the outside world, Diana, an Amazonian warrior in training, leaves home to fight a war, discovering her full powers and true destiny.",
		"Director": "Petty Jenkins",
		"Budget": "$149,000,000",
		"Runtime": "141 min",
	 	"Score": "7.5",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 11,
		"Title": "Guardians of the Galaxy Vol. 2",
		"Year": "2017",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "The Guardians struggle to keep together as a team while dealing with their personal family issues, notably Star-Lord's encounter with his father the ambitious celestial being Ego.",
		"Director": "James Gunn",
		"Budget": "$200,000,000",
		"Runtime": "136 min",
	 	"Score": "7.7",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 12,
		"Title": "Spider-Man: Homecoming",
		"Year": "2017",
		"Poster": "https://m.media-amazon.com/images/M/MV5BNTk4ODQ1MzgzNl5BMl5BanBnXkFtZTgwMTMyMzM4MTI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "Peter Parker balances his life as an ordinary high school student in Queens with his superhero alter-ego Spider-Man, and finds himself on the trail of a new menace prowling the skies of New York City.",
		"Director": "Jon Watts",
		"Budget": "$175,000,000",
		"Runtime": "133 min",
	 	"Score": "7.5",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 13 ,
		"Title": "Thor: Ragnarok",
		"Year": "2017",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "Thor is imprisoned on the planet Sakaar, and must race against time to return to Asgard and stop Ragnarök, the destruction of his world, at the hands of the powerful and ruthless villain Hela.",
		"Director": "Taika Waititi",
		"Budget": "$180,000,000",
		"Runtime": "130 min",
	 	"Score": "7.9",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 14,
		"Title": "Batman v Superman: Dawn of Justice",
		"Year": "2016",
		"Poster": "https://m.media-amazon.com/images/M/MV5BYThjYzcyYzItNTVjNy00NDk0LTgwMWQtYjMwNmNlNWJhMzMyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "Fearing that the actions of Superman are left unchecked, Batman takes on the Man of Steel, while the world wrestles with what kind of a hero it really needs.",
		"Director": "Zack Snyder",
		"Budget": "$250,000,000",
		"Runtime": "151 min",
	 	"Score": "6.5",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 15,
		"Title": "Captain America: Civil War",
		"Year": "2016",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjQ0MTgyNjAxMV5BMl5BanBnXkFtZTgwNjUzMDkyODE@._V1_UY209_CR0,0,140,209_AL_.jpg",
		"Summary": "Political involvement in the Avengers' affairs causes a rift between Captain America and Iron Man.",
		"Director": "Anthony Russo, Joe Russo",
		"Budget": "$250,000,000",
		"Runtime": "147 min",
	 	"Score": "7.8",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 16 ,
		"Title": "Deadpool",
		"Year": "2016",
		"Poster": "https://m.media-amazon.com/images/M/MV5BYzE5MjY1ZDgtMTkyNC00MTMyLThhMjAtZGI5OTE1NzFlZGJjXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "A wisecracking mercenary gets experimented on and becomes immortal but ugly, and sets out to track down the man who ruined his looks.",
		"Director": "Tim Miller",
		"Budget": "$58,000,000",
		"Runtime": "108 min",
	 	"Score": "8.0",
	 	"MPAA": "R"

	},
	{
		"Id": 17,
		"Title": "Warcraft: The Beginning",
		"Year": "2016",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjIwNTM0Mzc5MV5BMl5BanBnXkFtZTgwMDk5NDU1ODE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "As an Orc horde invades the planet Azeroth using a magic portal, a few human heroes and dissenting Orcs must attempt to stop the true evil behind this war.",
		"Director": "Duncan Jones",
		"Budget": "$160,000,000",
		"Runtime": "123 min",
	 	"Score": "6.9",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 18,
		"Title": "Star Trek Beyond",
		"Year": "2016",
		"Poster": "https://m.media-amazon.com/images/M/MV5BZDRiOGE5ZTctOWIxOS00MWQwLThlMDYtNWIwMDQwNzBjZDY1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "The crew of the USS Enterprise explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy, who puts them, and everything the Federation stands for, to the test.",
		"Director": "Justin Lin",
		"Budget": "$185,000,000",
		"Runtime": "122 min",
	 	"Score": "7.1",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 19,
		"Title": "Kingsman: The Secret Service",
		"Year": "2015",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NTIwNDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "A spy organization recruits an unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius.",
		"Director": "Matthew Vaughn",
		"Budget": "$81,000,000",
		"Runtime": "129 min",
	 	"Score": "7.7",
	 	"MPAA": "R"

	},
	{
		"Id": 20,
		"Title": "Mad Max: Fury Road",
		"Year": "2015",
		"Poster": "https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwZjMyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical ruler in search for her homeland with the aid of a group of female prisoners, a psychotic worshiper, and a drifter named Max.",
		"Director": "George Miller",
		"Budget": "NA",
		"Runtime": "120 min",
	 	"Score": "8.1",
	 	"MPAA": "R"

	},
	{
		"Id": 21,
		"Title": "Jurassic World",
		"Year": "2015",
		"Poster": "https://m.media-amazon.com/images/M/MV5BNzQ3OTY4NjAtNzM5OS00N2ZhLWJlOWUtYzYwZjNmOWRiMzcyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "A new theme park, built on the original site of Jurassic Park, creates a genetically modified hybrid dinosaur, the Indominus Rex, which escapes containment and goes on a killing spree.",
		"Director": "Colin Trevorrow",
		"Budget": "$150,000,000",
		"Runtime": "124 min",
	 	"Score": "7.0",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 22,
		"Title": "Mission: Impossible - Rogue Nation",
		"Year": "2015",
		"Poster": "https://m.media-amazon.com/images/M/MV5BOTFmNDA3ZjMtN2Y0MC00NDYyLWFlY2UtNTQ4OTQxMmY1NmVjXkEyXkFqcGdeQXVyNTg4NDQ4NDY@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "Ethan and team take on their most impossible mission yet, eradicating the Syndicate - an International rogue organization as highly skilled as they are, committed to destroying the IMF.",
		"Director": "Christopher McQuarrie",
		"Budget": "$150,000,000",
		"Runtime": "131 min",
	 	"Score": "7.4",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 23,
		"Title": "Terminator Genisys",
		"Year": "2015",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjM1NTc0NzE4OF5BMl5BanBnXkFtZTgwNDkyNjQ1NTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "When John Connor, leader of the human resistance, sends Sgt. Kyle Reese back to 1984 to protect Sarah Connor and safeguard the future, an unexpected turn of events creates a fractured timeline.",
		"Director": "Alan Taylor",
		"Budget": "$155,000,000",
		"Runtime": "126 min",
	 	"Score": "6.4",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 24,
		"Title": "Furious 7",
		"Year": "2015",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFtZTgwNzY2MTMxMzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "Deckard Shaw seeks revenge against Dominic Toretto and his family for his comatose brother.",
		"Director": "James Wan",
		"Budget": "$190,000,000",
		"Runtime": "137 min",
	 	"Score": "7.2",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 25,
		"Title": "Divergent",
		"Year": "2014",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMTYxMzYwODE4OV5BMl5BanBnXkFtZTgwNDE5MzE2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "In a world divided by factions based on virtues, Tris learns she's Divergent and won't fit in. When she discovers a plot to destroy Divergents, Tris and the mysterious Four must find out what makes Divergents dangerous before it's too late.",
		"Director": "Neil Burger",
		"Budget": "$85,000,000",
		"Runtime": "139 min",
	 	"Score": "6.7",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 26,
		"Title": "Tansformers: Age of Extinction",
		"Year": "2014",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMjE1OTMyODA5M15BMl5BanBnXkFtZTgwMjc2MDk3MTE@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "When humanity allies with a bounty hunter in pursuit of Optimus Prime, the Autobots turn to a mechanic and his family for help.",
		"Director": "Michael Bay",
		"Budget": "$210,000,000",
		"Runtime": "165 min",
	 	"Score": "5.7",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 27,
		"Title": "Guardians of the Galaxy",
		"Year": "2014",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMTAwMjU5OTgxNjZeQTJeQWpwZ15BbWU4MDUxNDYxODEx._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.",
		"Director": "James Gunn",
		"Budget": "$170,000,000",
		"Runtime": "121 min",
	 	"Score": "8.1",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 28,
		"Title": "Captain America: The Winter Soldier",
		"Year": "2014",
		"Poster": "https://m.media-amazon.com/images/M/MV5BMzA2NDkwODAwM15BMl5BanBnXkFtZTgwODk5MTgzMTE@._V1_UY268_CR1,0,182,268_AL_.jpg",
		"Summary": "As Steve Rogers struggles to embrace his role in the modern world, he teams up with a fellow Avenger and S.H.I.E.L.D agent, Black Widow, to battle a new threat from history: an assassin known as the Winter Soldier.",
		"Director": "Anthony Russo, Joe Russo",
		"Budget": "$170,000,000",
		"Runtime": "136 min",
	 	"Score": "7.8",
	 	"MPAA": "PG-13"

	},
	{
		"Id": 29,
		"Title": "The Last Stand",
		"Year": "2013",
		"Poster": "https://m.media-amazon.com/images/M/MV5BODc4NjI0OTYwNl5BMl5BanBnXkFtZTcwOTYwODQ3OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "The leader of a drug cartel busts out of a courthouse and speeds to the Mexican border, where the only thing in his path is a sheriff and his inexperienced staff.",
		"Director": "Jae-woon Kim",
		"Budget": "$45,000,000",
		"Runtime": "107 min",
	 	"Score": "6.4",
	 	"MPAA": "R"

	},
	{
		"Id": 30,
		"Title": "G.I. Joe: Retaliation",
		"Year": "2013",
		"Poster": "https://m.media-amazon.com/images/M/MV5BNzk5ODM0OTQ0N15BMl5BanBnXkFtZTcwODg2ODE4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg",
		"Summary": "The G.I. Joes are not only fighting their mortal enemy Cobra; they are forced to contend with threats from within the government that jeopardize their very existence.",
		"Director": "Jon M. Chu",
		"Budget": "$130,000,000",
		"Runtime": "110 min",
	 	"Score": "5.8",
	 	"MPAA": "PG-13"

	}

]


@app.route('/')
def hello_world():
   return 'Hello World'


@app.route('/Add_item')
def Add_item(name=None):
	return render_template('Add_item.html', data=data) 


@app.route('/search')
def search(name=None):
	return render_template('search.html', data=data) 


@app.route('/item/<item_id>')
def item(item_id=None):
	return render_template('item.html', item_id = item_id, data=data) 

@app.route('/save_item', methods=['GET', 'POST'])
def save_item():
	global data
	global current_id

	new_item = request.get_json()
	single_item = {
		"Title": new_item["Title"],
		"Year ": new_item["Year"],
		"Poster": new_item["Poster"],
		"Summary": new_item["Summary"],
		"Director": new_item["Director"],
		"Budget": new_item["Budget"],
		"Runtime": new_item["Runtime"],
	 	"Score": new_item["Score"],
	 	"MPAA": new_item["MPAA"]

	}

	current_id += 1
	new_entry = {
		"Id": current_id,
		"Title": new_item["Title"],
		"Year ": new_item["Year"],
		"Poster": new_item["Poster"],
		"Summary": new_item["Summary"],
		"Director": new_item["Director"],
		"Budget": new_item["Budget"],
		"Runtime": new_item["Runtime"],
	 	"Score": new_item["Score"],
	 	"MPAA": new_item["MPAA"]

	}
	data.insert(0,new_entry)
	return jsonify(data=data)









if __name__ == '__main__':
   app.run(debug = True)

