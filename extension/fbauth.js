window.fbAyncInit = function(){
    FB.init({
        appId: '329702947703206',
        cookie : true,
        xfbml : true,
        version: 'v3.3'
    });
    FB.AppEvents.logPageView();
};

(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if(d.getElementById(id)){return ;};
    js = d.createElement(s);
    js.id = id;
    js.src = "fb_auth/sdk.js";
    fjs.parentNode.insertBefore(js,fjs);
}(document,'script','facebook-jssdk'));