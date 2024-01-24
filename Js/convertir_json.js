form = document.querySelector('#user_create')
inputs = document.querySelectorAll('input')

function getFormData(inputs){
    formData = {}
    inputs.forEach(input, () => {
        formData[input.name] = input.value;
    });
    return formData
}

form.addEventListener('submit', (e) =>{
    e.preventDefault();
    getFormData(inputs)
})