;; Auto-generated. Do not edit!


(when (boundp 'sensor_msgs_ext::gnss_position)
  (if (not (find-package "SENSOR_MSGS_EXT"))
    (make-package "SENSOR_MSGS_EXT"))
  (shadow 'gnss_position (find-package "SENSOR_MSGS_EXT")))
(unless (find-package "SENSOR_MSGS_EXT::GNSS_POSITION")
  (make-package "SENSOR_MSGS_EXT::GNSS_POSITION"))

(in-package "ROS")
;;//! \htmlinclude gnss_position.msg.html


(defclass sensor_msgs_ext::gnss_position
  :super ros::object
  :slots (_fix_3d _latitude _longitude _altitude ))

(defmethod sensor_msgs_ext::gnss_position
  (:init
   (&key
    ((:fix_3d __fix_3d) nil)
    ((:latitude __latitude) 0.0)
    ((:longitude __longitude) 0.0)
    ((:altitude __altitude) 0.0)
    )
   (send-super :init)
   (setq _fix_3d __fix_3d)
   (setq _latitude (float __latitude))
   (setq _longitude (float __longitude))
   (setq _altitude (float __altitude))
   self)
  (:fix_3d
   (&optional (__fix_3d :null))
   (if (not (eq __fix_3d :null)) (setq _fix_3d __fix_3d)) _fix_3d)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:serialization-length
   ()
   (+
    ;; bool _fix_3d
    1
    ;; float64 _latitude
    8
    ;; float64 _longitude
    8
    ;; float64 _altitude
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _fix_3d
       (if _fix_3d (write-byte -1 s) (write-byte 0 s))
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _fix_3d
     (setq _fix_3d (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _altitude
     (setq _altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get sensor_msgs_ext::gnss_position :md5sum-) "2e7f35a71c90d67e8708448548aa7e32")
(setf (get sensor_msgs_ext::gnss_position :datatype-) "sensor_msgs_ext/gnss_position")
(setf (get sensor_msgs_ext::gnss_position :definition-)
      "# A global position measurement from a GNSS sensor.

bool fix_3d                 # Indicates if the fix is 3-dimensional (includes altitude).

float64 latitude            # Degrees latitude (positive = N, negative = S).
float64 longitude           # Degrees longitude (positive = E, negative = W).
float64 altitude            # Altitude above MSL [m]
")



(provide :sensor_msgs_ext/gnss_position "2e7f35a71c90d67e8708448548aa7e32")


