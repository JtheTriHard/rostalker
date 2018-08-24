#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

from flask import Flask
import time
from time import sleep
import rospy
from std_msgs.msg import String
import threading

app = Flask(__name__)

threading.Thread(target=lambda: rospy.init_node('test_node',disable_signals=True)).start()
pub = rospy.Publisher('test_pub', String, queue_size=1)

@app.route('/')
def index():
	return 'Empty Request'

@app.route('/forward')
def forward():
	outMsg = "w"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "w sent"
	return 'Forward'

@app.route('/left')
def left():
	outMsg = "a"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "a sent"
	return 'Left'

@app.route('/right')
def right():
	outMsg = "d"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "d sent"
	return 'Right'

@app.route('/backward')
def forward():
	outMsg = "s"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "s sent"
	return 'Backward'

@app.route('/rightturn')
def rightturn():
	outMsg = "r"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "r sent"
	return 'Right Turn'

@app.route('/leftturn')
def leftturn():
	outMsg = "l"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "l sent"
	return 'Left Turn'

@app.route('/stop')
def forward():
	outMsg = "z"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "z sent"
	return 'Stop'

@app.route('/on')
def forward():
	outMsg = "o"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "o sent"
	return 'On'

@app.route('/off')
def off():
	outMsg = "f"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "f sent"
	return 'Off'
	
@app.route('/manual')
def forward():
	outMsg = "m"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "m sent"
	return 'Manual Mode'

if __name__ == '__main__':
app.run(debug=True, host='0.0.0.0')


