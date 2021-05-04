function why(){
	prompt('Why you do this ?')
}


function copy(value){
	var tempInput = document.createElement("input");
  	tempInput.value = value;
  	document.body.appendChild(tempInput);
  	tempInput.select();
  	document.execCommand("copy");
  	document.body.removeChild(tempInput);
}


function discord(){
	copy("Moi#5013")
	alert("Discord ID copied")
}

function email(){
	copy("mathias@dupeux.net")
	alert("Email copied")
}