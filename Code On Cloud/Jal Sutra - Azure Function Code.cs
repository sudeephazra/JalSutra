#r "Newtonsoft.Json"
#r "Microsoft.ServiceBus"

using System.Configuration;
using System.Text;
using System.Net;
using Microsoft.Azure.Devices;
using Newtonsoft.Json;
using System;

public static async Task Run(string myEventHubMessage, TraceWriter log)
{
    Microsoft.Azure.Devices.ServiceClient client = ServiceClient.CreateFromConnectionString("HostName=Caliber-IoTHub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=TA+nqHDHYARyKPSr/DiW1kt/NXohzThW56BOFwvM5V8=");
    // {"time":"2018-05-14T16:05:45.4920000Z","temperature":32.0,"humidity":68.0,"rain_chance":52.8176546096802,"scored_label":"Yes","soilmoisture":0.0,"israining":1.0}
    var definition = new { time = "", temperature = 0.0, humidity = 0.0, rain_chance = 0.0, scored_label = "", soilmoisture = 0.0, israining = 0.0 };
    log.Info($"C# Event Hub trigger function processed a message: {myEventHubMessage}");
    var data_feed = JsonConvert.DeserializeAnonymousType(myEventHubMessage, definition);
    var rain_chance_threshold = 70.0;

    // cloud-to-device message 
    var msg = JsonConvert.SerializeObject(new { startPumping = 1, startDraining = 1 });
    var c2dmsg = new Microsoft.Azure.Devices.Message(Encoding.ASCII.GetBytes(msg));

    // send AMQP message
    log.Info($"Sending message to device: {msg}");
    // **** Add switching logic here
    if (data_feed.soilmoisture == 0.0 && data_feed.rain_chance > rain_chance_threshold && data_feed.israining == 1.0)
	{
		c2dmsg.Properties.Add("startPumping", "0");
		c2dmsg.Properties.Add("startDraining", "0");
	}
	else if (data_feed.soilmoisture == 0.0 && data_feed.rain_chance < rain_chance_threshold && data_feed.israining == 1.0)
	{
		c2dmsg.Properties.Add("startPumping", "1");
		c2dmsg.Properties.Add("startDraining", "0");
	}   
	else if (data_feed.soilmoisture == 0.0 && data_feed.israining == 0.0)
	{
		c2dmsg.Properties.Add("startPumping", "0");
		c2dmsg.Properties.Add("startDraining", "0");
	}
	else if (data_feed.soilmoisture == 1.0 && data_feed.israining == 0.0)
	{
		c2dmsg.Properties.Add("startPumping", "0");
		c2dmsg.Properties.Add("startDraining", "1");
	}
	else
	{
		c2dmsg.Properties.Add("startPumping", "0");
		c2dmsg.Properties.Add("startDraining", "0");
    }

    //***** Add switching logic here
    await client.SendAsync("raspberrypi3", c2dmsg);
    c2dmsg.Dispose();
    client.CloseAsync ();
}
