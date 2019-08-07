chrome.runtime.onMessage.addListener(function(request,sender,sendResponse){

    /*check for request from content.js*/
    if(request.contentScriptQuery == "querynews")
    {
        let xhr = new XMLHttpRequest();

        // encode uri component
        var news= encodeURIComponent(request.news)
        var url = "http://127.0.0.1:8000/news/"+news;

        //send xhr request
        xhr.open("GET",url);
        xhr.send()
    
        //call back function
        xhr.onload = function(){
            var response = xhr.response;
            console.log(response);

            sendResponse({"result":response});
            
        }
    }

    chrome.tabs.query({active:true,currentWindow:true},function(tabs){

        //highlight the icon on tab where extension is loaded
        chrome.pageAction.show(tabs[0].id);
    
    });

    //this sends message to content.js to wait until response from query is received
    return true;

});

function onRequest(request,sender,sendResponse){

    

}


// chrome.storage.sync.get(['title'],function(object){
//     var xhr  = new XMLHttpRequest();
//     var title = object.title;
//     xhr.open("GET","http://localhost:8888/data?title="+title);
//     xhr.onload= function(){
//         chrome.storage.sync.set({'response':xhr.responseText},function(){});
//     }
//     xhr.send();
//     //var response = xhr.responseText;
//     //console.log("response="+response);
    
    
// });

// var menuItem = {
//     "id":"report_links",//     "title":"Report Link",  // };
// chrome.contextMenus.create(menuItem);

// chrome.contextMenus.onClicked.addListener(function(clickData){
//     if(clickData.menuItemId=="report_link")
//     {
        
//             var url_d = clickData.pageUrl;
//             var xhr  =new XMLHttpRequest();
//             xhr.open("GET","http://localhost:8888/report?url="+url_d);
//             xhr.onload = function(){
//                 console.log(xhr.response);
//             }
//             xhr.send();
        
     
        
//     }
// });


// chrome.tabs.query({active:true,currentWindow:true},function(tabs){

//     var tab = tabs[0];
//     var link = tab.url;

//     var xhr = new XMLHttpRequest();
//     xhr.open("GET","http://localhost:8888/valid?link="+link);
//     xhr.onload = function()
//     {
        
//     }
//     xhr.send();
   

    
// });
