# smart-office

Project developed at the Distributed Systems course, the objective of this is to create a smart environment that can be controled by a web aplication.

The choosen environment is composed by a couple of devices as a TV, light-bulb and an air-conditioner where the sensors are simulated by programs.

The architecture of this project is composed by a web aplication, a server/gateway that makes the connection between the devices and the client and the smart dispositives.

---

### Mensages 

It is used a JSON to make the communication between the client and server, and the communication between server and devices it is used strings.

Example used for the air-conditioner:

{	tipo: ‘Ar-condicionado’,
	ip: ‘127.0.0.1’,
	porta: 3000,
	id: 1,
	acoes: {	status: ‘Ligado’,
		temperatura: 22 
    }
}


Infelimente, tentamos realizar a comunicação entre cliente e servidor mas não conseguimos, então resolvemos deixar a nossa tentativa registrada através dos comentários. A mensagem  .proto encontra-se na pasta protoBuf e os arquivos gerados para Python e JavaScript em suas respectivas pastas.

---

### Dependeces

- pip install flask
- pip install flask-cors
- pip install protobuf

---
### Execução

#### Devices execution
1. Use alguma IDE, como o IntelliJ e adicione o pacote java-json.jar como dependência do projeto seguindo as instruções em: https://stackoverflow.com/questions/1051640/correct-way-to-add-external-jars-lib-jar-to-an-intellij-idea-project.
2. Em seguida, basta rodar a aplicação, conforme a IDE.

#### Server execution
1. No terminal, execute: python server/server.py

#### Client execution
 1. Basta abrir o arquivo client/index.html em seu browser, ou se preferir, instanciar um servidor na pasta em uma porta, por exemplo com Python através de python -m http.server PORTA, e então em seu browser abrir localhost:porta/

