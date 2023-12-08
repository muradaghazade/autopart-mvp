const slider = document.querySelector('.slider');
const slideButtons = document.querySelectorAll('.slide-button');

slideButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const targetSlideIndex = parseInt(button.getAttribute('data-slide-index')) - 1;
    const translateX = -targetSlideIndex * 33.3;
    slider.style.transform = `translateX(${translateX}%)`;
  });
});