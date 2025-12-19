import pyns
from pyns.nsentity import EntityType
from matplotlib import pyplot
import numpy

input_file = "data/sample_data_set.nev"
# input_file = "datafile0001.nev" # default location for sample data is ../Users/../Trellis/sampleData

nsfile = pyns.NSFile(input_file)

event_entities = [e for e in nsfile.get_entities(EntityType.event)]
entity = event_entities[0]

last_ts = 0
curr_ts = 0

diff = numpy.zeros(entity.item_count - 1)
for index in range(0, entity.item_count):
    data = entity.get_event_data(index)
    curr_ts = data[0]
    if last_ts == 0:
        last_ts = data[0]
        continue
    diff[index-1] = last_ts - curr_ts
    if curr_ts < last_ts:
        print('{0}: {1}'.format(index-1, last_ts))
        print('{0}: {1}'.format(index, curr_ts))

pyplot.hist(diff, 1000)
pyplot.show()