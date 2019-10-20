var devices = [];
const server = "localhost:2000/"; //TODO: mudar dados do server aqui

function search_devices() {
    $.ajax({
        headers: { "Accept": "application/json" },
        type: "GET",
        crossDomain: true,
        url: "http://localhost:2000/getDevices",
        contentType: 'application/json',
        dataType: 'json',
        beforeSend: function(xhr) {
            xhr.withCredentials = true;
        },
        success: function(msg) {
            devices = msg; //JSON.parse(msg);  //TODO: possivel mudanças
            $("#root").html('<button id="search_devices" type="button" class="btn btn-success text-center" onclick="search_devices()"><strong>Procurar novos dispositivos</strong>      <i class="fas fa-search"></i></button>');
            atualizar_tela();
        }
    });
};

function setStatus(e, id) {
    var status = e.target.value;
    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.status = status;
            $.ajax({
                headers: { "Accept": "application/json" },
                type: "PUT",
                url: 'http://localhost:2000/changeStatus/' + id + "/" + status,
                crossDomain: true,
                dataType: "json",
                data: device,
                contentType: 'application/json',
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.withCredentials = true;
                },
                success: function(msg) {
                    // console.log(msg);
                    $("#" + id).find(".change_status")[0].innerHTML = "  " + status;
                }
            });
        }
    });
};

function setCanal(e, id) {
    var canal = e.target.value;
    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.canal = canal;
            $.ajax({
                headers: { "Accept": "application/json" },
                type: "PUT",
                url: 'http://localhost:2000/changeCanal/' + id + "/" + canal,
                crossDomain: true,
                dataType: "json",
                data: device,
                contentType: 'application/json',
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.withCredentials = true;
                },
                success: function(msg) {
                    // console.log(msg);
                }
            });
        }
    });
};

function setVolume(e, id) {
    var volume = e.target.value;
    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.volume = volume;
            $.ajax({
                headers: { "Accept": "application/json" },
                type: "PUT",
                url: 'http://localhost:2000/changeVolume/' + id + "/" + volume,
                crossDomain: true,
                dataType: "json",
                data: device,
                contentType: 'application/json',
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.withCredentials = true;
                },
                success: function(msg) {
                    // console.log(msg);
                }
            });
        }
    });
};

function setTemperatura(e, id) {
    var temperatura = e.target.value;

    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.temperatura = temperatura;
            $.ajax({
                headers: { "Accept": "application/json" },
                type: "PUT",
                url: 'http://localhost:2000/changeTemp/' + id + "/" + temperatura,
                crossDomain: true,
                dataType: "json",
                data: device,
                contentType: 'application/json',
                dataType: 'json',
                beforeSend: function(xhr) {
                    xhr.withCredentials = true;
                },
                success: function(msg) {
                    // console.log(msg);
                }
            });
        }
    });
};

function atualizar_tela() {
    var id;
    devices.forEach((device, index) => {
        if (index % 2 === 0) { // se for o número par, eu inicio uma nova row
            id = index + 1;
            $("#root").append("<div id = row_" + id + " class='row'> </div>");
        }
        gerar_componente_device(device, "row_" + id);
    });
};

function gerar_componente_device(device, id_linha) {
    var ligado = 'Ligado';
    var desligado = "Desligado";

    if (device.tipo === 'Ar-condicionado') {
        $("#" + id_linha).append("<div class='col-md-5 mx-auto card' id='" + device.id + "'>" +
            "<img src = './img/ar-condicionado.png' class='img_devices'>" +
            "<div>" +
            "<h3 class='text-center tipo-device'>" + device.tipo + "</h3></br>" +
            "<p><strong>STATUS:</strong><span class='change_status'> " + device.acoes.status + "</span></p>" +
            "</div>" +
            "<div>" +
            "<h3 class='text-center'><strong>AÇÕES</strong></h3>" +
            "<div class='acoes'>" +
            "<label><strong>STATUS:</strong> </label>" +
            "<span>" +
            "<button type='button' class='btn btn-warning btn-sm' value='Ligado' onclick='setStatus(event, " + device.id + ")'>Ligar</button>" + //TODO: botar onchange/onclick
            "<button type='button' class='btn btn-danger btn-sm' value='Desligado' onclick='setStatus(event, " + device.id + ")'>Desligar</button>" + //TODO: botar onchange/onclick
            "</span>" +
            "</div>" +
            "<div class='acoes'>" +
            "<label for='temperatura'><strong>TEMPERATURA:</strong> </label>" +
            "<input type='number' class='input-group-text ' max='30' min='17' name='temperatura' value=" + device.acoes.temperatura + " oninput='setTemperatura(event, " + device.id + ")'></input>" + //TODO: botar oninput
            "</div>" +
            "</div>" +
            "</div>"
        );
    } else if (device.tipo === 'lampada') {
        $("#" + id_linha).append("<div class='col-md-5 mx-auto card' id='" + device.id + "'>" +
            "<img src = './img/lampada.png' class='img_devices'>" +
            "<div>" +
            "<h3 class='text-center tipo-device'>Lâmpada</h3></br>" +
            "<p><strong>STATUS:</strong><span class='change_status'> " + device.acoes.status + "</span></p>" +
            "</div>" +
            "<div>" +
            "<h3 class='text-center'><strong>AÇÕES</strong></h3>" +
            "<div class='acoes'>" +
            "<label><strong>STATUS:</strong> </label>" +
            "<span>" +
            "<button type='button' class='btn btn-warning btn-sm' value = 'Ligado' onclick='setStatus(event, " + device.id + ")'>Ligar</button>" + //TODO: botar onchange/onclick
            "<button type='button' class='btn btn-danger btn-sm' value = 'Desligado' onclick='setStatus(event, " + device.id + ")'>Desligar</button>" + //TODO: botar onchange/onclick
            "</span>" +
            "</div>" +
            "</div>" +
            "</div>"
        );
    } else if (device.tipo === 'TV') {
        $("#" + id_linha).append("<div class='col-md-5 mx-auto card' id='" + device.id + "'>" +
            "<img src = './img/tv.png' class='img_devices'>" +
            "<div>" +
            "<h3 class='text-center tipo-device'>" + device.tipo + "</h3></br>" +
            "<p><strong>STATUS:</strong><span class='change_status'> " + device.acoes.status + "</span></p>" +
            "</div>" +
            "<div>" +
            "<h3 class='text-center'><strong>AÇÕES</strong></h3>" +
            "<div class='acoes'>" +
            "<label><strong>STATUS:</strong></label>" +
            "<span>" +
            "<button type='button' class='btn btn-warning btn-sm' value = 'Ligado' onclick='setStatus(event," + device.id + ")'>Ligar</button>" + //TODO: botar onchange/onclick
            "<button type='button' class='btn btn-danger btn-sm' value='Desligado' onclick='setStatus(event," + device.id + ")'>Desligar</button>" + //TODO: botar onchange/onclick
            "</span>" +
            "</div>" +
            "<div class='acoes'>" +
            "<label for='volume'><strong>VOLUME:</strong> </label>" +
            "<input type='number' class='input-group-text ' max='100' min='0' name='volume' value=" + device.acoes.volume + "  oninput='setVolume(event," + device.id + ")'></input>" + //TODO: botar oninput
            "</div>" +
            "<div class='acoes'>" +
            "<label for='canal'><strong>CANAL:</strong> </label>" +
            "<input type='number' class='input-group-text ' max='50' min='2' name='canal' value=" + device.acoes.canal + "  oninput='setCanal(event," + device.id + ")'></input>" + //TODO: botar oninput
            "</div>" +
            "</div>" +
            "</div>"
        );
    }

}
$(document).ready(function() {
    atualizar_tela();
});