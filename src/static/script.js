function loaded(){
	if (navigator.geolocation)
	{
		alert("I support it");
		navigator.geolocation.getCurrentPosition(success, failure);
	}
}
function success(postion){
	lat=position.coords.latitude;
	longi=position.coords.longitude;
	acc=position.coords.accuracy;
	alert(lat + " " + longi + " " +acc);
}
function failure(){
	alert("I failed");
}

