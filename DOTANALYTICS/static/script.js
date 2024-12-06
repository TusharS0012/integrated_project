const formOpenBtn = document.querySelector("#form-open"),
    home = document.querySelector(".home"),
    formContainer = document.querySelector(".form_container"),
    formCloseBtn = document.querySelector(".form_close"),
    signupBtn = document.querySelector("#signup"),
    loginBtn = document.querySelector("#login"),
    forgotPwLink = document.querySelector(".forgot_pw"),
    sendOtpBtn = document.querySelector("#send_otp"),
    loginForm = document.querySelector(".login_form"),
    signupForm = document.querySelector(".signup_form"),
    emailForm = document.querySelector(".email_form"),
    setPasswordForm = document.querySelector(".set_password_form"),
    pwShowHide = document.querySelectorAll(".pw_hide");

formOpenBtn.addEventListener("click", () => home.classList.add("show"));
formCloseBtn.addEventListener("click", () => home.classList.remove("show"));

pwShowHide.forEach((icon) => {
    icon.addEventListener("click", () => {
        let getPwInput = icon.parentElement.querySelector("input");
        if (getPwInput.type === "password") {
            getPwInput.type = "text";
            icon.classList.replace("uil-eye-slash", "uil-eye");
        } else {
            getPwInput.type = "password";
            icon.classList.replace("uil-eye", "uil-eye-slash");
        }
    });
});


signupBtn.addEventListener("click", (e) => {
    e.preventDefault();
    formContainer.classList.add("active");
    signupForm.style.display = "block";
    loginForm.style.display = "none";
    emailForm.style.display = "none";
    setPasswordForm.style.display = "none";
});


loginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    formContainer.classList.remove("active");
    signupForm.style.display = "none";
    loginForm.style.display = "block";
    emailForm.style.display = "none";
    setPasswordForm.style.display = "none";
});


forgotPwLink.addEventListener("click", (e) => {
    e.preventDefault(); 
    formContainer.classList.add("active"); 
    emailForm.style.display = "block"; 
    loginForm.style.display = "none";
    signupForm.style.display = "none"; 
    setPasswordForm.style.display = "none"; 
});


sendOtpBtn.addEventListener("click", (e) => {
    e.preventDefault(); // Prevent form submission

    const emailInput = emailForm.querySelector("input[type='email']");
    const email = emailInput.value;

    if (!email) {
        alert("Please enter your email.");
        return;
    }

    
    emailForm.style.display = "none";
    setPasswordForm.style.display = "block";
});

var nextBtn = document.querySelector('.next'),
    prevBtn = document.querySelector('.prev'),
    carousel = document.querySelector('.carousel'),
    list = document.querySelector('.list'), 
    item = document.querySelectorAll('.item')
nextBtn.onclick = function(){
    showSlider('next')
}
prevBtn.onclick = function(){
    showSlider('prev')
}

function showSlider(type) {
    let sliderItemsDom = list.querySelectorAll('.carousel .list .item')
    if(type === 'next'){
        list.appendChild(sliderItemsDom[0])
        carousel.classList.add('next')
    } else{
        list.prepend(sliderItemsDom[sliderItemsDom.length - 1])
        carousel.classList.add('prev')
    }
  
}

function redirect_AI(url){
    window.location.href = url;
}

