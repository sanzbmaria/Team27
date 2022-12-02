const Status = {
	logedIn: true,
	logedOut: false,
};

window.addEventListener("load", () => {
	isLoggedIn(); //Check if user is logged-in
});

// Todo: Get Email and Password from HTML, Save it to the DB
function isLoggedIn() {
	// Todo: change this once DB is implemented
	let userInfo = Status.logedIn; // change for check cookes function
	if (!userInfo) {
		console.log("not user");
		// show page where user logs/registers
		notLoggedIn();
	} else {
		// show page content
		loggedIn();
	}
}

// When a user is not logged in, only the login/register page should be shown
function notLoggedIn() {
	console.log("not logged in");
	// Hidde asside
	document.getElementById("offcanvasResponsive").style.display = "none";
	// Hidde asside button on smaller screens
	document.getElementById("aside-button").style.display = "none";
	// Hide Notices
	document.getElementById("content-notices").style.display = "none";
}

// If the user is logged in, hide the login/register options
function loggedIn() {
	console.log("logged in");
	// Hide Login-Register-Menu
	document.getElementById("login-register-menu").style.display = "none";
}
