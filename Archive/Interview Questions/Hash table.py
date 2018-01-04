
table = {}

def Main(table):

    # User defined row count of table, set counters
    rows = int(raw_input("\n\nEnter number of items in hash table:  "))
    c = 0
    base_num = 0
    word_count = 0

    # Loop through number of key/value pairs // if already in dict, skips
    while (c < rows):
        value = raw_input("Enter value of item # %d:  " % (c + 1))
        if value in table.values():
            print 'Already in the table, not adding'
        else:
            table[c] = value

    # Finds word with highest char and prints
        if len(value) > word_count:
            highest_word = value
            word_count = len(value)
        else:
            word_count = word_count
        c+=1
    s = input('Would you like to know word counts?  \n1:  YES\n2:  NO')
    if (s == 1) or (s == 2):
        print '    HIGHEST WORD COUNT       '
        print "#############################"
        print "Word:        ",highest_word
        print "Word count:  ", word_count
        print "#############################"
        print '    OTHER WORD COUNTS    '
        for i in table:
            if table[i] != highest_word:
                print 'Word:     ',table[i]
                print 'Count:    ',len(table[i])
                print ' ---------------------------------------'
            else:
                continue


    else:
        print 'Invalid...'

# Print Table
def PrintTable(table):
    print '|KEY| VALUE|'
    print '----------------------------------------'
    for key in table:
        print '|',key, '|',table[key]
        print '----------------------------------------'

def RemoveByKey(table):
    PrintTable(table)
    remove_item = input('Enter key to remove:  ')
    if isinstance(remove_item, int ):
        r = dict(table)
        del r[remove_item]
        return r
    else:
        print 'Please enter an integer'

def Search(table):
    search_key = int(raw_input("What is the key?  "))
    print "You are looking for ", search_key
    if search_key in table:
        print 'Value for key %d is %s' % (search_key, str(table[search_key]))
    else:
        print '%s cannot be found in this hash table.  Please try again...' % search_key


Main(table)
# PrintTable(table)
# Search(table)
# RemoveByKey(table)
