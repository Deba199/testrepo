# Display the output
print("New python file")
class car:
  def __init__(self,a=40'):
     self._speed=a
  def get_speed(self):
     return self._speed
  def set_speed(self,a):
      self._speed=a
      return
  speed=property(get_speed,set_speed)
