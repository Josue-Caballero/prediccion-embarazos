
tpbody = document.getElementById('tpbody');
rFile = document.getElementById("input_3_1");
fileSection = document.getElementById("id_9");
inputFile = document.getElementById("input_9")
registriesSection = document.getElementById("id_4");
rRegistries = document.getElementById("input_3_0");
inputRegistries = document.getElementById("input_4")
buttonClear = document.getElementById("button-clear");
buttonPredict = document.getElementById("button-predict");

const getTemplateForRow = function (dataset) {

    let template = "";

    dataset.forEach( (row, idx) => {
        template += `
        <tr>
            <th scope="row">${idx + 1}</th>
            <td>
                ${row ? "<span style='background-color: #B2EA70; padding: 12px; display: inline-block; width: 200px;'>Si<span>" 
                    : "<span style='background-color: #C85C5C; padding: 12px; display: inline-block; width: 200px;'>No<span>"}
            </td>
        </tr>`
    });

    return template;

}

const toggleSection = function(opR, opF, enR, enF) {
    
    fileSection.style.opacity = opF;
    registriesSection.style.opacity = opR;
    inputFile.disabled = enF;
    inputRegistries.disabled = enR;
    inputFile.value = "";
    inputRegistries.value = "";

}

const clearForm = function(e) {

    inputFile.value = "";
    inputRegistries.value = "";
    rRegistries.checked = true;
    tpbody.innerHTML = "";
    toggleSection("1", "0.6", false, true);

}

const fileSelected = function(e) {

    target = e.target;
    
}

const requestFunc = async function(url, method, body) {

    return fetch(url, {
        method: method,
        body: body
    });

}

const showPredictions = async function(response) {

    if(response.status === 200) {
            
        data = await response.json();
        tpbody.innerHTML = "";
        tpbody.innerHTML = getTemplateForRow(data.prediccion);

    }

}

const sendData = async function(e) {

    let file = inputFile.files[0],
        form = new FormData(),
        response = null;

    if(file) {
        
        form.append('file', file);
        response = await requestFunc('/api/v0.1/predict-file/', 'POST', form);
        
        showPredictions(response);

    } else {
        
        validNumber = inputRegistries.value.split('\n').find( e => e.split(',').length != 51);

        if( validNumber || inputRegistries.value == "" ) {
            alert("Los registros ingresados son incorrectos!"); }
        else {

            form.append('registros', inputRegistries.value);
            response = await requestFunc('/api/v0.1/predict-registers/', 'POST', form)
            showPredictions(response);

        }

    }

}

buttonClear.addEventListener('click', clearForm);
buttonPredict.addEventListener('click', sendData);
inputFile.addEventListener('change', fileSelected);
rFile.addEventListener('change', (e) => toggleSection("0.6", "1", true, false) );
rRegistries.addEventListener('change', (e) => toggleSection("1", "0.6", false, true) );
