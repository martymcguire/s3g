host_query_command_dict = {
  'GET_VERSION'               : 0,
  'INIT'                      : 1,
  'GET_AVAILABLE_BUFFER_SIZE' : 2,
  'CLEAR_BUFFER'              : 3,
  'GET_POSITION'              : 4,
  'ABORT_IMMEDIATELY'         : 7,
  'PAUSE'                     : 8,
  'TOOL_QUERY'                : 10,
  'IS_FINISHED'               : 11,
  'READ_FROM_EEPROM'          : 12,
  'WRITE_TO_EEPROM'           : 13,
  'CAPTURE_TO_FILE'           : 14,
  'END_CAPTURE'               : 15,
  'PLAYBACK_CAPTURE'          : 16,
  'RESET'                     : 17,
  'GET_NEXT_FILENAME'         : 18,
  'GET_BUILD_NAME'            : 20,
  'GET_EXTENDED_POSITION'     : 21,
  'EXTENDED_STOP'             : 22,
  'GET_MOTHERBOARD_STATUS'    : 23,
  'GET_COMMUNICATION_STATS'   : 26
}

host_action_command_dict = {
  'QUEUE_POINT'               : 129,
  'SET_POSITION'              : 130,
  'FIND_AXES_MINIMUMS'        : 131,
  'FIND_AXES_MAXIMUMS'        : 132,
  'DELAY'                     : 133,
  'WAIT_FOR_TOOL_READY'       : 135,
  'TOOL_ACTION_COMMAND'       : 136,
  'ENABLE_AXES'               : 137,
  'QUEUE_EXTENDED_POINT'      : 139,
  'SET_EXTENDED_POSITION'     : 140,
  'WAIT_FOR_PLATFORM_READY'   : 141,
  'QUEUE_EXTENDED_POINT_NEW'  : 142,
  'STORE_HOME_POSITIONS'      : 143,
  'RECALL_HOME_POSITIONS'     : 144,
  'SET_POT_VALUE'             : 145,
  'SET_RGB_LED'               : 146,
  'SET_BEEP'                  : 147,
  'WAIT_FOR_BUTTON'           : 148,
  'DISPLAY_MESSAGE'           : 149,
  'SET_BUILD_PERCENT'         : 150,
  'QUEUE_SONG'                : 151,
  'RESET_TO_FACTORY'          : 152,
  'BUILD_START_NOTIFICATION'  : 153,
  'BUILD_END_NOTIFICATION'    : 154,
}

slave_query_command_dict = {
  'GET_VERSION'                : 0,
  'GET_TOOLHEAD_TEMP'          : 2,
  'GET_MOTOR_1_SPEED_RPM'      : 17,
  'IS_TOOL_READY'              : 22,
  'READ_FROM_EEPROM'           : 25,
  'WRITE_TO_EEPROM'            : 26,
  'GET_PLATFORM_TEMP'          : 30,
  'GET_TOOLHEAD_TARGET_TEMP'   : 32,
  'GET_PLATFORM_TARGET_TEMP'   : 33,
  'IS_PLATFORM_READY'          : 35,
  'GET_TOOL_STATUS'            : 36,
  'GET_PID_STATE'              : 37,
}

slave_action_command_dict = {
  'INIT'                       : 1,
  'SET_TOOLHEAD_TARGET_TEMP'   : 3,
  'SET_MOTOR_1_SPEED_RPM'      : 6,
  'TOGGLE_MOTOR_1'             : 10,
  'TOGGLE_FAN'                 : 12,
  'TOGGLE_VALVE'               : 13,
  'SET_SERVO_1_POSITION'       : 14,
  'PAUSE'                      : 23,
  'ABORT'                      : 24,
  'SET_PLATFORM_TEMP'          : 31,
#  'SET_MOTOR_1_SPEED_DDA'      : 38, We are considering this deprecated, but some people use it in the wild so we are keeping it in here as a reminder
}

response_code_dict = {
  'GENERIC_ERROR'              : 0x80,
  'SUCCESS'                    : 0x81,
  'ACTION_BUFFER_OVERFLOW'     : 0x82,
  'CRC_MISMATCH'               : 0x83,
#  'QUERY_TOO_BIG'              : 0x84,
#  'COMMAND_NOT_SUPPORTED'      : 0x85,
  'DOWNSTREAM_TIMEOUT'         : 0x87,
  'TOOL_LOCK_TIMEOUT'          : 0x88,
  'CANCEL_BUILD'               : 0x89,
}

sd_error_dict = {
  'SUCCESS'                    : 000,
  'NO_CARD_PRESENT'            : 001,
  'INITIALIZATION_FAILED'      : 002,
  'PARTITION_TABLE_ERROR'      : 003,
  'FILESYSTEM_ERROR'           : 004,
  'DIRECTORY_ERROR'            : 005,
}

# TODO: convention for naming these?
header = 0xD5
maximum_payload_length = 32
max_retry_count = 5
timeout_length = .5
s3g_version = 100
max_tool_index = 127