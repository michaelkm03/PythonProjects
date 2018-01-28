import json

class JSON:

    def __init__(self):
        with open("5104402.json") as file:
            self.sequences = json.load(file)

    def get_sequenceById(self, sequence_id):
        # Get sequence id, return list of tuples (key,value) in that sequence id
        self.sequence = self.sequences[sequence_id]
        elements = []
        for key in self.sequence.iteritems():
            elements.append(key)
            print key
        return elements

    def get_sequencesByType(self, sequence_type):
        list_of_ids = []
        for self.sequence in self.sequences:
            if self.sequence is not None:
                if self.sequence['Type'] == sequence_type:
                    list_of_ids.append(self.sequence['SequenceId'])
        print 'Found ' + str(list_of_ids.__len__()) + ' sequences of type ' + sequence_type
        return list_of_ids

    def get_sequencesGameEvent(self):
        list_of_ids = []
        list_of_events = []
        for self.sequence in self.sequences:
            if self.sequence is not None:
                if self.sequence['GameEvent']:
                    list_of_ids.append(self.sequence['SequenceId'])
                    list_of_events.append(self.sequence['GameEvent'])
        print 'Found ' + str(list_of_ids.__len__()) + ' sequences with GameEvent data'
        return list_of_events

if __name__ == '__main__':
    j = JSON()
    j.get_sequenceById(334)
    j.get_sequencesByType('DangerStateAddedDto')
    j.get_sequencesGameEvent()