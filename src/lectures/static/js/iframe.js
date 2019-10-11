/*

variables
*/
var tag = document.createElement('script');
var scriptTag = document.getElementsByTagName('script')[0];
var videoDuration;
var videoCurrentTime;
var remainingTime;
var player;




tag.src = "https://www.youtube.com/iframe_api";
scriptTag.parentNode.insertBefore(tag, scriptTag);


function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    playerVars: {
      'controls': 0,
      'disablekb': 1
    },
    events: {
      'onReady': onPlayerReady,
      'onStateChange': onPlayerStateChange
    }
  });

  update();
}


function onPlayerReady(event) {

  //console.log("hey Im ready");
  event.target.setVolume(100);
  event.target.playVideo();
  event.start()
  
  //do whatever you want here. Like, player.playVideo();

}


// did vid state changed? 
function onPlayerStateChange(event) {
  
  // disable ability to seek
  switch(event.data) {
  case YT.PlayerState.ENDED:
  console.log("ENDED");
  PostVideoData();
    break;
  case -1:
    console.log("NOT STARTED")
    break;
  case YT.PlayerState.PLAYING:
    console.log("PLAYING")
    PostVideoData();
    break;
  case YT.PlayerState.PAUSED:
    console.log("PAUSED")
    PostVideoData();
  case YT.PlayerState.BUFFERING:
    console.log("BUFFERING")
    break;
  case YT.PlayerState.CUED:
    console.log("VIDEO CUED");
    break
  default:
    console.log("defualt" + event.data)
    // code block
}


  // chekc if played video? 
    //send nothing keep calculating until vid stopped
  // check if stopped video
    //send post request
  if(remainingTime!=null){
  //console.log("my state changed " + "remaining time is : "+remainingTime );
  }

  else {
   // console.log("state changed and remainingTime is still 0")
  }

}

///stop the video
function stopVideo() {
  player.stopVideo();
}


function PrepareVideo()
{
  if(player.isMuted()){
    player.unMute();
  }

}

//update every 3 seconds
function update() {
  setInterval(
    function() {
      //assign curr time
      videoCurrentTime = player.getCurrentTime();
      /// aasign vid duration
      videoDuration = player.getDuration();
      //get the remining time and round it up + convert to mins 

      remainingTime = Math.floor(parseInt(videoDuration - videoCurrentTime) / 60);
      //todo remove log
       // player.seekTo(videoCurrentTime,false) does not work! its totally wrong to do it this way!
      var percRem = player.getCurrentTime()/ player.getDuration() *100
     document.getElementsByClassName("progress-bar").item(0).setAttribute('aria-valuenow',percRem);
     document.getElementsByClassName('progress-bar').item(0).setAttribute('stylele','width:'+percRem+'%');
     console.log(parseInt(percRem))
     //var iwatched = Math.floor(parseInt(player.getCurrentTime())/60)
     //console.log("i watched this amount of the video :" +iwatched)
     $(".progress-bar").animate({
    width: parseInt(percRem) + "%"
    }, 1);
   
      //setStyle(percRem);
     //console.log("here i am " + remainingTime);
      document.getElementById("remtime").value = remainingTime
      var doc = document.getElementById("remtime").value ;
      if(doc ==0){


      }
    }, 3000


  )
  player.getCurrentTime()

}





