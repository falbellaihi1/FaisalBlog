var scriptTag = document.getElementById("remtime")
var input=0;

let remaining = new XMLHttpRequest();


//TODO remove lator
setInterval(
    function() {
    }, 3000 )
// instead of calling setInterval, call it when video stops!!




///function that POSTS the remining time andd video 
function PostVideoData() {

    var newinput = document.getElementById("remtime").value;
    var video_id = document.getElementById("video_id").value;
    if (newinput != input) {
        input = newinput;
      
    }

//TODO change address (url) 
var saveData = $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/lectures/analytics/",
      data: {"value": input, "id" : video_id},
      dataType: "text",
      success: function(resultData){
          //alert("Save Complete " + resultData);
      }
});


}
