# Simple script to demonstrate how to write a pipeline using generator functions in python
# Code credits: https://brett.is/writing/about/generator-pipelines-in-python/


class LogProcessor:
    def __init__(self, file):
        self._file = file
        self._filters = []
    def add_filter(self, new_filter):
        if callable(new_filter):
            self._filters.append(new_filter)
    def process(self):
        # this is the pattern for creating a generator
        # pipeline, we start with a generator then wrap
        # each consecutive generator with the pipeline itself
        pipeline = self._file
        for new_filter in self._filters:
            pipeline = new_filter(pipeline)
        
        print("Pipeline gen: ", pipeline)
        
        return pipeline

def parser(lines):
    """
    Split each line based on spaces and
    yield the resulting list.
    """
    
    print("Inside parser func: ",lines)
    
    for line in lines:
        yield [part.strip('"[]') for part in line.split(' ')]

def mapper(lines):
    """
    Convert each line to a dict
    """
    
    print("Inside mapper func: ",lines)

    for line in lines:
        tmp = {}
        tmp['ip_address'] = line[0]
        tmp['timestamp'] = line[1]
        tmp['timezone'] = line[2]
        tmp['method'] = line[3]
        tmp['request'] = line[4]
        tmp['version'] = line[5]
        tmp['status'] = int(line[6])
        tmp['size'] = int(line[7])
        yield tmp

def status_filter(lines):
    """
    Filter out lines whose status
    code is not 200
    """

    print("Inside status_filter func: ",lines)
    
    for line in lines:
        # is the status is not 200
        # then the line is ignored
        # and does not make it through
        # the pipeline to the end
        if line['status'] == 200:
            yield line

def method_filter(lines):
    """
    Filter out lines whose method
    is not 'GET'
    """

    print("Inside method_filter func: ",lines)
    
    for line in lines:
        # all lines with method not equal
        # to 'get' are dropped
        if line['method'].lower() == 'get':
            yield line

def size_converter(lines):
    """Convert the size (in bytes)
    into megabytes
    """

    print("Inside size_converter func: ",lines)
    
    mb = 9.53674e-7
    for line in lines:
        line['size'] = line['size'] * mb
        yield line

# setup the processor
with open('./sample.log') as log:
    processor = LogProcessor(log)

    # this is the order we want the functions to run
    processor.add_filter(parser)
    processor.add_filter(mapper)
    processor.add_filter(status_filter)
    processor.add_filter(method_filter)
    processor.add_filter(size_converter)

    # process() returns the generator pipeline
    for line in processor.process():
        # line with be a dict whose status is
        # 200 and method is 'GET' and whose
        # size is expressed in megabytes
        print(line)
