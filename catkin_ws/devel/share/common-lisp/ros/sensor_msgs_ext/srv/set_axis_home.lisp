; Auto-generated. Do not edit!


(cl:in-package sensor_msgs_ext-srv)


;//! \htmlinclude set_axis_home-request.msg.html

(cl:defclass <set_axis_home-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass set_axis_home-request (<set_axis_home-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <set_axis_home-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'set_axis_home-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor_msgs_ext-srv:<set_axis_home-request> is deprecated: use sensor_msgs_ext-srv:set_axis_home-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <set_axis_home-request>) ostream)
  "Serializes a message object of type '<set_axis_home-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <set_axis_home-request>) istream)
  "Deserializes a message object of type '<set_axis_home-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<set_axis_home-request>)))
  "Returns string type for a service object of type '<set_axis_home-request>"
  "sensor_msgs_ext/set_axis_homeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'set_axis_home-request)))
  "Returns string type for a service object of type 'set_axis_home-request"
  "sensor_msgs_ext/set_axis_homeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<set_axis_home-request>)))
  "Returns md5sum for a message object of type '<set_axis_home-request>"
  "937c9679a518e3a18d831e57125ea522")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'set_axis_home-request)))
  "Returns md5sum for a message object of type 'set_axis_home-request"
  "937c9679a518e3a18d831e57125ea522")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<set_axis_home-request>)))
  "Returns full string definition for message of type '<set_axis_home-request>"
  (cl:format cl:nil "# Sets the home position of the axis to it's current position.~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'set_axis_home-request)))
  "Returns full string definition for message of type 'set_axis_home-request"
  (cl:format cl:nil "# Sets the home position of the axis to it's current position.~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <set_axis_home-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <set_axis_home-request>))
  "Converts a ROS message object to a list"
  (cl:list 'set_axis_home-request
))
;//! \htmlinclude set_axis_home-response.msg.html

(cl:defclass <set_axis_home-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil)
   (message
    :reader message
    :initarg :message
    :type cl:string
    :initform ""))
)

(cl:defclass set_axis_home-response (<set_axis_home-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <set_axis_home-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'set_axis_home-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor_msgs_ext-srv:<set_axis_home-response> is deprecated: use sensor_msgs_ext-srv:set_axis_home-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <set_axis_home-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_msgs_ext-srv:success-val is deprecated.  Use sensor_msgs_ext-srv:success instead.")
  (success m))

(cl:ensure-generic-function 'message-val :lambda-list '(m))
(cl:defmethod message-val ((m <set_axis_home-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_msgs_ext-srv:message-val is deprecated.  Use sensor_msgs_ext-srv:message instead.")
  (message m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <set_axis_home-response>) ostream)
  "Serializes a message object of type '<set_axis_home-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'message))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'message))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <set_axis_home-response>) istream)
  "Deserializes a message object of type '<set_axis_home-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'message) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'message) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<set_axis_home-response>)))
  "Returns string type for a service object of type '<set_axis_home-response>"
  "sensor_msgs_ext/set_axis_homeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'set_axis_home-response)))
  "Returns string type for a service object of type 'set_axis_home-response"
  "sensor_msgs_ext/set_axis_homeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<set_axis_home-response>)))
  "Returns md5sum for a message object of type '<set_axis_home-response>"
  "937c9679a518e3a18d831e57125ea522")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'set_axis_home-response)))
  "Returns md5sum for a message object of type 'set_axis_home-response"
  "937c9679a518e3a18d831e57125ea522")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<set_axis_home-response>)))
  "Returns full string definition for message of type '<set_axis_home-response>"
  (cl:format cl:nil "bool success        # Indicates if the home position was set successfully.~%string message      # Provides an error message if unsuccessful.~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'set_axis_home-response)))
  "Returns full string definition for message of type 'set_axis_home-response"
  (cl:format cl:nil "bool success        # Indicates if the home position was set successfully.~%string message      # Provides an error message if unsuccessful.~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <set_axis_home-response>))
  (cl:+ 0
     1
     4 (cl:length (cl:slot-value msg 'message))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <set_axis_home-response>))
  "Converts a ROS message object to a list"
  (cl:list 'set_axis_home-response
    (cl:cons ':success (success msg))
    (cl:cons ':message (message msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'set_axis_home)))
  'set_axis_home-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'set_axis_home)))
  'set_axis_home-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'set_axis_home)))
  "Returns string type for a service object of type '<set_axis_home>"
  "sensor_msgs_ext/set_axis_home")