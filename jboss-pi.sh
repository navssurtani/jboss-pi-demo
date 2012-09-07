# ---------------------------------------------------------------------------------------------------------------
# -------------------- Script to start up JBoss on a Raspberry Pi. ----------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------
# -------------------- This script is designed to take in 3 parameters. -----------------------------------------
# ---------------------------------------------------------------------------------------------------------------

export JBOSS_EAP_HOME=$1
export IP_ADDRESS=$2
export JBOSS_NODE_NAME=$3

clear

echo 'JBoss EAP home is: ' 
echo $JBOSS_EAP_HOME

echo 'IP address is: '
echo $IP_ADDRESS

echo 'JBoss node name is: '
echo $JBOSS_NODE_NAME

$JBOSS_EAP_HOME/bin/standalone.sh -c standalone-full-ha.xml -b=$IP_ADDRESS -bmanagement=$IP_ADDRESS -u=230.0.0.4 -Djboss.node.name=$JBOSS_NODE_NAME

