import re

class Packet:

    def __init__(self, message_id, packet_id, packet_count, text):
        self.message_id = int(message_id)
        self.packet_id = int(packet_id)
        self.packet_count = int(packet_count)
        self.text = text

    def __str__(self):
        return f"Mid: {self.message_id} Pid: {self.packet_id} Count: {self.packet_count} Text: {self.text}"

class Message:

    def __init__(self, message_id, count):
        self.message_id = message_id
        self.count = count
        self.packets = Message.create_list_of_size(count)
    
    def add_packet(self, packet):
        self.packets[packet.packet_id] = packet

    def __str__(self):
        result = ""
        for p in self.packets:
            result = result + str(p) + "\n"
        return result

    @staticmethod
    def create_list_of_size(count):
        l = list()
        for i in range(count):
            l.append(0)
        return l

class Messages:

    def __init__(self, packets = None):
        if packets == None:
            self.packets_stream = list()
        else:
            self.packets_stream = list().extend(packets)
        self.messages = dict()

    def recieve_packets(self, incoming_packets):
        self.packets_stream.extend(incoming_packets)

    def recieve_packet(self, incoming_packet):
        self.packets_stream.append(incoming_packet)

    def assemble(self):
        for p in self.packets_stream:
            if p.message_id in self.messages:
                self.messages[p.message_id].add_packet(p)
            else:
                self.messages[p.message_id] = Message(p.message_id, p.packet_count)
                self.messages[p.message_id].add_packet(p)


if __name__ == "__main__":
    packets = list()
    pattern = re.compile("(\d+)\s*(\d+)\s*(\d+)\s*(.*)")
    with open("C:\\Users\\joraki\\src\\personal\\daily-programmer\\challenge333\\packets_input_1.txt", "r") as f:
        for line in f:
            matches = re.match(pattern, line)
            packet = Packet(matches.groups()[0], matches.groups()[1], matches.groups()[2], matches.groups()[3])
            packets.append(packet)
    
    messages = Messages()
    messages.recieve_packets(packets)
    messages.assemble()