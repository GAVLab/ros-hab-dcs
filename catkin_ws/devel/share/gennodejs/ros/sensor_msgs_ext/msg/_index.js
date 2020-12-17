
"use strict";

let proximity = require('./proximity.js');
let gnss_track = require('./gnss_track.js');
let covariance = require('./covariance.js');
let gnss_position = require('./gnss_position.js');
let time_reference = require('./time_reference.js');
let analog_voltage = require('./analog_voltage.js');
let temperature = require('./temperature.js');
let angular_velocity = require('./angular_velocity.js');
let acceleration = require('./acceleration.js');
let axis_state = require('./axis_state.js');
let magnetic_field = require('./magnetic_field.js');
let gnss_fix = require('./gnss_fix.js');

module.exports = {
  proximity: proximity,
  gnss_track: gnss_track,
  covariance: covariance,
  gnss_position: gnss_position,
  time_reference: time_reference,
  analog_voltage: analog_voltage,
  temperature: temperature,
  angular_velocity: angular_velocity,
  acceleration: acceleration,
  axis_state: axis_state,
  magnetic_field: magnetic_field,
  gnss_fix: gnss_fix,
};
