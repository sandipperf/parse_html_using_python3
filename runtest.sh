
#!/bin/sh
#Chng_in_OI_CE |Chng_in_OI_PE|IV_CE|IV_PE|LTP_CE|LTP_PE|NetChng_CE|Net_Chng_PE|OI_CE|OI_PE|StrikePrice|Volume_CE|Volume_PE|data_collection_time|nifty_base_price
while :
do
  echo "collecting data from nse"
  mvn gatling:test -X  -Dgatling.simulationClass=Sandip.Sandip_Scn -DrampUpTimeSecs=5 -DNoofXOMusers=1 -DmaxDurationSecs=100 > data.txt
 sleep 100s
  echo "data collected"
sed -n '/<!DOCTYPE/,/<\/html>/p' data.txt > test.html
rm report.csv
python3 parse_data.py test.html report.csv collected_data/2JAN-Option-chain.csv

sleep 400s

done

