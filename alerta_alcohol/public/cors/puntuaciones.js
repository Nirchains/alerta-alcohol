var host = "https://www.alcoholalerta.es";
var apiKey = "e789694259dabb0";
var apiSecret = "7b457950d0ee1c4";

//PRE
var pre = false;
if (pre) {
	host = "http://pre.alertaalcohol.com";
	apiKey = "e789694259dabb0";
	apiSecret = "6d5c25a13880b90";
}

const token = "token " + apiKey + ":" + apiSecret
const headers = new Headers();
headers.append('Authorization', token);
headers.append('cache-control', 'no-cache');
headers.append('Accept', 'application/json');
headers.append('Content-Type', 'application/json');


function getCard(username, project, card) {
	
	//var url0 = host + "/api/resource/Incentivos?fields=[%22username%22,%20%22project%22,%20%22card%22]";
	var url = host + "/api/resource/Carta/" + card;
			
	fetch(url, {
		headers: {
			'Authorization': token
		}
	})
	.then(r => r.json())
	.then(r => {
		//console.log(r.data.image);
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

function ping() {
	
	//var url0 = host + "/api/resource/Incentivos?fields=[%22username%22,%20%22project%22,%20%22card%22]";
	var url = host + "/api/method/alerta_alcohol.alerta_alcohol.doctype.incentivos.incentivos.pingdos";
			
	fetch(url, {
		headers: {
			'Authorization': token
		}
	})
	.then(r => r.json())
	.then(r => {
		console.log(r);
		
	})

	
}

function alerta_puntuacion(username, fullname, email, location, project, card) {
	//obtenemos la carta
	var url = host + "/api/resource/Carta/" + card;
			
	fetch(url, {
		headers: {
			'Authorization': token
		}
	})
	.then(r => r.json())
	.then(r => {
		//console.log(r.data.image);
		var card_element = document.getElementById('card');
		card_element.outerHTML = "<div id='card'><img src='" + host + "" + r.data.image + "' alt='funciona' /></div>";
		var card_container = document.getElementById('card-container');
		//card_element.classList.remove("card-0");
		card_container.classList.add("card-1");
	})

	//guardamos las puntuaciones
	var url = host + "/api/method/alerta_alcohol.alerta_alcohol.doctype.incentivos.incentivos.alerta_puntuacion";
			
	const data = {
			username: username,
			fullname: fullname,
			email: email,
			location: location,
			project: project,
			card: card
		}
	const init = {
		method: 'POST',
		headers,
		body: JSON.stringify(data)
	}

	fetch(url, init)
	.then((response) => {
		console.log("Respuesta: " + response);
		return response.text(); // or .json() or .blob() ...
	})
	.then((text) => {
		console.log(text) // text is the response body
	})
	.catch((e) => {
		console.log(e) // error in e.message
	});
}

function trazar_error(mensaje) {
	var url = host + "/api/method/alerta_alcohol.alerta_alcohol.doctype.incentivos.incentivos.trazar_error";
			
	const data = {
			mensaje: mensaje
		}
	const init = {
		method: 'POST',
		headers,
		body: JSON.stringify(data)
	}

	fetch(url, init)
	.then((response) => {
		console.log(response);
		return response.text(); // or .json() or .blob() ...
	})
	.then((text) => {
		console.log(text) // text is the response body
	})
	.catch((e) => {
		console.log(e) // error in e.message
	});
}
