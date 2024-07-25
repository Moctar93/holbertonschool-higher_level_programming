document.addEventListener('DOMContentLoaded', () => {
  const btnTranslate = document.getElementById('btn_translate');
  const languageCode = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  btnTranslate.addEventListener('click', () => {
    const selectedLanguage = languageCode.value;

    if (selectedLanguage) {
      const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`;
      
      fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
          helloDiv.innerText = data.hello;
        })
        .catch(error => {
          helloDiv.innerText = 'Error fetching translation';
          console.error('Error:', error);
        });
    } else {
      helloDiv.innerText = 'Please select a language';
    }
  });
});

