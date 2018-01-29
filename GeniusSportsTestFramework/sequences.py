import json

class Sequences:

    def __init__(self):
        with open("4825925.json") as file:
            self.sequences = json.load(file)

    def get_sequenceById(self, sequence_id):
        # Get sequence id, return list of tuples (key,value) in that sequence id
        self.sequence = self.sequences[sequence_id]
        elements = []
        for key in self.sequence.iteritems():
            elements.append(key)
        return elements

    def get_sequencesByType(self, sequence_type):
        # Get all sequences matching sequence_type param; returns list of sequence ids that match
        list_of_ids = []
        for self.sequence in self.sequences:
            if self.sequence is not None:
                if self.sequence['Type'] == sequence_type:
                    list_of_ids.append(self.sequence['SequenceId'])
        # print 'Found ' + str(list_of_ids.__len__()) + ' sequences of type ' + sequence_type
        return list_of_ids

    def get_sequencesGameEvent(self):
        # Return list of GameEvent maps for each in self.sequence
        list_of_events = []
        for self.sequence in self.sequences:
            if self.sequence is not None:
                if self.sequence['GameEvent']:
                    list_of_events.append(self.sequence['GameEvent'])
       # print 'Found ' + str(list_of_events.__len__()) + ' sequences with GameEvent data'
        return list_of_events

    def display(self):
        for index in self.sequences:
            if index is not None:
                print '* ------------------------------------------------------- *'
                print 'Sequence ID:          ' + str(index['SequenceId'])
                print 'Fixture ID:           ' + str(index['FixtureId'])
                print 'Game Event (count):   ' + str(len(index['GameEvent']))
                print 'Source:               ' + str(index['Source'])
                print 'Type:                 ' + str(index['Type'])

if __name__ == '__main__':
    s = Sequences()
    s.get_sequenceById(33)
    s.get_sequencesByType('DangerStateAddedDto')
    s.get_sequencesGameEvent()
    # s.display()