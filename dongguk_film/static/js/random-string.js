var introMessage = new Array("오늘 촬영도 파이팅!", "오늘 편집도 파이팅!", "오늘 사전작업도 파이팅!", "오늘 후반작업도 파이팅!", "당신의 촬영을 응원해요!", "바빠도 밥은 먹고 찍어요!", "바빠도 잠은 자고 찍어요!", "외장하드 챙기셨죠?", "메모리 카드 챙기셨죠?", "슬레이트 챙기셨죠?", "보드 마커 챙기셨죠?", "배우 의상 잘 챙기셨죠?", "미술 소품 잘 챙기셨죠?", "사운드 건전지 챙기셨죠?", "배터리 잘 물려놓으셨죠?", "렌더링 잘 걸어놓으셨죠?", "메모리 백업 잘 하셨죠?", "안전촬영, 안전운전!");
var welcome = new Array("어서오세요!", "오! 오셨어요?", "반가워요!", "오늘도 아자아자!", "어서와요!", "환영해요!", "기다렸어요~", "왜 이제야 왔어요~", "잘 오셨어요!", "보고 싶었어요!");
var emoji = new Array("😀", "😁", "😃", "😄", "😆", "😉", "😊", "🙂", "🤗", "🤓");
var emoticon = new Array("o(>ω<)o", "o( ❛ᴗ❛ )o", "(๑˃ᴗ˂)ﻭ", "(´･ᴗ･ ` )", "(„• ֊ •„)", "(.❛ ᴗ ❛.)", "(≧◡≦)", "(o´∀`o)", "(*≧ω≦*)", "＼(≧▽≦)／", "ヽ(o＾▽＾o)ノ", "٩(◕‿◕｡)۶", "ヽ(・∀・)ﾉ", "(´｡• ω •｡`)", "ヽ(*・ω・)ﾉ", "(o´▽`o)", "(*´▽`*)", "(o˘◡˘o)");
function randomItem(e) {
    return e[Math.floor(Math.random() * e.length)];
}
if (document.querySelector("#introMessage")) {
    document.querySelector("#introMessage").innerText = randomItem(introMessage);
}
if (document.querySelector("#welcome")) {
    document.querySelector("#welcome").innerText = randomItem(welcome);
}
if (document.querySelector("#emoji")) {
    document.querySelector("#emoji").innerText = randomItem(emoji);
}
if (document.querySelector("#emoticon")) {
    document.querySelector("#emoticon").innerText = randomItem(emoticon);
}