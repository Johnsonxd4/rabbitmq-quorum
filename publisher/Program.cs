// See https://aka.ms/new-console-template for more information
using EasyNetQ;
using EasyNetQ.Topology;

using (var bus = RabbitHutch.CreateBus("host=localhost;username=mqadmin;password=Admin123XX_")) 
            {
                var input = String.Empty;
                var exchange = new Exchange("testquorum","topic");
                
                var properties = new MessageProperties{
                    Type = nameof(TextMessage)
                };
                var i = 0;
                while(i < 1000)
                {
                var message = new Message<TextMessage>(new TextMessage { Text = i.ToString() },properties);
                    await bus.Advanced.PublishAsync<TextMessage>(exchange,"#",true,message);
                    Console.WriteLine("Message published!");
                    await Task.Delay(2000);
                    i++;
                }
                    
            }

public class TextMessage
{
    public string Text { get; set; } 
}