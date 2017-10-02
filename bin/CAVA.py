#!/env/bin/python


from __future__ import division
from optparse import OptionParser
from cava.main import main


ver = 'v1.3.0_alpha'


# Command line argument parsing
descr = 'CAVA (Clinical Annotation of VAriants) ' + ver + ' is a lightweight, fast and flexible NGS variant annotation tool that provides consistent transcript-level annotation.'
epilog = '\nExample usage: path/to/cava/CAVA.py -c config.txt -i input.vcf -o output\n\n'
OptionParser.format_epilog = lambda self, formatter: self.epilog

parser = OptionParser(usage='python path/to/cava/CAVA.py <options>', version=ver, description=descr, epilog=epilog)
parser.add_option('-i', "--in", default='input.vcf', dest='input', action='store',
                      help="Input file name [default value: %default]")
parser.add_option('-o', "--out", default='output', dest='output', action='store',
                      help="Output file name prefix [default value: %default]")
parser.add_option('-c', "--config", default=None, dest='conf', action='store',
                      help="Configuration file name")
parser.add_option('-s', "--stdout", default=False, dest='stdout', action='store_true',
                      help="Write output to standard output [default value: %default]")
parser.add_option('-t', "--threads", default=1, dest='threads', action='store',
                      help="Number of threads [default value: %default]")
(copts, args) = parser.parse_args()

main(ver, copts)