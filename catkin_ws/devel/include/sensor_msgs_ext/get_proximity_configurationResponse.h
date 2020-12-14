// Generated by gencpp from file sensor_msgs_ext/get_proximity_configurationResponse.msg
// DO NOT EDIT!


#ifndef SENSOR_MSGS_EXT_MESSAGE_GET_PROXIMITY_CONFIGURATIONRESPONSE_H
#define SENSOR_MSGS_EXT_MESSAGE_GET_PROXIMITY_CONFIGURATIONRESPONSE_H


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
struct get_proximity_configurationResponse_
{
  typedef get_proximity_configurationResponse_<ContainerAllocator> Type;

  get_proximity_configurationResponse_()
    : radiation_type(0)
    , min_range(0.0)
    , max_range(0.0)
    , field_of_view(0.0)  {
    }
  get_proximity_configurationResponse_(const ContainerAllocator& _alloc)
    : radiation_type(0)
    , min_range(0.0)
    , max_range(0.0)
    , field_of_view(0.0)  {
  (void)_alloc;
    }



   typedef uint8_t _radiation_type_type;
  _radiation_type_type radiation_type;

   typedef float _min_range_type;
  _min_range_type min_range;

   typedef float _max_range_type;
  _max_range_type max_range;

   typedef float _field_of_view_type;
  _field_of_view_type field_of_view;



// reducing the odds to have name collisions with Windows.h 
#if defined(_WIN32) && defined(RADIATION_TYPE_UNSPECIFIED)
  #undef RADIATION_TYPE_UNSPECIFIED
#endif
#if defined(_WIN32) && defined(RADIATION_TYPE_ULTRASOUND)
  #undef RADIATION_TYPE_ULTRASOUND
#endif
#if defined(_WIN32) && defined(RADIATION_TYPE_INFRARED)
  #undef RADIATION_TYPE_INFRARED
#endif
#if defined(_WIN32) && defined(RADIATION_TYPE_RADAR)
  #undef RADIATION_TYPE_RADAR
#endif

  enum {
    RADIATION_TYPE_UNSPECIFIED = 255u,
    RADIATION_TYPE_ULTRASOUND = 0u,
    RADIATION_TYPE_INFRARED = 1u,
    RADIATION_TYPE_RADAR = 2u,
  };


  typedef boost::shared_ptr< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> const> ConstPtr;

}; // struct get_proximity_configurationResponse_

typedef ::sensor_msgs_ext::get_proximity_configurationResponse_<std::allocator<void> > get_proximity_configurationResponse;

typedef boost::shared_ptr< ::sensor_msgs_ext::get_proximity_configurationResponse > get_proximity_configurationResponsePtr;
typedef boost::shared_ptr< ::sensor_msgs_ext::get_proximity_configurationResponse const> get_proximity_configurationResponseConstPtr;

// constants requiring out of line definition

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator1> & lhs, const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator2> & rhs)
{
  return lhs.radiation_type == rhs.radiation_type &&
    lhs.min_range == rhs.min_range &&
    lhs.max_range == rhs.max_range &&
    lhs.field_of_view == rhs.field_of_view;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator1> & lhs, const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace sensor_msgs_ext

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bc6aa8c1ba0744c7248467a89aa5b3e1";
  }

  static const char* value(const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xbc6aa8c1ba0744c7ULL;
  static const uint64_t static_value2 = 0x248467a89aa5b3e1ULL;
};

template<class ContainerAllocator>
struct DataType< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "sensor_msgs_ext/get_proximity_configurationResponse";
  }

  static const char* value(const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "uint8 radiation_type                    # The type of radiation used by the sensor.\n"
"uint8 RADIATION_TYPE_UNSPECIFIED=255\n"
"uint8 RADIATION_TYPE_ULTRASOUND=0\n"
"uint8 RADIATION_TYPE_INFRARED=1\n"
"uint8 RADIATION_TYPE_RADAR=2\n"
"\n"
"float32 min_range                       # The minimum detection range of the sensor [m]\n"
"float32 max_range                       # The maximum detection range of the sensor [m]\n"
"\n"
"float32 field_of_view                   # The maximum FoV of the sensor [rad]\n"
;
  }

  static const char* value(const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.radiation_type);
      stream.next(m.min_range);
      stream.next(m.max_range);
      stream.next(m.field_of_view);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct get_proximity_configurationResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::sensor_msgs_ext::get_proximity_configurationResponse_<ContainerAllocator>& v)
  {
    s << indent << "radiation_type: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.radiation_type);
    s << indent << "min_range: ";
    Printer<float>::stream(s, indent + "  ", v.min_range);
    s << indent << "max_range: ";
    Printer<float>::stream(s, indent + "  ", v.max_range);
    s << indent << "field_of_view: ";
    Printer<float>::stream(s, indent + "  ", v.field_of_view);
  }
};

} // namespace message_operations
} // namespace ros

#endif // SENSOR_MSGS_EXT_MESSAGE_GET_PROXIMITY_CONFIGURATIONRESPONSE_H
