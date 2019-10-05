var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player1;
var player2;
var checkInt; // save this as a var in this scope so we can clear it later

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player1', {
  	
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });


    player2 = new YT.Player('player2', {
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });

    startInterval()
}


function onPlayerReady() {

  console.log("hey Im ready");
  //do whatever you want here. Like, player.playVideo();

}

function onPlayerStateChange() {

     console.log("my state changed " );
      console.log("current time is : " + player.getCurrentTime );
  
}
/*

TODO CALCULATE REMAINING VIDEO, AND TIME WATCHED. 

*/
function startInterval() {
   //checks every 100ms to see if the video has reached 6s
   checkInt = setInterval(function() {
      if (player.getCurrentTime > 6) {
         changeSrc();

         clearInterval(checkInt);
      };
   }, 100)

}