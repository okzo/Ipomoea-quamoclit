EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L kbd:SW_PUSH SW1
U 1 1 5E3E4EEB
P 5100 3050
F 0 "SW1" H 5100 3305 50  0000 C CNN
F 1 "SW_PUSH" H 5100 3214 50  0000 C CNN
F 2 "Ipomoea-library:Ipomoea-quamoclit_Board_1U_CherryMX_Hotswap" H 5100 3050 50  0001 C CNN
F 3 "" H 5100 3050 50  0000 C CNN
	1    5100 3050
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J1
U 1 1 5EFD231E
P 5300 2350
F 0 "J1" V 5264 2162 50  0000 R CNN
F 1 "Conn_01x02" V 5173 2162 50  0000 R CNN
F 2 "Ipomoea-library:Ipomoea-quamoclit_Board_1U_TH_2" H 5300 2350 50  0001 C CNN
F 3 "~" H 5300 2350 50  0001 C CNN
	1    5300 2350
	0    -1   -1   0   
$EndComp
Wire Wire Line
	5400 2550 5400 3050
Wire Wire Line
	5300 2550 4800 2550
Wire Wire Line
	4800 2550 4800 3050
$EndSCHEMATC
