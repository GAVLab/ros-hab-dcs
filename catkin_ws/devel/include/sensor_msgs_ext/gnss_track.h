// Generated by gencpp from file sensor_msgs_ext/gnss_track.msg
// DO NOT EDIT!


#ifndef SENSOR_MSGS_EXT_MESSAGE_GNSS_TRACK_H
#define SENSOR_MSGS_EXT_MESSAGE_GNSS_TRACK_H


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
struct gnss_track_
{
  typedef gnss_track_<ContainerAllocator> Type;

  gnss_track_()
    : reference(0)
    , heading(0.0)
    , velocity(0.0)  {
    }
  gnss_track_(const ContainerAllocator& _alloc)
    : reference(0)
    , heading(0.0)
    , velocity(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _reference_type;
  _reference_type reference;

   typedef double _heading_type;
  _heading_type heading;

   typedef double _velocity_type;
  _velocity_type velocity;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(REFERENCE_TRUE_NORTH)
  #undef REFERENCE_TRUE_NORTH
#endif
#if defined(_WIN32) && defined(REFERENCE_MAGNETIC_NORTH)
  #undef REFERENCE_MAGNETIC_NORTH
#endif

  enum {
    REFERENCE_TRUE_NORTH = 0u,
    REFERENCE_MAGNETIC_NORTH = 1u,
  };


  typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> const> ConstPtr;

}; // struct gnss_track_

typedef ::sensor_msgs_ext::gnss_track_<std::allocator<void> > gnss_track;

typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_track > gnss_trackPtr;
typedef boost::shared_ptr< ::sensor_msgs_ext::gnss_track const> gnss_trackConstPtr;

// constants requiring out of line definition

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sensor_msgs_ext::gnss_track_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sensor_msgs_ext::gnss_track_<ContainerAllocator1> & lhs, const ::sensor_msgs_ext::gnss_track_<ContainerAllocator2> & rhs)
{
  return lhs.reference == rhs.reference &&
    lhs.heading == rhs.heading &&
    lhs.velocity == rhs.velocity;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sensor_msgs_ext::gnss_track_<ContainerAllocator1> & lhs, const ::sensor_msgs_ext::gnss_track_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sensor_msgs_ext

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
{
  static const char* value()
  {
    return "a14fcd5bdfa03784750802994cedd83c";
  }

  static const char* value(const ::sensor_msgs_ext::gnss_track_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xa14fcd5bdfa03784ULL;
  static const uint64_t static_value2 = 0x750802994cedd83cULL;
};

template<class ContainerAllocator>
struct DataType< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensor_msgs_ext/gnss_track";
  }

  static const char* value(const ::sensor_msgs_ext::gnss_track_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# An instantaneous velocity track as measured by a GNSS receiver.\n"
"\n"
"uint8 reference                       # The direction that the heading is in reference to.\n"
"uint8 REFERENCE_TRUE_NORTH = 0\n"
"uint8 REFERENCE_MAGNETIC_NORTH = 1\n"
"\n"
"float64 heading                         # The global heading of the track w.r.t. the reference [rad].\n"
"float64 velocity                        # The scalar velocity of the track, [m/s]\n"
;
  }

  static const char* value(const ::sensor_msgs_ext::gnss_track_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.reference);
      stream.next(m.heading);
      stream.next(m.velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct gnss_track_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensor_msgs_ext::gnss_track_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sensor_msgs_ext::gnss_track_<ContainerAllocator>& v)
  {
    s << indent << "reference: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.reference);
    s << indent << "heading: ";
    Printer<double>::stream(s, indent + "  ", v.heading);
    s << indent << "velocity: ";
    Printer<double>::stream(s, indent + "  ", v.velocity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENSOR_MSGS_EXT_MESSAGE_GNSS_TRACK_H
