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
		DatagramSocket serverSocket = new DatagramSocket(5000);

		
		String status = "Ligado";
		int temperatura = 30;
		String ip = InetAddress.getLocalHost().getHostAddress();
		String porta = "5001";
		String tipo = "Ar-condicionado";
		
		

		while (true) {
			
			byte[] receiveData = new byte[1024];
			byte[] sendData = new byte[1024];

			DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
			System.out.println("Esperando por datagrama UDP na porta " + 5000);
			serverSocket.receive(receivePacket);

			String sentence = new String(receivePacket.getData());
			System.out.println(sentence);

			InetAddress IPAddress = receivePacket.getAddress();

			int port = receivePacket.getPort();

			String x = "{'tipo':'Ar-condicionado', 'ip': '" + ip + "', 'porta':" + porta + ", 'acoes':{'status': '"
					+ status + "', 'temperatura':" + temperatura + "}}";

			sendData = x.getBytes();

			DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, IPAddress, port);

			System.out.print("Enviando " + x + "...");

			serverSocket.send(sendPacket);
			System.out.println("OK\n");
			serverSocket.close();
			
			serverSocket = new DatagramSocket(5001);
			
			receiveData = new byte[1024];
			sendData = new byte[1024];
			
			receivePacket = new DatagramPacket(receiveData, receiveData.length);
			System.out.println("Esperando por datagrama UDP na porta " + 5001);
			serverSocket.receive(receivePacket);

			sentence = new String(receivePacket.getData());
			System.out.println(sentence);
			JSONObject json = new JSONObject(sentence);
			temperatura = json.getJSONObject("acoes").getInt("temperatura"); 
			status = json.getJSONObject("acoes").getString("status");
			x = "{'tipo':'Ar-condicionado', 'ip': '" + ip + "', 'porta':" + porta + ", 'acoes':{'status': '"
					+ status + "', 'temperatura':" + temperatura + "}}";
			System.out.print("Frase: " + x + "...");


			serverSocket.close();
			break;

		}
		
		


		

	}
}
