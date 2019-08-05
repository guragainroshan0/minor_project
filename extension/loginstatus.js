function statusChangeCallback(response){
//  response is an object
/*{
    status: 'connected',
    authResponse: {
        accessToken: 'Access token of person using my app',
        expiresIn:'unix time when token expires and needs renewed',
        signedRequest:'contains information about the person using app',
        userID:'ID of the person using the app'
    }
}

*/
//status has 3 options connected if the user is connected to app
//other mentioned below 
//if the status is connected there is authresponse


    if(response.status ==='not_authorized'){
        //logged in to facebook but not in extension
        //shows the login dialog
        FB.login();
    }
    else if(response.status === 'unknown'){
        //status is unknown so just show login dialog again
        FB.login();
    }
    else {
        window.location.href = 'https://www.facebook.com'
    }

    if(response.authResponse){
        //if the response status is connected
    }
}

FB.getLoginStatus(function(response){
    statusChangeCallback(response);
})

function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }