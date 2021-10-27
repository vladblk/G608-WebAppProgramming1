const signUpBtn = document.querySelector('.btn-primary');
const cancelBtn = document.querySelector('.btn-secondary');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');
const passwordRepeatInput = document.querySelector('#passwordRepeat');
const form = document.querySelector('.container__form');

function User(name, email, pass, repeatPass) {
  this.name = name;
  this.email = email;
  this.pass = pass;
  this.repeatPass = repeatPass;
};

signUpBtn.addEventListener('click', (e) => {
  e.preventDefault();

  const formData = {
    name: nameInput.value,
    email: emailInput.value,
    password: passwordInput.value,
    passwordRepeat: passwordRepeatInput.value
  };

  fetch('http://example.com/movies.json')
    .catch(() => {
      console.log('Success!');

      const user = new User(formData.name, formData.email, formData.password, formData.passwordRepeat);

      console.log(user);
    })
});

cancelBtn.addEventListener('click', (e) => {
  e.preventDefault();

  const html = `
    <div class="cancel">
      <p>'Warning! You are about to reset your inputs. Are you sure you want to continue?'</p>
    </div>
  `;

  form.insertAdjacentHTML('beforeend', html);
})