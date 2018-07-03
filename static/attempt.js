console.log('loading attempt 2')

// try {
//   window.AudioContext = window.AudioContext || window.webkitAudioContext,
//   navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia
// } catch (b) {
//   console.log('Browser unsupported');
//   alert('browser unsupported');
//   // disble controls
// }
// var recorder;
// var me = {};
// var socket = null;
// var urlServer = window.location.host;
// var audioContext = new AudioContext();

// var playbackBuffers = function(buffers) {
// 	var newSource = audioContext.createBufferSource();
// 	var newBuffer = audioContext.createBuffer( 2, buffers[0].length, audioContext.sampleRate );
// 	newBuffer.getChannelData(0).set(buffers[0]);
// 	newBuffer.getChannelData(1).set(buffers[1]);
// 	newSource.buffer = newBuffer;

// 	newSource.connect(audioContext.destination);
// 	newSource.start(0);
// }

var startRecording = function(event) {
  navigator.getUserMedia({
    audio: true
  }, function(mediaStream) {
    var source = audioContext.createMediaStreamSource(mediaStream);
    recorder = new Recorder(source);
    recorder.record();
    // processor = audioContext.createScriptProcessor(bufferSize, 1, 1);
    // https://developer.mozilla.org/en-US/docs/Web/API/ScriptProcessorNode/onaudioprocess
    // https://github.com/mdn/voice-change-o-matic/blob/gh-pages/scripts/app.js
    // processor.onaudioprocess = function(audioProcessingEvent) {
    //   console.log('in processor.onaudioprocess');
    // };
    // processor.connect(audioContext.destination)
    // mediaTrack = mediaStream.getTracks()[0];
  }, function() {
    console.log ('Microphone inaccessible');
    // stopRecording();
  });
}

var stopRecording = function() {
  recorder.stop();
  recorder.getBuffer(playbackBuffers);
}

var downloadRecording = function() {
  recorder.exportWAV(function(blob) {
    var url = (window.URL || window.webkitURL).createObjectURL(blob);
    var link = document.getElementById('blob');
    link.href = url;
    link.download = 'output.wav';
  });
}

// var set = function() {
//   console.log(arguments);
// }

// var startStreaming_ = function() {
//   socket = new WebSocket("wss://" + urlServer + "/ws");
//   socket.binaryType = "arraybuffer";
//   socket.onopen = function() {
//     socket.send(JSON.stringify({
//       format: "LINEAR16",
//       language: languageSelected,
//       punctuation: punctuationEnabled,
//       rate: audioContext.sampleRate
//     }));
//     navigator.getUserMedia({
//       audio: !0
//     }, function(b) {
//       tabSelected = 0;
//       var d = audioContext.createMediaStreamSource(b);
//       processor = audioContext.createScriptProcessor(bufferSize, 1, 1);
//       processor.onaudioprocess = function(b) {
//         processAudio_(b)
//       }
//       ;
//       processor.connect(audioContext.destination);
//       d.connect(processor);
//       mediaTrack = b.getTracks()[0];
//       updateInterval = setInterval(function() {
//         setTimeDisplay_()
//       }, 500)
//     }, function() {
//       errorClient = "MICROPHONE_INACCESSIBLE";
//       stopRecording_()
//     })
//   };

//   socket.onmessage = function(b) {
//     b = JSON.parse(b.data);
//     b.isFinal ? transcripts[0].results ? (set("transcripts.0.tempResult", null),
//                                             push("transcripts.0.results", b.text)) : setResults_([b.text]) : (resultsReady = !0,
//                                                                                                               set("transcripts.0.isEnabled", !0),
//                                                                                                               set("transcripts.0.tempResult", b.text))
//   };

//   socket.onclose = function(b) {
//     1006 === b.code ? a.errorServer = "SERVICE_UNAVAILABLE" : a.controlsDisabled = !1
//   }

//   socket.onerror = function() {
//     a.errorServer = "SERVICE_UNAVAILABLE"
//   }
// }
