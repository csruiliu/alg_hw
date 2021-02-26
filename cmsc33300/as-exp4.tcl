set ns [new Simulator]

set queuevar1 [lindex $argv 0]

#set nf [open as_out.nam w]
#$ns namtrace-all $nf

set tf [open as_exp4_out.tr w]
$ns trace-all $tf

proc finish {} {
    global ns tf
    $ns flush-trace
    #close $nf
    close $tf
    #exec nam as_out.nam &
    exit 0
}

#create 8 nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]

#create links and form the network topology
$ns duplex-link $n2 $n3 1.5Mb 10ms $queuevar1
$ns duplex-link $n0 $n2 10Mb 10ms $queuevar1
$ns duplex-link $n1 $n2 10Mb 10ms $queuevar1
$ns duplex-link $n6 $n2 1.5Mb 10ms $queuevar1
$ns duplex-link $n3 $n4 10Mb 10ms $queuevar1
$ns duplex-link $n3 $n5 10Mb 10ms $queuevar1
$ns duplex-link $n3 $n7 1.5Mb 10ms $queuevar1

#for better layout 
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n0 $n2 orient right-down 
$ns duplex-link-op $n1 $n2 orient right-up 
$ns duplex-link-op $n6 $n2 orient right 
$ns duplex-link-op $n3 $n4 orient right-up 
$ns duplex-link-op $n3 $n5 orient right-down
$ns duplex-link-op $n3 $n7 orient right 

#create udp1, attach agenet to n6 and sink at n2
set udp1 [new Agent/UDP]
$udp1 set fid_ 1
$ns attach-agent $n6 $udp1
set null1 [new Agent/Null] 
$ns attach-agent $n7 $null1
$ns connect $udp1 $null1

#create udp2, attach agenet to n2 and sink at n3
set udp2 [new Agent/UDP]
$udp2 set fid_ 2
$ns attach-agent $n6 $udp2
set null2 [new Agent/Null] 
$ns attach-agent $n7 $null2
$ns connect $udp2 $null2

#create udp3, attach agenet to n3 and sink at n7
set udp3 [new Agent/UDP]
$udp3 set fid_ 3
$ns attach-agent $n6 $udp3
set null3 [new Agent/Null] 
$ns attach-agent $n7 $null3
$ns connect $udp3 $null3

#create CBR as the traffic for udp1
set cbr1 [new Application/Traffic/CBR]
$cbr1 attach-agent $udp1
$cbr1 set type_ CBR
$cbr1 set packet_size_ 1000
$cbr1 set rate_ 1Mb
$cbr1 set random_ false

#create CBR as the traffic for udp2
set cbr2 [new Application/Traffic/CBR]
$cbr2 attach-agent $udp2
$cbr2 set type_ CBR
$cbr2 set packet_size_ 1000
$cbr2 set rate_ 1Mb
$cbr2 set random_ false

#create CBR as the traffic for udp3
set cbr3 [new Application/Traffic/CBR]
$cbr3 attach-agent $udp3
$cbr3 set type_ CBR
$cbr3 set packet_size_ 500
$cbr3 set rate_ 0.6Mb
$cbr3 set random_ false

$ns at 0 "$cbr1 start"
$ns at 2.0 "$cbr1 stop"

$ns at 0.1 "$cbr2 start"
$ns at 2.0 "$cbr2 stop"

$ns at 0.2 "$cbr3 start"
$ns at 2.0 "$cbr3 stop"

$ns at 2.1 "finish"

$ns run