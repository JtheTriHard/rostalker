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
def backward():
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
def stop():
	outMsg = "z"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "z sent"
	return 'Stop'

@app.route('/on')
def on():
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
def manual():
	outMsg = "m"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "m sent"
	return 'Manual Mode'

@app.route('/kitchen')
def kitchen():
	outMsg = "k"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "k sent"
	return 'Kitchen'

@app.route('/office')
def office():
	outMsg = "i"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "i sent"
	return 'Office'

@app.route('/follow')
def follow():
	outMsg = "c"
	rospy.loginfo(outMsg)
	pub.publisher(outMsg)
	print "c sent"
	return 'Follow'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')


