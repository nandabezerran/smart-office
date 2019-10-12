//TODO: Possiveis mudanças nos tipos de envio e recebimento das msgs
var devices = [{
        "tipo": "Ar-condicionado",
        "ip": "adosihdaiosddios",
        "id": "1",
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
            "temperatura": 30,
        }
    },
    {
        "tipo": "TV",
        "ip": "adosihdaiosddios",
        "id": "2",
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
            "canal": 30,
            "volume": 20
        }
    },
    {
        "tipo": "Lâmpada",
        "ip": "adosihdaiosddios",
        "id": "3",
        "porta": 3000,
        "acoes": {
            "status": "Ligado",
        }
    },
    {
        "tipo": "Lâmpada",
        "ip": "adosihdaiosddios",
        "id": "5",
        "porta": 3000,
        "acoes": {
            "status": "Desligado", // true: ligado e false: desligado
        }
    },

];

const server = "localhost:3000/server/"; //TODO: mudar dados do server aqui

function search_devices() {
    $.ajax({
        type: "GET",
        url: server + "getDevices",
        dataType: "json",
        success: function(msg) {
            // TODO: copiar o conteudo do protocol buffer pro array de devices
            devices = msg.devices //JSON.parse(msg);  //TODO: possivel mudanças
            atualizar_tela();
        }
    });
};

function setStatus(id, status) {
    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.status = status;

            console.log($("#" + id).find(".change_status"));
            // $.ajax({
            //     type: "PUT",
            //     url: server + id + "/" + status,
            //     dataType: "json",
            //     data: device, //JSON.stringify(device), //TODO: talvez precise mudar
            //     success: function(msg) {
            //         // TODO: copiar o conteudo do protocol buffer pro array de devices
            //         // devices = ;
            //         atualizar_tela();
            //     }
            // });
        }
    });
};

function setCanal(e, id) {
    var canal = e.target.value;

    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.canal = canal;
            // $.ajax({
            //     type: "PUT",
            //     url: server + id + "/" + status,
            //     dataType: "json",
            //     data: device, //JSON.stringify(device), //TODO: talvez precise mudar
            //     success: function(msg) {
            //         // TODO: copiar o conteudo do protocol buffer pro array de devices
            //         // devices = ;
            //         atualizar_tela();
            //     }
            // });
        }
    });
};

function setVolume(e, id) {
    var volume = e.target.value;

    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.volume = volume;
            // $.ajax({
            //     type: "PUT",
            //     url: server + id + "/" + status,
            //     dataType: "json",
            //     data: device, //JSON.stringify(device), //TODO: talvez precise mudar
            //     success: function(msg) {
            //         // TODO: copiar o conteudo do protocol buffer pro array de devices
            //         // devices = ;
            //         atualizar_tela();
            //     }
            // });
        }
    });
};

function setTemperatura(e, id) {
    var temperatura = e.target.value;

    devices.forEach((device, index) => {
        if (device["id"] == id) {
            device.acoes.temperatura = temperatura;
            // $.ajax({
            //     type: "PUT",
            //     url: server + id + "/" + status,
            //     dataType: "json",
            //     data: device, //JSON.stringify(device), //TODO: talvez precise mudar
            //     success: function(msg) {
            //         // TODO: copiar o conteudo do protocol buffer pro array de devices
            //         // devices = ;
            //         atualizar_tela();
            //     }
            // });
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
        $("#" + id_linha).append("<div class='col-md-4 mx-auto card' id='" + device.id + "'>" +
            // "<div class='row'>" +
            "<img src = './img/ar-condicionado.png' class='img_devices'>" +
            "<div>" +
            "<h3 class='text-center'>" + device.tipo + "</h3></br>" +
            "<p><strong>STATUS:</strong><span class='change_status'> " + device.acoes.status + "</span></p>" +
            "</div>" +
            "<div>" +
            "<h3 >Ações:</h3>" +
            "<div class='acoes'>" +
            "<label>Status: </label>" +
            "<span>" +
            "<button type='button' class='btn btn-warning btn-sm' onclick='setStatus(" + device.id + ", " + ligado + ")'>Ligar</button>" + //TODO: botar onchange/onclick
            "<button type='button' class='btn btn-dark btn-sm' onclick='setStatus(" + device.id + ", " + desligado + ")'>Desligar</button>" + //TODO: botar onchange/onclick
            "</span>" +
            "</div>" +
            "<div class='acoes'>" +
            "<label for='temperatura'>Temperatura: </label>" +
            "<input type='number' class='input-group-text ' max='30' min='17' name='temperatura' value=" + device.acoes.temperatura + " oninput='setTemperatura(event, " + device.id + ")'></input>" + //TODO: botar oninput
            "</div>" +
            "</div>" +
            "</div>"
        );
    } else if (device.tipo === 'Lâmpada') {
        $("#" + id_linha).append("<div class='col-md-4 mx-auto card' id='" + device.id + "'>" +
            "<img src = './img/lampada.png' class='img_devices'>" +
            "<div>" +
            "<h3 class='text-center'>" + device.tipo + "</h3></br>" +
            "<p><strong>STATUS:</strong><span id='change_status'> " + device.acoes.status + "</span></p>" +
            "</div>" +
            "<div>" +
            "<h3 >Ações:</h3>" +
            "<div class='acoes'>" +
            "<label>Status: </label>" +
            "<span>" +
            "<button type='button' class='btn btn-warning btn-sm' value = 'Ligado' onclick='setStatus(event, " + device.id + ")'>Ligar</button>" + //TODO: botar onchange/onclick
            "<button type='button' class='btn btn-dark btn-sm' value = 'Desligado' onclick='setStatus(event, " + device.id + ")'>Desligar</button>" + //TODO: botar onchange/onclick
            "</span>" +
            "</div>" +
            "</div>" +
            "</div>"
        );
    } else if (device.tipo === 'TV') {
        $("#" + id_linha).append("<div class='col-md-4 mx-auto card' id='" + device.id + "'>" +
            "<img src = './img/tv.png' class='img_devices'>" +
            "<div>" +
            "<h3 class='text-center'>" + device.tipo + "</h3></br>" +
            "<p><strong>STATUS:</strong><span id='change_status'> " + device.acoes.status + "</span></p>" +
            "</div>" +
            "<div>" +
            "<h3 >Ações:</h3>" +
            "<div class='acoes'>" +
            "<label>Status: </label>" +
            "<span>" +
            "<button type='button' class='btn btn-warning btn-sm' value = 'Ligado' onclick='setStatus(event," + device.id + ")'>Ligar</button>" + //TODO: botar onchange/onclick
            "<button type='button' class='btn btn-dark btn-sm' value='Desligado' onclick='setStatus(event," + device.id + ")'>Desligar</button>" + //TODO: botar onchange/onclick
            "</span>" +
            "</div>" +
            "<div class='acoes'>" +
            "<label for='volume'>Volume: </label>" +
            "<input type='number' class='input-group-text ' max='100' min='0' name='volume' value=" + device.acoes.volume + "  oninput='setVolume(event," + device.id + ")'></input>" + //TODO: botar oninput
            "</div>" +
            "<div class='acoes'>" +
            "<label for='canal'>Canal: </label>" +
            "<input type='number' class='input-group-text ' max='50' min='2' name='canal' value=" + device.acoes.canal + "  oninput='setCanal(event," + device.id + ")'></input>" + //TODO: botar oninput
            "</div>" +
            "</div>" +
            "</div>"
        );
    }

}


$("#root").append("<p>CU</p>");
$(document).ready(function() {
    atualizar_tela();
});