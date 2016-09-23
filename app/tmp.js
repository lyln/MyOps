function SrsPlayer(container, width, height, private_object) {
    if (!SrsPlayer.__id) {
        SrsPlayer.__id = 100;
    }
    if (!SrsPlayer.__players) {
        SrsPlayer.__players = [];
    }

    SrsPlayer.__players.push(this);

    this.private_object = private_object;
    this.container = container;
    this.width = width;
    this.height = height;
    this.id = SrsPlayer.__id++;
    this.stream_url = null;
    this.buffer_time = 0.3; // default to 0.3
    this.max_buffer_time = this.buffer_time * 3; // default to 3 x bufferTime.
    this.volume = 1.0; // default to 100%
    this.callbackObj = null;
    this.srs_player_url = "srs_player/release/srs_player.swf?_version="+srs_get_version_code();

    // callback set the following values.
    this.meatadata = {}; // for on_player_metadata
    this.time = 0; // current stream time.
    this.buffer_length = 0; // current stream buffer length.
    this.kbps = 0; // current stream bitrate(video+audio) in kbps.
    this.fps = 0; // current stream video fps.
    this.rtime = 0; // flash relative time in ms.

    this.__fluency = {
        total_empty_count: 0,
        total_empty_time: 0,
        current_empty_time: 0
    };
    this.__fluency.on_stream_empty = function(time) {
        this.total_empty_count++;
        this.current_empty_time = time;
    };
    this.__fluency.on_stream_full = function(time) {
        if (this.current_empty_time > 0) {
            this.total_empty_time += time - this.current_empty_time;
            this.current_empty_time = 0;
        }
    };
    this.__fluency.calc = function(time) {
        var den = this.total_empty_count * 4 + this.total_empty_time * 2 + time;
        if (den > 0) {
            return time * 100 / den;
        }
        return 0;
    };


    empty_count()