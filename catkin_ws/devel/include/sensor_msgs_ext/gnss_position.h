// Generated by gencpp from file sensor_msgs_ext/gnss_position.msg
// DO NOT EDIT!


#ifndef SENSOR_MSGS_EXT_MESSAGE_GNSS_POSITION_H
#define SENSOR_MSGS_EXT_MESSAGE_GNSS_POSITION_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace sensor_msgs_ext
{
template <class ContainerAllocator>
struct gnss_position_
{
  typedef gnss_position_<ContainerAllocator> Type;

  gnss_position_()
    : fix_3d(false)
    , latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)  {
    }
  gnss_position_(const ContainerAllocator& _alloc)
    : fix_3d(false)
    , latitude(0.0)
    , longitude(0.0)
    , altitude(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _fix_3d_type;
  _fix_3d_type fix_3d;

   typedef double _latitude_type;
  _latitude_type latitude;

   typedef double _longitude_type;
  _longitude_type longitude;

   typedef double _altitude_type;
  _altitude_type altitude;





  typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> const> ConstPtr;

}; // struct gnss_position_

typedef ::sensor_msgs_ext::gnss_position_<std::allocator<void> > gnss_position;

typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_position > gnss_positionPtr;
typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_position const> gnss_positionConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sensor_msgs_ext::gnss_position_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sensor_msgs_ext::gnss_position_<ContainerAllocator1> & lhs, const ::sensor_msgs_ext::gnss_position_<ContainerAllocator2> & rhs)
{
  return lhs.fix_3d == rhs.fix_3d &&
    lhs.latitude == rhs.latitude &&
    lhs.longitude == rhs.longitude &&
    lhs.altitude == rhs.altitude;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sensor_msgs_ext::gnss_position_<ContainerAllocator1> & lhs, const ::sensor_msgs_ext::gnss_position_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sensor_msgs_ext

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2e7f35a71c90d67e8708448548aa7e32";
  }

  static const char* value(const ::sensor_msgs_ext::gnss_position_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2e7f35a71c90d67eULL;
  static const uint64_t static_value2 = 0x8708448548aa7e32ULL;
};

template<class ContainerAllocator>
struct DataType< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensor_msgs_ext/gnss_position";
  }

  static const char* value(const ::sensor_msgs_ext::gnss_position_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# A global position measurement from a GNSS sensor.\n"
"\n"
"bool fix_3d                 # Indicates if the fix is 3-dimensional (includes altitude).\n"
"\n"
"float64 latitude            # Degrees latitude (positive = N, negative = S).\n"
"float64 longitude           # Degrees longitude (positive = E, negative = W).\n"
"float64 altitude            # Altitude above MSL [m]\n"
;
  }

  static const char* value(const ::sensor_msgs_ext::gnss_position_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.fix_3d);
      stream.next(m.latitude);
      stream.next(m.longitude);
      stream.next(m.altitude);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct gnss_position_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensor_msgs_ext::gnss_position_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sensor_msgs_ext::gnss_position_<ContainerAllocator>& v)
  {
    s << indent << "fix_3d: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.fix_3d);
    s << indent << "latitude: ";
    Printer<double>::stream(s, indent + "  ", v.latitude);
    s << indent << "longitude: ";
    Printer<double>::stream(s, indent + "  ", v.longitude);
    s << indent << "altitude: ";
    Printer<double>::stream(s, indent + "  ", v.altitude);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENSOR_MSGS_EXT_MESSAGE_GNSS_POSITION_H