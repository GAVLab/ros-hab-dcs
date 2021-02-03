;; Auto-generated. Do not edit!


(when (boundp 'sensor_msgs_ext::set_axis_home)
  (if (not (find-package "SENSOR_MSGS_EXT"))
    (make-package "SENSOR_MSGS_EXT"))
  (shadow 'set_axis_home (find-package "SENSOR_MSGS_EXT")))
(unless (find-package "SENSOR_MSGS_EXT::SET_AXIS_HOME")
  (make-package "SENSOR_MSGS_EXT::SET_AXIS_HOME"))
(unless (find-package "SENSOR_MSGS_EXT::SET_AXIS_HOMEREQUEST")
  (make-package "SENSOR_MSGS_EXT::SET_AXIS_HOMEREQUEST"))
(unless (find-package "SENSOR_MSGS_EXT::SET_AXIS_HOMERESPONSE")
  (make-package "SENSOR_MSGS_EXT::SET_AXIS_HOMERESPONSE"))

(in-package "ROS")





(defclass sensor_msgs_ext::set_axis_homeRequest
  :super ros::object
  :slots ())

(defmethod sensor_msgs_ext::set_axis_homeRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass sensor_msgs_ext::set_axis_homeResponse
  :super ros::object
  :slots (_success _message ))

(defmethod sensor_msgs_ext::set_axis_homeResponse
  (:init
   (&key
    ((:success __success) nil)
    ((:message __message) "")
    )
   (send-super :init)
   (setq _success __success)
   (setq _message (string __message))
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:message
   (&optional __message)
   (if __message (setq _message __message)) _message)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ;; string _message
    4 (length _message)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;; string _message
       (write-long (length _message) s) (princ _message s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; string _message
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _message (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass sensor_msgs_ext::set_axis_home
  :super ros::object
  :slots ())

(setf (get sensor_msgs_ext::set_axis_home :md5sum-) "937c9679a518e3a18d831e57125ea522")
(setf (get sensor_msgs_ext::set_axis_home :datatype-) "sensor_msgs_ext/set_axis_home")
(setf (get sensor_msgs_ext::set_axis_home :request) sensor_msgs_ext::set_axis_homeRequest)
(setf (get sensor_msgs_ext::set_axis_home :response) sensor_msgs_ext::set_axis_homeResponse)

(defmethod sensor_msgs_ext::set_axis_homeRequest
  (:response () (instance sensor_msgs_ext::set_axis_homeResponse :init)))

(setf (get sensor_msgs_ext::set_axis_homeRequest :md5sum-) "937c9679a518e3a18d831e57125ea522")
(setf (get sensor_msgs_ext::set_axis_homeRequest :datatype-) "sensor_msgs_ext/set_axis_homeRequest")
(setf (get sensor_msgs_ext::set_axis_homeRequest :definition-)
      "# Sets the home position of the axis to it's current position.

---
bool success        # Indicates if the home position was set successfully.
string message      # Provides an error message if unsuccessful.

")

(setf (get sensor_msgs_ext::set_axis_homeResponse :md5sum-) "937c9679a518e3a18d831e57125ea522")
(setf (get sensor_msgs_ext::set_axis_homeResponse :datatype-) "sensor_msgs_ext/set_axis_homeResponse")
(setf (get sensor_msgs_ext::set_axis_homeResponse :definition-)
      "# Sets the home position of the axis to it's current position.

---
bool success        # Indicates if the home position was set successfully.
string message      # Provides an error message if unsuccessful.

")



(provide :sensor_msgs_ext/set_axis_home "937c9679a518e3a18d831e57125ea522")

