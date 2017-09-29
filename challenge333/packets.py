import re
import unittest
import sys

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
            self.packets_stream = list()
            self.packets_stream.extend(packets)
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

    def get_all_messages(self):
        for m in self.messages.values():
            yield m

    @staticmethod
    def bootstrap_from_input_file(path):
        packets = list()
        pattern = re.compile("(\d+)\s*(\d+)\s*(\d+)\s*(.*)")
        with open(path, "r") as f:
            for line in f:
                matches = re.match(pattern, line)
                packet = Packet(matches.groups()[0], matches.groups()[1], matches.groups()[2], matches.groups()[3])
                packets.append(packet)    
        return Messages(packets)
            
class PacketAssemblerTests(unittest.TestCase):

    def test_regex_parse_of_packet_text_representation(self):
        pattern = re.compile("(\d+)\s*(\d+)\s*(\d+)\s*(.*)")
        matches = re.match(pattern, "6220    1   10  Because he's the hero Gotham deserves, ")
        packet = Packet(matches.groups()[0], matches.groups()[1], matches.groups()[2], matches.groups()[3])
        self.assertEqual(packet.message_id, 6220)
        self.assertEqual(packet.packet_id, 1)
        self.assertEqual(packet.packet_count, 10)
        self.assertEqual(packet.text, "Because he's the hero Gotham deserves, ")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].lower() == "runtests":
        unittest.main(argv=["First"])
    else:
        messages = Messages.bootstrap_from_input_file("C:\\Users\\joraki\\src\\personal\\daily-programmer\\challenge333\\packets_challenge_input.txt")
        messages.assemble()
        for m in messages.get_all_messages():
            print(m)
        