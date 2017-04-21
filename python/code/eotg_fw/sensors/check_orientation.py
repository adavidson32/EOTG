import math

def check_orientation(mpu):
  accel_data = mpu.get_accel_data()
  ax = float("{0:.3f}".format(accel_data['x']))
  ay = float("{0:.3f}".format(accel_data['y']))
  az = float("{0:.3f}".format(accel_data['z']))
  xz_fraction = math.fabs(ax / az)
  yz_fraction = math.fabs(ay / az)
  xz_angle = math.degrees(math.atan(xz_fraction))
  yz_angle = math.degrees(math.atan(yz_fraction))
  print("xz-angle: {0:.1f} deg.,  yz-angle: {1:.1f} deg.".format(xz_angle, yz_angle))
  if ((xz_angle <= 5) and (yz_angle <= 5)):
    return "level"
  elif ((xz_angle > 5) or (yz_angle  > 5)):
    return "not-level"
