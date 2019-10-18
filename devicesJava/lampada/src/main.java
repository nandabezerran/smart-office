import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.util.Timer;
import java.util.TimerTask;
import org.json.*;

//Ar-condicionado
public class main {
    public static void main(String args[]) throws IOException, JSONException {
        DatagramSocket serverSocket = new DatagramSocket(null);
        serverSocket.setReuseAddress(true);
        String ip = InetAddress.getLocalHost().getHostAddress();
        InetSocketAddress address = new InetSocketAddress(ip, 5000);
        serverSocket.bind(address);

        String porta = "5002";
        int id = 2;
        String tipo = "TV";
        String status = "Ligado";
        int canal = 30;
        int volume = 30;


        ////////////////// CONEXAO BROADCAST
        byte[] receiveData = new byte[1024];
        byte[] sendData = new byte[1024];

        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        System.out.println("Esperando por datagrama UDP na porta " + 5000);
        serverSocket.receive(receivePacket);

        String sentence = new String(receivePacket.getData());
        System.out.println(sentence);

        InetAddress IPAddress = receivePacket.getAddress();

        int port = receivePacket.getPort();

        String x = "{'id': "+ id +", 'tipo':'lampada', 'ip': '" + ip + "', 'porta':" + porta + ", 'acoes':{'status': '"
                + status + "'}}";

        sendData = x.getBytes();

        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);

        System.out.print("Enviando " + x + "...");

        serverSocket.send(sendPacket);
        System.out.println("OK\n");
        //serverSocket.close();
        serverSocket = new DatagramSocket(5002);


        while (true) {

            ////////////////// TESTANDO RECEBER
            receiveData = new byte[1024];
            sendData = new byte[1024];

            receivePacket = new DatagramPacket(receiveData, receiveData.length);
            System.out.println("Esperando por datagrama UDP na porta " + porta);
            serverSocket.receive(receivePacket);

            sentence = new String(receivePacket.getData());
            System.out.println(sentence);


        }
    }
}