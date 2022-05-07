
(
// s.options.numOutputBusChannels = 14;

//increase number of buffers the server has access to for loading samples
// s.options.numBuffers = 1024 * 16;
 //increase the memory available to the server
// s.options.memSize = 8192 * 64;
 //boot the server
// s.boot;
 //display the oscilloscope
s.scope;
 //start proxyspace
// p=ProxySpace.push(s);

thisProcess.openUDPPort(4545); // attempt to open 4545
thisProcess.openPorts;

// OSC PARSING

~o = Array.series(32);
~params = ~o.collect{ Bus.control(s, 1) };
~section = Bus.control(s, 1);
~time = Bus.control(s,1);
~paramavg = Bus.control(s,1);
~parammax = Bus.control(s,1);
~parammin = Bus.control(s,1);


)

(
// OSCdef(\section, {|msg|
// 	msg.postln;
// 	~section.set(msg[1]);
// 	}, "/section"
// ).permanent_(true);
//
// OSCdef(\time, {|msg|
// 	var paramArray, paramAvg;
// 	msg.postln;
// 	~time.set(msg[1]);
// 	paramArray = { Array.fill(size:8, function: {arg i;  ~params[i].getSynchronous}) }.value;
// 	paramAvg = (paramArray.sum / paramArray.size);
// 	~paramavg.set(paramAvg);
// 	}, "/time"
// ).permanent_(true);

// OSCdef(\param, {|msg|
// 	// ~frame.set(msg[1]);
// 	msg.postln;
// 	~params[ msg[1] ].set(msg[2] / 1000);
// 	// ("Frame count: " ++ msg[1]).postln;
// 	}, "/param"
// ).permanent_(true);
// );

OSCdef(\param, {|msg|
	// ~frame.set(msg[1]);
	msg.postln;
	~params[ msg[1] ].set(msg[3]);
	// ("Frame count: " ++ msg[1]).postln;
	}, "/param"
).permanent_(true);
);