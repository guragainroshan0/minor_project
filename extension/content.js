/*
This is chrome api that shows the icon in the screen
*/
chrome.runtime.sendMessage({todo:"showPageAction"});

//a = document.getElementsByTagName('head');
//a.appendChild("<script src='jquery-3.3.1.min.js'></script>")

var d = chrome.runtime.getURL("./images/icons/icon.png");
var d2 = chrome.runtime.getURL("./images/icons/icon2.png");

$(document).on('click','.this-is-my-dropdown',function(){

    var url = this.value;
    var win = window.open(url,"_blank");
    win.focus();

})



/*
    Click listener for the icon ie the image of the extension
*/
$(document).on('click','.this-is-my-image',function(){
    /*
    div variable is the image instance
    */
    var div = $(this);
    //console.log($(this).attr('id'));
    //var ima = $(this).find('.this-is-my-image');

    /*
    Since the title is added to the id of the image it is retrieved here
    */
    var title = $(this).attr('id');


    

    chrome.runtime.sendMessage({
        contentScriptQuery:"querynews",
        news : title
    }, function(response)
    {
        var responsedata = response.result;
    
        console.log(responsedata)

    /*
    
        For sending webrequest ajax is used xhr is the instance
    */
  //  var xhr  = new XMLHttpRequest();
    /*
    Here "GET" is sending the get request
    The url is the url of the server and title is the query parameter
    */
   // xhr.open("GET","http://localhost:8000/news/"+title);

    /*
    Ajax sends asynchronous request so in load the function gets executed
    */
    //xhr.onload = function(){
        /*
            response is the response from the server here the json data is sent
        */
        //var response = xhr.response;
       // console.log(response);

       // div.attr('src',"https://assets-cdn-npb.kantipurdaily.com/uploads/source/news/kantipur/2018/miscellaneous/supreme-court-29112018040924-1000x0.jpg");
       /*
            This is used to hide the image after it has been clicked
            div is the instance of the image
       */
       //div.hide()

        /*
            the json is parsed
        */
        var resp = JSON.parse(responsedata);

        /*
            The data are extracted from the response
            color contains the color returned
            link is the links in the json data of the response
            if statements checks if a particular source has the news if not it is not used
        */
        //var color = resp.color;
        //alert(color);
       // var link = resp.links;
       var link = resp.result;
        var htmlText="";

        for(var i=0;i<link.length;i++)
        {
            htmlText+=getOption(link[i].link,link[i].title);
        }

      
      /*
      If statements for the news in json if news in json then add the news in drop down list
      */
       // var htmlText = '<img src="https://www.freeiconspng.com/uploads/blue-button-icon-png-20.png" height="25px" width="25px" style="float:right;display:inline;margin-right:25px" onclick="myFunction('+title+')" class="dropbtn"><div id="'+title+'" class="dropdown-content">'
       
       
    //    for(var i=0; i<link.length; i++){
    //      var a = link[i];
    //      htmlText+=getOption(a[1],a[0]+":- "+a[2]);
    //     //htmlText+=ddown(link.ekantipur+"/"+title,"ekantipur");
    // }
     

        /*
            <select> tag returns the drop down menu and html text containst the options
        */
       if(link.length==0)
       {

        div.attr('src',"https://img.icons8.com/dusk/64/000000/pi.png");
        
       }
       else{
       
        div.attr('src',"https://i.imgur.com/eFy7r3z.png");
        var finalHtml = "<select class='this-is-my-dropdown'><option value=''>News</option>"+htmlText+"</select>";
       
       // var finalHtml = '<div class="dropdown"><div class="dropdown-content">'+htmlText+'</div></div>'

        /*
            For adding the drop down menu the drop variable is used it has div element
            Th innerHTML of the div is the drop down menu
        */
        var drop = document.createElement('div');
        drop.innerHTML = finalHtml;
        drop.className = "dropdown";

        /*
            Here the post variable has the image instance title is the title sent to the server
        */
        var post= document.getElementById(title);
        /*
            This goes to the parent node and append the drop down list to the parent node
        */
        post.parentNode.appendChild(drop);
        //alert(title);
       }
    }

    /*
    The request is sent using this
    */
  //  xhr.send();
);
});
//});
  
/*
    function to get all the post and add the extension icon the set interval function is an infinite loop
*/
setInterval(function(){

  

    /*
    posts has all the post in the facebook link (posts is an array)
    */
    var posts = document.getElementsByClassName('_4-u2 mbm _4mrt _5v3q _7cqq _4-u8');


    //var titles = new Array();


    /*
    this is for the links that are shared
    */
    var shares= document.getElementsByClassName('_4-u2 mbm _4mrt _5v3q _7cqq _4-u8');



    for(var i=0;i<posts.length;i++){
/*
        For loop to add the icon on every post
*/

        //get each post from posts array
        var post = posts[i];

        /*
        data has the post title and the data
        */
        var data = post.querySelector('._3n1k');
        if(data)
        {

        /*
        title is the title in bold in posts
        */
        var title = data.querySelector('.mbs');

        /*
        data is the link of the post
        */
        var li = data.querySelector('a').innerHTML;

        /*
        createRow function to add image
        */
        createROW(post,li);
       
        //titles.push(data);
            
    }
}

},5000);


/*
function to add the image in the post 
the argument post is the post instance and title is the title of the post
*/
function createROW(post,title){
    
    /*
    This is the parent node of the added image div the image div is in code below
    datas[0] is the data div element created 
    */
    var datas = post.getElementsByClassName('_6a uiPopover _5pbi _cmw _b1e _1wbl');

    /*
        Check if there is the extension image if not add one
    */
   
    var a = check_nepali(title);

    if(datas[0].getElementsByClassName('this-is-my-class').length===0 && a==true)
     {

        /*
            Create element item which is div 
            add class name 'this-is-my-class'
            add height, width
            the innerHTML contains the image tag 
        */
        var item = document.createElement('div');
        item.className = 'this-is-my-class';
        //item.id = title;  
        //item.clicked = false;
        item.height=25;
        item.width=25;
       // item.src="https://assets-cdn.ekantipur.com/images/kantipur-radio/politics/download-26122018082624-600x0.jpg";
       /*
            THIS IS THE CODE WHERE THE DIFFERENT PROPERTIES OF THE IMAGE OF THE EXTENSION LIES
            src= link to the image of to be displayed
            class = 'this-is-my-image'
            id = title here title is the title of the facebook post. The id of title is given so that the title can be retriived easily in click listener where Ajax request is sent 
       */
        item.innerHTML=
        '<img src='+d+' class="this-is-my-image" id="'+title+'" height="25px" width="25px" style="float:right;display:inline;margin-right:25px">';
        
        /*
            Now the code of the image is added
        */
        datas[0].appendChild(item);
        
    }     
}

/*
    Function to return the code for drop down menu
    the value property is given the link because on click the redirection happens
    site is the text to be displayed in the drop down menu
*/
function getOption(link,site)
{
    
    return "<option value='"+link+"'><a href="+link+">"+site+"</a></option>";
}

function add(title,link){
     return "<a href="+link+"><p>"+title+"</p></a>";
}

function dropDown(){
    
  
  
  
}

function check_nepali(title)
{
    var a = 0;
    for(var i=0;i<title.length;i++)
    {
        var int_of_nep = title[i].charCodeAt(0);
        if(int_of_nep > 2324)
        {
            a ++;
        }
    }
    if (a> title.length/3)
    {
        return true;
    }
    return false;
}