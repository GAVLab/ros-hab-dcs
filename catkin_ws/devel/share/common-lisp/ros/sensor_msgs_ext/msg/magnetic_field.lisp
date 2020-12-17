; Auto-generated. Do not edit!


(cl:in-package sensor_msgs_ext-msg)


;//! \htmlinclude magnetic_field.msg.html

(cl:defclass <magnetic_field> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0))
)

(cl:defclass magnetic_field (<magnetic_field>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <magnetic_field>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'magnetic_field)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name sensor_msgs_ext-msg:<magnetic_field> is deprecated: use sensor_msgs_ext-msg:magnetic_field instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <magnetic_field>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_msgs_ext-msg:x-val is deprecated.  Use sensor_msgs_ext-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <magnetic_field>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_msgs_ext-msg:y-val is deprecated.  Use sensor_msgs_ext-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <magnetic_field>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader sensor_msgs_ext-msg:z-val is deprecated.  Use sensor_msgs_ext-msg:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <magnetic_field>) ostream)
  "Serializes a message object of type '<magnetic_field>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <magnetic_field>) istream)
  "Deserializes a message object of type '<magnetic_field>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<magnetic_field>)))
  "Returns string type for a message object of type '<magnetic_field>"
  "sensor_msgs_ext/magnetic_field")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'magnetic_field)))
  "Returns string type for a message object of type 'magnetic_field"
  "sensor_msgs_ext/magnetic_field")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<magnetic_field>)))
  "Returns md5sum for a message object of type '<magnetic_field>"
  "4a842b65f413084dc2b10fb484ea7f17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'magnetic_field)))
  "Returns md5sum for a message object of type 'magnetic_field"
  "4a842b65f413084dc2b10fb484ea7f17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<magnetic_field>)))
  "Returns full string definition for message of type '<magnetic_field>"
  (cl:format cl:nil "# A 3D measurement of the local magnetic field.~%~%float64 x           # The magnetic field strength in the X direction [T]~%float64 y           # The magnetic field strength in the Y direction [T]~%float64 z           # The magnetic field strength in the Z direction [T]~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'magnetic_field)))
  "Returns full string definition for message of type 'magnetic_field"
  (cl:format cl:nil "# A 3D measurement of the local magnetic field.~%~%float64 x           # The magnetic field strength in the X direction [T]~%float64 y           # The magnetic field strength in the Y direction [T]~%float64 z           # The magnetic field strength in the Z direction [T]~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <magnetic_field>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <magnetic_field>))
  "Converts a ROS message object to a list"
  (cl:list 'magnetic_field
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
))
