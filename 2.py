def function: showHidePassword(elem) {
    const checkbox = elem.querySelector('input[type="checkbox"]');
    const input = elem.querySelector('input[type="password"]');
    checkbox.onchange = () => {
        if (checkbox.checked) {
            elem.classList.add('is-visible')
            elem.classList.remove('is-hidden');
            input.setAttribute('type', 'text');
        } else {
            elem.classList.remove('is-visible');
            elem.classList.add('is-hidden');
            input.setAttribute('type', 'password');
        }
    };