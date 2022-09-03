// See https://aka.ms/new-console-template for more information


using EasyNetQ;

static void HandleTextMessage(IMessage<TextMessage> textMessage, MessageReceivedInfo info) 
{
    Console.ForegroundColor = ConsoleColor.Red;
    Console.WriteLine("Got message: {0}", textMessage.Body.Text);
    
    Console.ResetColor();
}
 using (var bus = RabbitHutch.CreateBus("host=localhost;username=mqadmin;password=Admin123XX_")) 
{
    var queue = await bus.Advanced.QueueDeclareAsync("test-quorum-queue",x => {
        x.WithQueueType("quorum");
    });

    var exchange = await bus.Advanced.ExchangeDeclareAsync("testquorum",x => {
        x.WithType("topic");
    });

    var binding = await bus.Advanced.BindAsync(exchange,queue,"#",new Dictionary<string,object>());

    bus.Advanced.Consume<TextMessage>(queue, (x,y) =>HandleTextMessage(x,y));
    
    Console.WriteLine("Listening for messages. Hit <return> to quit.");
    Console.ReadLine();
}