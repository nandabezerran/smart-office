# escritorio-inteligente

Projeto desenvolvido na disciplina de Sistemas Distribuídos, Departamento de Computação, Universidade Federal do Ceará, com o objetivo de elaborar um ambiente inteligente que possa ser controlado por uma aplicação web.

O ambiente escolhido é composto de dispositivos tais como TV, ar-condicionado e lâmpada, onde os sensores desses dispositivos são simulados por programas.

A estrutura desse projeto é composto pela aplicação web, um servidor/gateway que é encarregado de fazer o meio-termo entre os dispositivos e o cliente, e os dispositivos inteligentes.

---

### Mensagens

As mensagens são feitas em JSON entre cliente e servidor, e entre servidor e devices com strings.

O formato de mensagem elaborado foi, por exemplo, no caso do ar-condicionado:
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

### Dependências

- pip install flask
- pip install flask-cors
- pip install protobuf

---
### Execução

#### Execução devices
1. Use alguma IDE, como o IntelliJ e adicione o pacote java-json.jar como dependência do projeto seguindo as instruções em: https://stackoverflow.com/questions/1051640/correct-way-to-add-external-jars-lib-jar-to-an-intellij-idea-project.
2. Em seguida, basta rodar a aplicação, conforme a IDE.

#### Execução server
1. No terminal, execute: python server/server.py

#### Execução cliente
 1. Basta abrir o arquivo client/index.html em seu browser, ou se preferir, instanciar um servidor na pasta em uma porta, por exemplo com Python através de python -m http.server PORTA, e então em seu browser abrir localhost:porta/

