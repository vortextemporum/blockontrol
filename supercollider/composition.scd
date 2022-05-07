(

// param1 - scale (0-7)
~params[0].set(5);

//param1 - scales
// ~params[0].set(rrand(0,4));


// param2 - fundamental note
~params[1].set(rrand(0,11));

// param4 - seq1speed
~params[2].set(rrand(1,10000)); // 0.25 - 5

// param6 - seq1octave
~params[3].set(rrand(0,4)); // -2 +3

// param4 -
~params[4].set(rrand(1,10000)); // 0.25 - 5

// param6 - seq2 octave
~params[5].set(rrand(0,4));
//
// param4 - seq2 speed
~params[6].set(rrand(1,10000)); // 0.25 - 5

// param6 - seq3 octave
~params[7].set(rrand(0,4));
// param8 - seq1 amt of note speed chaos
// ~params[7].set(rrand(0,4));

)



//
(

~scales = #[
	[0,3,7,10,14],
	[0,5,7,10],
	[0,3,7, 8],
	[0,7,8,15],
	[0,7,12,19],
	[0,4,7,11]
];
Ndef(\sineArp1, {
	var centerNote = 60;
	var freq1, trig1, seq1, sig1;
	var fund, scale, tuning;
	var seq1speed, seq1notes, seq1octave;
	// var scaleNum = Select.kr(~params[0].kr,[0,1,2,3,4,5]);


	scale = ~scales[1];
	// scale = ~scales[scaleNum];
	fund = ~params[1].kr.lag(2);
	// fund = Select.kr(~params[1].kr,[2,8,11]).lag(2);

	seq1speed = ~params[2].kr.linlin(1,10000, 0.15,10);
	seq1octave = ~params[3].kr.linlin(0,4,-2,2);
	// seq1chaos =

    trig1 = Dust.kr(seq1speed);
	seq1 = Dseq((Dshuf(centerNote + fund + (seq1octave * 12) + Select.kr(~params[0].kr,
		~scales), 3) + Dwrand([0,12,24],[0.85,0.1,0.05],inf)),inf).midicps;
    freq1 = Demand.kr(trig1, 0, seq1);
	sig1 = 	SinOsc.ar(freq1).cubed.cubed * 0.07 * EnvGen.kr(Env.perc,trig1);
	// sig1 = 	SinOsc.ar(freq1 + [0,0.7]).cubed.cubed * 0.07;


	Out.ar(6,sig1);
	// sig1 + sig2;



});

Ndef(\sineArp2, {
	var centerNote = 60;
	var fund, scale, tuning;
	var freq2, trig2, reset, seq2, sig2;
	var seq2speed, seq2notes, seq2octave;

	scale = ~scales[1];
	// scale = ~scales[~params[0].kr.round(0)];
	fund = ~params[1].kr.lag(2);
	// fund = Select.kr(~params[1].kr,[2,8,11]).lag(2);


	seq2speed = ~params[4].kr.linlin(1,10000, 0.15,2);
	seq2octave = ~params[5].kr.linlin(0,4,-2,2);
	// seq1chaos =


    trig2 = Dust.kr(seq2speed);
	seq2 = (Dseq(centerNote + fund + (seq2octave * 12) + Select.kr(~params[0].kr,
		~scales), inf) + Dwrand([0,12],[0.85,0.1],inf)).midicps;
    freq2 = Demand.kr(trig2, 0, seq2);
	sig2 = 	SinOsc.ar(freq2 ) * 0.03;

	Out.ar(7,sig2);
	// sig1 + sig2;



});

//
Ndef(\sineArp3, {
	var centerNote = 60;
	var fund, scale, tuning;
	var freq2, trig2, reset, seq2, sig2;
	var seq2speed, seq2notes, seq2octave;

	scale = ~scales[1];
	// scale = ~scales[~params[0].kr.round(0)];
	// fund = Select.kr(~params[1].kr,[2,8,11]).lag(2);

	fund = ~params[1].kr.lag(2);
	tuning = ~params[2].kr.linlin(0,25,-12,12).round();

	seq2speed = ~params[6].kr.linlin(0,10000, 0.15,2);
	seq2octave = ~params[7].kr.linlin(0,4,-2,2);
	// seq1chaos =


    trig2 = Impulse.kr(seq2speed);
	seq2 = (Drand(centerNote + fund + (seq2octave * 12) + Select.kr(~params[0].kr,
		~scales), inf) ).midicps;
    freq2 = Demand.kr(trig2, 0, seq2);
	sig2 = 	SinOsc.ar(freq2) * 0.03;

	Out.ar(8,sig2);
	// sig1 + sig2;



});




Ndef(\sineArp4, {
	var centerNote = 60;
	var freq1, trig1, seq1, sig1;
	var fund, scale, tuning;
	var seq1speed, seq1notes, seq1octave;
	var scaleNum = ~params[0].kr;

	scale = ~scales[1];
	// scale = ~scales[scaleNum];

	fund = ~params[1].kr.lag(2);
	// fund = Select.kr(~params[1].kr,[2,8,11]).lag(2);
	seq1speed = ~params[6].kr.linexp(1,10000, 0.15,10);
	// seq1chaos =


    trig1 = Dust.kr(seq1speed / 8);
	seq1 = Dseq(centerNote + fund - 24,inf).midicps;
    freq1 = Demand.kr(trig1, 0, seq1);
	sig1 = 	SinOsc.ar(freq1).cubed.cubed * 0.07 * EnvGen.kr(Env.perc,trig1);
	// sig1 = 	SinOsc.ar(freq1 + [0,0.7]).cubed.cubed * 0.07;


	Out.ar(9,sig1);
	// sig1 + sig2;



});


/*Ndef(\sineArp5, {
	var freq, trig, reset, seq,sig;
	var fund = ~params[1].kr.lag(2);

	trig = Impulse.kr(~params[2].kr.linexp(1,10000,0.5,20).lag(5));
	seq = Dseq([72, 75, 79, Drand([82,84,86])] + fund, inf).midicps;
	freq = Demand.kr(trig, 0, seq);
	sig = SinOsc.ar(freq + [0,0.7]).cubed.cubed * 0.02;


	Out.ar(10,sig);
	// sig1 + sig2;



	});*/

/*Ndef(\droneFM, {
	arg f1Freq=0.1, f2Freq=1, f3Freq=1, m1Ratio=1, m2Ratio=2, m3Ratio=1,
	amp=0.01, dur=55, ampM=0.84 , pan=0;
	var sig, car1, mod1, car2, mod2, car3, mod3, env, index;
	var nFreq = (~params[1].kr + 48).midicps.lag(2);


	index = LFNoise1.kr(0.2).range(2, 3);
	// env = EnvGen.kr(Env.new([0, 0.70, 0.70, 0], [dur*0.333, dur*0.333, dur*0.333]), doneAction:2);
	mod1 = SinOsc.ar([nFreq * m1Ratio, nFreq+0.3 * m1Ratio], mul:nFreq * m1Ratio * index) * ampM;
	car1 = SinOsc.ar(f1Freq + mod1);
	mod2 = SinOsc.ar([nFreq * m2Ratio, nFreq+1.4 * m2Ratio], mul:nFreq * m2Ratio * index) * ampM;
	car2 = SinOsc.ar(f2Freq + mod2);
	mod3 = SinOsc.ar([nFreq * m3Ratio, nFreq+0.35 * m3Ratio], mul:nFreq * m3Ratio * index) * ampM;
	car3 = SinOsc.ar(f3Freq + mod3) * 0.4;
	sig = car1 + car2 + car3 * amp;
	sig = Pan2.ar(sig, pan);
	Out.ar(10, sig);
}).play;
)*/
)



