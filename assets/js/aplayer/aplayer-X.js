const ap = new APlayer({
    lrcType: 3,
    // 列表折叠
    listFolded: true,
    // 自动播放
    autoplay: false,
    container: document.getElementById('aplayer'),
    audio: [
        {
            name: '平凡之路',
            artist: '朴树',
            url: 'assets/mp3/朴树 - 平凡之路.mp3',
            cover: 'images/music/Road.jpeg',
            lrc:'assets/mp3/lyrics/平凡之路 - 朴树.lrc'
        }, {
            name: 'スパークル',
            artist: 'RADWIMPS',
            url: 'assets/mp3/スパークル.mp3',
            cover: 'images/music/name.jpeg',
            lrc:'assets/mp3/lyrics/スパークル.lrc'
        }, {
            name: '[Instrumental]',
            artist: ' Swaggin\' Drama',
            url: 'assets/mp3/Swaggin\' Drama [Instrumental].mp3',
            cover: 'images/music/lol.jpeg',
            lrc:'assets/mp3/lyrics/nothing.lrc'
        }, {
            name: 'unravel',
            artist: 'TK from凛冽时雨',
            url: 'assets/mp3/TK from凛冽时雨——unravel.mp3',
            cover: 'images/music/unravel.jpeg',
            lrc:'assets/mp3/lyrics/unravel.lrc'
        }, {
            name: '失楽園',
            artist: 'Reol',
            url: 'assets/mp3/Reol - 失楽園.mp3',
            cover: 'images/music/失楽園.jpg',
            lrc:'assets/mp3/lyrics/Reol - 失楽園.lrc'
        }, {
            name: 'mede:mede',
            artist: 'Reol',
            url: 'assets/mp3/Reol - mede mede.mp3',
            cover: 'images/music/Reol.jpeg',
            lrc:'assets/mp3/lyrics/Reol - medemede.lrc'

        }, {
            name: 'My Songs Know What You Did In the Dark',
            artist: 'Fall Out Boy',
            url: 'assets/mp3/Fall Out Boy - My Songs Know What You Did In the Dark (Light Em Up).mp3',
            cover: 'images/music/My Songs Know What You Did In the Dark.jpg',
            lrc: 'assets/mp3/lyrics/Fall Out Boy - My Songs Know What You Did In the Dark (Light Em Up).lrc'
        }, {
            name: '心臓を捧げよ!',
            artist: 'Linked Horizon',
            url: 'assets/mp3/Linked Horizon - 心臓を捧げよ! (献出心脏!).mp3',
            cover: 'images/music/心臓を捧げよ!.jpg',
            lrc:'assets/mp3/lyrics/Linked Horizon - 心臓を捧げよ! (献出心脏!).lrc'
        }]
});
ap.play();