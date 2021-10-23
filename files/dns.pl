#!/usr/bin/perl

delete @ENV{qw(PATH)};
$ENV{PATH} = '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/sbin';

# Use Cloudflare DNS servers by default.
$name = $ARGV[0] // "example.com";
$server4 = $ARGV[1] // "1.1.1.1";
$server6 = $ARGV[2] // "2606:4700:4700::1111";

# Sanitize input.
($name) = $name =~ /^([\w.-]+)$/;
($server4) = $server4 =~ /^([\w.-]+)$/;
($server6) = $server6 =~ /^([\w.-:]+)$/;

# Perform IPv4 query for IPv4 address
open(PROCESS, "host -v4t A $name $server4 |");
foreach (<PROCESS>) {
  if ($_ =~ /^Received\s+.*\s+in\s+(\d+)\s+ms$/) {
    $latency4 = $1;
  }
}
close(PROCESS);

# Perform IPv6 query for IPv6 address
open(PROCESS, "host -v6t AAAA $name $server6 |");
foreach (<PROCESS>) {
  if ($_ =~ /^Received\s+.*\s+in\s+(\d+)\s+ms$/) {
    $latency6 = $1;
  }
}
close(PROCESS);

if (defined $latency4 and defined $latency6) {
  print "IPv4:" . $latency4 . " IPv6:" . $latency6 . "\n";
}
