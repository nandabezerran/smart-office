import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.util.Timer;
import java.util.TimerTask;
import org.json.*;

import java.util.Timer;
import java.util.TimerTask;
//Ar-condicionado
public class main {

    static byte[] sendData = new byte[1024];
    static DatagramPacket sendPacket;
    static DatagramSocket serverSocket;


    public static void main(String args[]) throws IOException, JSONException {

        serverSocket = new DatagramSocket(null);
        serverSocket.setReuseAddress(true);
        String ip = InetAddress.getLocalHost().getHostAddress();
        InetSocketAddress address = new InetSocketAddress(ip, 5000);

        serverSocket.bind(address);
        String porta = "5001";
        int id = 1;
        String tipo = "Ar-condicionado";
        String status = "Ligado";
        int temperatura = 30;


        ////////////////// CONEXAO BROADCAST
        byte[] receiveData = new byte[1024];

        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        System.out.println("Esperando por datagrama UDP na porta " + 5000);
        serverSocket.receive(receivePacket);

        String sentence = new String(receivePacket.getData());
        System.out.println(sentence);

        InetAddress IPAddress = receivePacket.getAddress();

        int port = receivePacket.getPort();

        String x = "{'id': "+ id +", 'tipo':'Ar-condicionado', 'ip': '" + ip + "', 'porta':" + porta + ", 'acoes':{'status': '"
                + status + "', 'temperatura':" + temperatura + "}}";

        sendData = x.getBytes();

        sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);

        System.out.print("Enviando " + x + "...");

        serverSocket.send(sendPacket);
        System.out.println("OK\n");
        serverSocket.close();
        serverSocket = new DatagramSocket(5001);


        TimerTask task = new TimerTask() {
            @Override
            public void run() {
                System.out.print("temperatura eneviada\n");
                String p = "{'id': "+ id +", 'tipo':'Ar-condicionado', 'ip': '" + ip + "', 'porta':" + porta + ", 'acoes':{'status': '"
                        + status + "', 'temperatura':" + temperatura + "}}";

                sendData = p.getBytes();

                sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);

                System.out.print("Enviando " + x + "...");

                try {
                    serverSocket.send(sendPacket);
                }
                catch(IOException e) {
                    e.printStackTrace();
                }
            };
        };

        Timer timer = new Timer();
        long delay = 0;
        long intevalPeriod = 1 * 90000;
        // schedules the task to be run in an interval
        timer.scheduleAtFixedRate(task, delay,	intevalPeriod);

        while (true) {


            ////////////////// TESTANDO RECEBER
            receiveData = new byte[1024];
            sendData = new byte[1024];

            receivePacket = new DatagramPacket(receiveData, receiveData.length);
            System.out.println("Esperando por datagrama UDP na porta " + 5001);
            serverSocket.receive(receivePacket);

            sentence = new String(receivePacket.getData());
            System.out.println(sentence);



//            System.out.print("Enviando " + x + "...");
//            JSONObject json = new JSONObject(sentence);
//            temperatura = json.getJSONObject("acoes").getInt("temperatura");
//            status = json.getJSONObject("acoes").getString("status");
//            // x = "{'tipo':'Ar-condicionado', 'ip': '" + ip + "', 'porta':" + porta + ", 'acoes':{'status': '"
//            // 		+ status + "', 'temperatura':" + temperatura + "}}";
//            System.out.print("Frase: ");


//            serverSocket.close();
//            break;
        }
    }
}