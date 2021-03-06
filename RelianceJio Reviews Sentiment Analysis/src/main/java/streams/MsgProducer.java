package streams;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.io.IOException;
import java.util.Properties;

public class MsgProducer {

    // Declare a new producer
    public static KafkaProducer producer;

    public static void main(String[] args) throws IOException {


        String topic = "/user/mapr/stream:reviews";

        String fileName = "/mapr/demo.mapr.com/user/mapr/data/revsportstream.json";

        if (args.length == 2) {
            topic = args[0];
            fileName = args[1];
        }
        System.out.println("Sending to topic " + topic);
        configureProducer();
        File f = new File(fileName);
        FileReader fr = new FileReader(f);
        BufferedReader reader = new BufferedReader(fr);
        String line = reader.readLine();
        while (line != null) {

            ProducerRecord<String, String> rec = new ProducerRecord<>(topic, line);

            // Send the record to the producer client library.
            producer.send(rec);
         //   System.out.println("Sent message: " + line);
            line = reader.readLine();

        }

        producer.close();
        System.out.println("All done.");

        System.exit(1);

    }

    public static void configureProducer() {
        Properties props = new Properties();
        props.put("key.serializer",
                "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer",
                "org.apache.kafka.common.serialization.StringSerializer");

        producer = new KafkaProducer<>(props);
    }

}
