const signUpBtn = document.querySelector('.btn-primary');
const cancelBtn = document.querySelector('.btn-secondary');
const nameInput = document.getElementsByClassName('form-control')[0];

const sumOfN = (n) => {
  let sum = 0;

  for (let i = 1; i <= n; i++) {
    sum += i;
  }

  console.log(`Sum of all numbers up to ${n}: ${sum}`);
}

signUpBtn.addEventListener('click', (e) => {
  e.preventDefault();

  let greet = nameInput.value === '' ? '' : `, ${nameInput.value}`;

  console.log(`Congratulations${greet}! You have successfully created an account`);

  sumOfN(50);
});

cancelBtn.addEventListener('click', (e) => {
  e.preventDefault();

  console.log('Warning! You are about to reset your inputs. Are you sure you want to continue?');
})