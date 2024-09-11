const fortunes = [
    "오늘은 행운이 따를 것입니다.",
    "당신은 놀라운 기회를 얻을 것입니다.",
    "힘든 시기가 지나갈 것입니다.",
    "새로운 친구를 사귈 기회가 생길 것입니다.",
    "긍정적인 태도가 좋은 결과를 가져올 것입니다.",
    "당신의 노력은 결실을 맺을 것입니다.",
    "마음을 여는 것이 중요합니다.",
    "자신을 믿으세요.",
    "생각지도 못한 곳에서 답을 찾게 될 것입니다.",
    "당신의 목표는 곧 달성될 것입니다."
];

document.getElementById('generate-cookie').addEventListener('click', function () {
    const randomIndex = Math.floor(Math.random() * fortunes.length);
    const fortuneText = fortunes[randomIndex];
    document.getElementById('fortune-text').textContent = fortuneText;
});
