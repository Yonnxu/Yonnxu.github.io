const ap = new APlayer({
    // 迷你
    mini: true,
    // 吸底
    fixed: true,
    // 自动播放
    autoplay: true,
    container: document.getElementById('aplayer'),
    audio: [
        {
            name: '平凡之路',
            artist: '朴树',
            url: 'assets/mp3/朴树 - 平凡之路.mp3',
            cover: 'images/music/Road.jpeg'
        }, {
            name: 'スパークル',
            artist: 'RADWIMPS',
            url: 'assets/mp3/スパークル.mp3',
            cover: 'images/music/name.jpeg'
        }, {
            name: '[Instrumental]',
            artist: ' Swaggin\' Drama',
            url: 'assets/mp3/Swaggin\' Drama [Instrumental].mp3',
            cover: 'images/music/lol.jpeg'
        }, {
            name: 'unravel',
            artist: 'TK from凛冽时雨',
            url: 'assets/mp3/TK from凛冽时雨——unravel.mp3',
            cover: 'images/music/unravel.jpeg'
        }, {
            name: '失楽園',
            artist: 'Reol',
            url: 'assets/mp3/Reol - 失楽園.mp3',
            cover: 'images/music/Reol.jpeg'
        }, {
            name: 'mede:mede',
            artist: 'Reol',
            url: 'assets/mp3/Reol - mede mede.mp3',
            cover: 'images/music/Reol.jpeg'
        }, {
            name: 'My Songs Know What You Did In the Dark',
            artist: 'Fall Out Boy',
            url: 'assets/mp3/Fall Out Boy - My Songs Know What You Did In the Dark (Light Em Up).mp3',
            cover: 'images/music/My Songs Know What You Did In the Dark.jpg'
        }, {
            name: '心臓を捧げよ!',
            artist: 'Linked Horizon',
            url: 'assets/mp3/Linked Horizon - 心臓を捧げよ! (献出心脏!).mp3',
            cover: 'images/music/心臓を捧げよ!.jpg'
        }]
});
ap.play();