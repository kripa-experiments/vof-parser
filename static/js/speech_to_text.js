function consoleLogger(text, data) {
  console.log(text + " " + (data || ''));
}

var recorder = new Recorder({
  monitorGain: 0,
  recordingGain: 1,
  numberOfChannels: 1,
  wavBitDepth: 16,
  encoderPath: "/static/js/external/opus/waveWorker.min.js"
});

recorder.onstart = function(){
  consoleLogger('Recorder is started');
  // start.disabled = resume.disabled = true;
  // pause.disabled = stopButton.disabled = false;
};

recorder.onstop = function(){
  consoleLogger('Recorder is stopped');
  // start.disabled = false;
  // pause.disabled = resume.disabled = stopButton.disabled = true;
};

recorder.onpause = function(){
  consoleLogger('Recorder is paused');
  // pause.disabled = start.disabled = true;
  // resume.disabled = stopButton.disabled = false;
};

recorder.onresume = function(){
  consoleLogger('Recorder is resuming');
  // start.disabled = resume.disabled = true;
  // pause.disabled = stopButton.disabled = false;
};

recorder.onstreamerror = function(e){
  consoleLogger('Error encountered: ' + e.message);
};

recorder.ondataavailable = function(typedArray) {
  console.log('data available')
  var http = new XMLHttpRequest();
  http.open('POST', '/speech_to_text', true)
  
  http.onreadystatechange = function() {
    if (this.readyState === 4 && this.status === 200) {
      setNarrative(http.responseText)
    }
    if (this.readyState === 4 && this.status === 500) {
      console.log("ERROR: " + http.responseText);
    }
  }

  http.send(new Blob([typedArray], { type: 'audio/wav' }));
};


var toggleRecording = function() {
  if (recorder.state === 'inactive') {
    startRecording();
  } else {
    stopRecording();
  }
}

var startRecording = function() {
  recorder.start().catch(function(e){
    console.log('Error encountered:', e.message );
  });
  var x = document.getElementById('talk');
  x.classList.add('dark-red')
  x.innerText = 'Stop'
}

var stopRecording = function() {
  recorder.stop();
  var x = document.getElementById('talk');
  x.classList.remove('dark-red')
  x.innerText = 'Talk'
}
