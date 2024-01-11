/*=============== SHOW MENU ===============*/
const navMenu = document.getElementById("nav-menu"),
  navToggle = document.getElementById("nav-toggle"),
  navClose = document.getElementById("nav-close");

/*===== MENU SHOW =====*/
/* Validate if constant exists */
if (navToggle) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.add("show-menu");
  });
}

/*===== MENU HIDDEN =====*/
/* Validate if constant exists */
if (navClose) {
  navClose.addEventListener("click", () => {
    navMenu.classList.remove("show-menu");
  });
}

/*=============== REMOVE MENU MOBILE ===============*/
const navLink = document.querySelectorAll(".nav__link");

const linkAction = () => {
  const navMenu = document.getElementById("nav-menu");
  // When we click on each nav__link, we remove the show-menu class
  navMenu.classList.remove("show-menu");
};
navLink.forEach((n) => n.addEventListener("click", linkAction));

/*=============== ADD BLUR TO HEADER ===============*/
const blurHeader = () => {
  const header = document.getElementById("header");
  // When the scroll is greater than 50 viewport height, add the blur-header class to the header tag
  this.scrollY >= 50
    ? header.classList.add("blur-header")
    : header.classList.remove("blur-header");
};
window.addEventListener("scroll", blurHeader);

/*=============== SHOW SCROLL UP ===============*/
const scrollUp = () => {
  const scrollUp = document.getElementById("scroll-up");
  // When the scroll is higher than 350 viewport height, add the show-scroll class to the a tag with the scrollup class
  this.scrollY >= 350
    ? scrollUp.classList.add("show-scroll")
    : scrollUp.classList.remove("show-scroll");
};
window.addEventListener("scroll", scrollUp);

/*=============== SCROLL SECTIONS ACTIVE LINK ===============*/
const sections = document.querySelectorAll("section[id]");

const scrollActive = () => {
  const scrollDown = window.scrollY;

  sections.forEach((current) => {
    const sectionHeight = current.offsetHeight,
      sectionTop = current.offsetTop - 58,
      sectionId = current.getAttribute("id"),
      sectionsClass = document.querySelector(
        ".nav__menu a[href*=" + sectionId + "]"
      );

    if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
      sectionsClass.classList.add("active-link");
    } else {
      sectionsClass.classList.remove("active-link");
    }
  });
};
window.addEventListener("scroll", scrollActive);

/*=============== DARK LIGHT THEME ===============*/
const themeButton = document.getElementById("theme-button");
const darkTheme = "dark-theme";
const iconTheme = "ri-sun-line";

// Previously selected topic (if user selected)
const selectedTheme = localStorage.getItem("selected-theme");
const selectedIcon = localStorage.getItem("selected-icon");

// We obtain the current theme that the interface has by validating the dark-theme class
const getCurrentTheme = () =>
  document.body.classList.contains(darkTheme) ? "dark" : "light";
const getCurrentIcon = () =>
  themeButton.classList.contains(iconTheme) ? "ri-moon-line" : "ri-sun-line";

// We validate if the user previously chose a topic
if (selectedTheme) {
  // If the validation is fulfilled, we ask what the issue was to know if we activated or deactivated the dark
  document.body.classList[selectedTheme === "dark" ? "add" : "remove"](
    darkTheme
  );
  themeButton.classList[selectedIcon === "ri-moon-line" ? "add" : "remove"](
    iconTheme
  );
}
// Activate / deactivate the theme manually with the button
themeButton.addEventListener("click", () => {
  // Add or remove the dark / icon theme
  document.body.classList.toggle(darkTheme);
  themeButton.classList.toggle(iconTheme);
  // We save the theme and the current icon that the user chose
  localStorage.setItem("selected-theme", getCurrentTheme());
  localStorage.setItem("selected-icon", getCurrentIcon());
});

/*=============== SCROLL REVEAL ANIMATION ===============*/
const sr = ScrollReveal({
  origin: "top",
  distance: "60px",
  duration: 2500,
  delay: 400,
  reset: true,
  //reset:true //Animations repeat
});

sr.reveal(".home__data, .list__container, .join__content, .footer__container", {
  origin: "top",
});
sr.reveal(".home__img", { origin: "bottom" });
sr.reveal(".health__image, .routine__images, follow__img-3", {
  origin: "left",
});
sr.reveal(".health__data, .routine__data, .follow__img4", { origin: "right" });
sr.reveal(".follow__data, .routine__content-1 img", { interval: 100 });

/*=============== Pop-up ===============*/
function showPopup(popupId, titleId, subtitleId, contentId) {
  var popup = document.getElementById(popupId);
  var popupTitle = document.getElementById(titleId);
  var popupSubtitle = document.getElementById(subtitleId);
  var popupContent = document.getElementById(contentId);

  // 設置 .popup-content 的內容
  popupTitle.textContent = popupTitle.textContent;
  popupSubtitle.textContent = popupSubtitle.textContent;
  popupContent.textContent = popupContent.textContent;

  // 顯示 .popup
  popup.style.display = "block";
}

function closePopup(popupId) {
  var popup = document.getElementById(popupId);
  // 隱藏 .popup
  popup.style.display = "none";
}

/*=============== pose-detection ===============*/
function startPoseDetectionA() {
  // 發送 GET 請求到後端端點
  fetch("/warrior_I_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionB() {
  // 發送 GET 請求到後端端點
  fetch("/warrior_II_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionC() {
  // 發送 GET 請求到後端端點
  fetch("/downward_facing_dog")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionD() {
  // 發送 GET 請求到後端端點
  fetch("/chair_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionE() {
  // 發送 GET 請求到後端端點
  fetch("/mountain_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionF() {
  // 發送 GET 請求到後端端點
  fetch("/tree_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionG() {
  // 發送 GET 請求到後端端點
  fetch("/triangle_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionH() {
  // 發送 GET 請求到後端端點
  fetch("/half_moon_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionI() {
  // 發送 GET 請求到後端端點
  fetch("/full_boat_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startPoseDetectionJ() {
  // 發送 GET 請求到後端端點
  fetch("/happy_baby_pose")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

function startYolo() {
  // 發送 GET 請求到後端端點
  fetch("/yolo")
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
}

/*=============== Email ===============*/
function subscribeEmail(event) {
  event.preventDefault(); // 阻止表單默認的提交行為

  var emailInput = document.getElementById("emailInput").value;

  emailjs.init("AlLyqhS21MAXSwLMX"); // 替換成您的 User ID

  emailjs
    .send("yoga2023", "yoga2023", {
      recipient: emailInput,
    })
    .then(
      function (response) {
        console.log("郵件發送成功", response);
        alert("郵件已成功發送至 " + emailInput);
        // 在這裡添加顯示成功消息或其他相應的處理邏輯
      },
      function (error) {
        console.log("郵件發送失敗", error);
        alert("發送郵件時發生錯誤，請稍後再試。");
        // 在這裡添加顯示失敗消息或其他相應的處理邏輯
      }
    );
}

/*==================== 蓮花 ==================== */
function showImage(imageSource) {
  var displayedImage = document.getElementById("displayedImage");
  displayedImage.src = imageSource;
}
