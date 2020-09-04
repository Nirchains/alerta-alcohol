//var host = "http://pre.alertaalcohol.com";
//var apiKey = "215e8d8fd8ea1e8";
//var apiSecret = "63b17f0ebe96d5d";


function getCard(username, project, card, host, apiKey, apiSecret) {
	const token = "token " + apiKey + ":" + apiSecret
	const headers = new Headers();
	headers.append('Authorization', token);
	headers.append('cache-control', 'no-cache');
	headers.append('Accept', 'application/json');
	headers.append('Content-Type', 'application/json');
	//var url0 = host + "/api/resource/Incentivos?fields=[%22username%22,%20%22project%22,%20%22card%22]";
	var url = host + "/api/resource/Carta/" + card;
			
	fetch(url, {
		headers: {
			'Authorization': token
		}
	})
	.then(r => r.json())
	.then(r => {
		console.log(r.data.image);
		var card_element = document.getElementById('card');
		card_element.outerHTML = "<div id='card'><img src='" + host + "" + r.data.image + "' alt='funciona' /></div>";
		var card_container = document.getElementById('card-container');
		//card_element.classList.remove("card-0");
		card_container.classList.add("card-1");
	})

	const data = {
			username: username,
			project: project,
			card: card
		}
	const init = {
		method: 'POST',
		headers,
		body: JSON.stringify(data)
	}

	const urll = host + "/api/resource/Incentivos"
	fetch(urll, init)
	.then((response) => {
		return response.text(); // or .json() or .blob() ...
	})
	.then((text) => {
		console.log(text) // text is the response body
	})
	.catch((e) => {
		console.log(e) // error in e.message
	});
}