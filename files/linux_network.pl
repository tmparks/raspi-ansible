#!/usr/bin/perl

delete @ENV{qw(PATH)};
$ENV{PATH} = '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin';

# sanitize input
$val1 = $ARGV[0];
($val1) = $val1 =~ /^([\w.:]+)$/;

# $1 interface
# $2 receive bytes
# $3 receive packets
# $4 receive errs
# $5 receive drop
# $6 receive fifo
# $7 receive frame
# $8 receive compressed
# $9 receive multicast
# $10 transmit bytes
# $11 transmit packets
# $12 transmit errs
# $13 transmit drop
# $14 transmit fifo
# $15 transmit colls
# $16 transmit carrier
# $17 transmit compressed

open(PROCESS, "cat /proc/net/dev | grep -w $val1 |");
foreach (<PROCESS>) {
  if ($_ =~ /($ARGV[0]):\s+(\d+)\s+(\d)+\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)/) {
   print "receive:" . $2 . " transmit:" . $10 . "\n";
  }
}
close(PROCESS);

