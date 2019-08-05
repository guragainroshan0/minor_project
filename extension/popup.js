$(function(){
$('#report').click(function(){
    console.log("clicked");
    var link = $('#link').val();
    console.log(link);
    $('#link').text("clicked");
    var xhr = new XMLHttpRequest();
    // chrome.storage.sync.get(['title'],function(t){
    //     var titles = t.title;
    //     for(var i=0;i<titles.length;i++)
    //     {
    //         xhr.open("GET","https://ingratiating-cosal.000webhostapp.com/get.php?title="+titles[i]);
    //         xhr.send();
    //         var result = xhr.responseText;
    //         $('#headi').text(result)
    //     }
    // });

    
  
 

});
});