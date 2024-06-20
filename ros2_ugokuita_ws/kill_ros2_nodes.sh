#!/bin/bash
echo "kill all ros2 nodes"
ps aux | grep ros | grep -v grep | awk '{print "kill -9", $2}' | sh
exit 0