/*

 reference  stackoverflow answer

 https://stackoverflow.com/questions/24646997/getting-current-time-of-embedded-iframe-youtube-player

*/


var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

var player;

function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
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

     console.log("my state changed ")


     /*
     TODO:
     SOMETHING LIKE ->
     CHECK IF PLAYER.STOPED
     			REMAINING = DURATION - TCURRENT_TIME

     */

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