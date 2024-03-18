from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self,routing_key,exchange_name):
        super().__init__(routing_key,exchange_name)
    
